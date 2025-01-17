from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


manager = LoginManager()
manager.init_app(app)


# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


@manager.user_loader
def user_load(id_user):
    return db.session.get(User, id_user)


with app.app_context():
    db.create_all()



@app.route('/')
def home():
    return render_template("index.html", masuk=current_user.is_authenticated)


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        try:
            hash_method = "pbkdf2"
            new_user = User(
                email=request.form['email'],
                name=request.form["name"],
                password=generate_password_hash(request.form['password'], method=hash_method, salt_length=8)
            )
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            flash("Email sudah ada di database. Silahkan login!")
            return redirect(url_for('login'))
        else:
            login_user(new_user)
            return redirect(url_for('secrets'))

    return render_template("register.html", masuk=current_user.is_authenticated)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        res = db.session.execute(db.select(User).where(User.email == request.form['email'])).scalar()
        if res:
            if check_password_hash(pwhash=res.password, password=request.form['password']):
                login_user(res)
                return redirect(url_for('secrets'))
            else:
                flash("Password tidak sesuai.")
        else:
            flash("Email tidak ditemukan di database.")
    return render_template("login.html", masuk=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", masuk=True)


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
