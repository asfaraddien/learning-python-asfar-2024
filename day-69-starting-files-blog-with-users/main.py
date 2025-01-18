from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy.exc import IntegrityError
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)
Gravatar(app, size=100,
         rating='g',
         default='retro',
         force_default=False,
         force_lower=False,
         use_ssl=False,
         base_url=None)


def admin_only(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if current_user.id != 1:
            abort(403)
        return function(*args, **kwargs)

    return wrapper


# TODO: Configure Flask-Login
manager = LoginManager()
manager.init_app(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="posts")

    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    comments = relationship("Comments", back_populates="blog_author")


# TODO: Create a User table for all your registered users.
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(250), unique=True)
    password: Mapped[int] = mapped_column(Integer, nullable=False)
    name: Mapped[str] = mapped_column(String(250), nullable=False)

    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comments", back_populates="comment_author")


# MAKE COMMENT TABLE
class Comments(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    comment_author: Mapped[User] = relationship("User", back_populates="comments")

    blog_id = mapped_column(Integer, ForeignKey("blog_posts.id"))
    blog_author = relationship("BlogPost", back_populates="comments")

    text: Mapped[str] = mapped_column(Text, nullable=False)


with app.app_context():
    db.create_all()


@manager.user_loader
def user_load(id_user):
    return db.get_or_404(User, id_user)


# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            email=form.email.data,
            password=generate_password_hash(form.password.data, method="pbkdf2", salt_length=8),
            name=form.name.data
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            flash("Email sudah pernah terdaftar di database kami. Silahkan login")
            return redirect(url_for('login'))
        else:
            login_user(new_user)
            return redirect(url_for('get_all_posts'))

    return render_template("register.html", form=form, masuk=current_user)


# TODO: Retrieve a user from the database based on their email. 
@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        auth = db.session.execute(db.select(User).where(User.email == login_form.email.data)).scalar()
        if auth:
            if check_password_hash(auth.password, login_form.password.data):
                login_user(auth)
                return redirect(url_for('get_all_posts'))
            else:
                flash("Password yang anda masukan salah.")
        else:
            flash("Email tidak terdaftar di database.")
    return render_template("login.html", form=login_form, masuk=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts, masuk=current_user)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>", methods=['POST', 'GET'])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comments = db.session.execute(db.select(Comments)).scalars().all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        if current_user.is_authenticated:
            new_comment = Comments(
                text=comment_form.text.data,
                comment_author=current_user,
                blog_author=requested_post

            )
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for("show_post", post_id=post_id))
        else:
            flash("Kamu belum login, silahkan login terlebih dahulu")
            return redirect(url_for('login'))
    return render_template("post.html", post=requested_post, masuk=current_user, form=comment_form, comments=comments)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, masuk=current_user)


# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True, masuk=current_user)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# ------------------------TIDAK BERFUNGSI------------------------
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# ---------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=5002)
