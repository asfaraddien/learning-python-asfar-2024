from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy, record_queries
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import choice
import re

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_RECORD_QUERIES'] = True
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def __repr__(self):
        return f"{self.name}"

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    recorded = record_queries.get_recorded_queries()
    for i in recorded:
        print(i.statement, i.parameters, sep="|")
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def get():
    random_cafe = choice(db.session.execute(db.select(Cafe)).scalars().all())
    return jsonify(
        main_info=dict(id=random_cafe.id,
                       name=random_cafe.name,
                       map_url=random_cafe.map_url,
                       location=random_cafe.location),
        others=dict(img_url=random_cafe.img_url,
                    seats=random_cafe.seats,
                    has_toilet=random_cafe.has_toilet,
                    has_wifi=random_cafe.has_wifi,
                    has_sockets=random_cafe.has_sockets,
                    can_take_calls=random_cafe.can_take_calls,
                    coffee_price=random_cafe.coffee_price)
    )


@app.route('/all')
def all():
    all_cafe = db.session.execute(db.select(Cafe)).scalars().all()
    all_cafe_list = []
    for cafe in all_cafe:
        choosen = {'id': cafe.id, 'name': cafe.name, 'map_url': cafe.map_url, 'location': cafe.location,
                   'img_url': cafe.img_url, 'seats': cafe.seats, 'has_toilet': cafe.has_toilet,
                   'has_wifi': cafe.has_wifi, 'has_sockets': cafe.has_sockets, 'can_take_calls': cafe.can_take_calls,
                   'coffee_price': cafe.coffee_price}

        all_cafe_list.append(choosen)
    return jsonify(all_cafe_list)


@app.route("/search")
def search():
    q = request.args.get('loc').title()

    all_cafe = db.session.execute(db.select(Cafe).where(Cafe.location == q)).scalars().all()
    list_cafes = []
    if all_cafe:
        for cafe in all_cafe:
            choosen = {'id': cafe.id, 'name': cafe.name, 'map_url': cafe.map_url, 'location': cafe.location,
                       'img_url': cafe.img_url, 'seats': cafe.seats, 'has_toilet': cafe.has_toilet,
                       'has_wifi': cafe.has_wifi, 'has_sockets': cafe.has_sockets, 'can_take_calls': cafe.can_take_calls,
                       'coffee_price': cafe.coffee_price}
            list_cafes.append(choosen)
        return jsonify(list_cafes)
    else:
        return jsonify(errors={"not found": "Sorry, you should give another keyword"})


# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafe(
                # id=request.form['id'],
                name=request.form['name'],
                map_url=request.form['map_url'],
                location=request.form['location'],
                img_url=request.form['img_url'],
                seats=request.form['seats'],
                has_toilet=bool(request.form['has_toilet']),
                has_wifi=bool(request.form['has_wifi']),
                has_sockets=bool(request.form['has_sockets']),
                can_take_calls=bool(request.form['can_take_calls']),
                coffee_price=request.form['coffee_price']
            )

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Your cafe has been added to database"})
# HTTP PUT/PATCH - Update Record
@app.route('/edit/<int:cafe_id>', methods=['PATCH'])
def edit(cafe_id):
    cafe_editable = db.session.get(Cafe, cafe_id)
    print(cafe_editable)
    if cafe_editable:
        cafe_editable.coffee_price = f"£{request.args.get('price')}"
        db.session.commit()
        return jsonify(response={"success": f"cafe '{cafe_editable}' has been edited"})
    else:
        return jsonify(errors={"Id Not Found": "You should give the correct keyword"}), 404

# HTTP DELETE - Delete Record
@app.route('/delete', methods=['DELETE'])
def delete():
    api_key = request.args.get('api-key')
    cafe_id = request.args.get('id')
    if api_key == "123456":
       deleted = db.session.get(Cafe, cafe_id)
       if deleted:
           db.session.delete(deleted)
           db.session.commit()
           return jsonify(response={"success": "Thanks for deleting."})
       else:
           return jsonify(error={"error 404": "The cafe was not found."}), 404
    else:
        return jsonify(error={"error 403": "you have input the wrong api key."}), 403


if __name__ == '__main__':
    app.run(debug=False)

