from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)
# create database
# ------------------------bingung nih---------------------------
class Base(DeclarativeBase):
    pass
# ---------------------------------------------------------------

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-asfarbooks-collection.db"

db = SQLAlchemy(model_class=Base)


# create extension
db.init_app(app)


# create a table (books)
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


with app.app_context():
    db.create_all()







@app.route('/')
def home():

    all_book = db.session.execute(db.select(Book)).scalars()
    all_book = [i for i in all_book]

    return render_template('index.html', library=all_book)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == "POST":
        data = request.form.to_dict()
        # print(data)
        # all_books.append(data)

        new_book = Book(title=data["title"], author=data["author"], rating=data["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        book_changed = db.get_or_404(Book, request.form["id"])
        book_changed.rating = float(request.form['edit'])
        db.session.commit()
        return redirect(url_for('home'))
    book_num = request.args.get('id', type=int)
    book_change = db.get_or_404(Book, book_num)
    return render_template('edit.html', book=book_change)

@app.route('/delete')
def delete():
    id = request.args.get("id", type=int)
    deleted = db.get_or_404(Book, id)
    db.session.delete(deleted)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=False, port=5001)
