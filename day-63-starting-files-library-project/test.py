from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# create database
# ------------------------bingung nih---------------------------
class Base(DeclarativeBase):
    pass


# ---------------------------------------------------------------

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-booked-collection.db"

db = SQLAlchemy(model_class=Base)

# create extension
db.init_app(app)


# create a table (books)
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


# with app.app_context():
# db.create_all()
with app.app_context():
    #     new_book = Books(title="Harry Potter", author="J. K. Rowling", rating=9.3)
    #     new_book2 = Books(title="Harry Mcguire", author="J. K. Romland", rating=2.3)
    #     new_book3 = Books(title="Mr Potter", author="Rowling", rating=7.3)
    #     db.session.add(new_book)
    #     db.session.add(new_book2)
    #     db.session.add(new_book3)
    #     db.session.commit()
    books = db.session.execute(db.select(Books)).scalars()
    for book in books:
        print(book.title, book.author, book.rating, sep="\n")
