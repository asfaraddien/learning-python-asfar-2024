from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("MOVIE_API")
end_search = "https://api.themoviedb.org/3/search/movie"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///favorite-movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(500), nullable=True)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)

# with app.app_context():
#     db.create_all()




class EditForm(FlaskForm):
    edit_rating = StringField(label="Your Rating Out Of 10", validators=[DataRequired()])
    edit_review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Save")

class AddForm(FlaskForm):
    movie = StringField(label="Movie Name", validators=[DataRequired()])
    submit = SubmitField(label="Search Movie")


@app.route("/")
def home():
    data = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars().all()
    for item in data:
        item.ranking = data.index(item) + 1
        # print(item.ranking, data.index(item), sep="|")
    db.session.commit()
    return render_template("index.html", data=data)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    movie_num = request.args.get('id', type=int)
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        changed = db.get_or_404(Movie, movie_num)
        changed.rating = float(edit_form.edit_rating.data)
        changed.review = edit_form.edit_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=edit_form)


@app.route('/delete')
def delete():
    movie_num = request.args.get("id", type=int)
    deleted_movie = db.get_or_404(Movie, movie_num)
    db.session.delete(deleted_movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/add', methods=['POST', 'GET'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        param = {
            "api_key":api_key,
            "query":add_form.movie.data,

        }
        res = requests.get(url=end_search, params=param)
        data = res.json()
        movies = [(movie["id"], movie["title"], movie["release_date"]) for movie in data["results"]]
        return render_template('select.html', movies=movies)
    return render_template('add.html', form=add_form)

@app.route('/find')
def find():
    movie_id = request.args.get("id", type=int)
    end_find = f"https://api.themoviedb.org/3/movie/{movie_id}"
    print(end_find)
    param2 = {
        "api_key": api_key
    }

    res2 = requests.get(url=end_find, params=param2)
    movie_chosen = res2.json()
    new_movie = Movie(
            title=movie_chosen["title"],
            year=movie_chosen["release_date"].split("-")[0],
            description=movie_chosen["overview"],
            img_url=f"https://image.tmdb.org/t/p/w500{movie_chosen['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))



if __name__ == '__main__':
    app.run(debug=True, port=5001)
