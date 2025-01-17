from flask import Flask, render_template
import random
import datetime as dt
import requests




# ---------server----------
app = Flask(__name__)


@app.route('/')
def home():
    number = random.randint(0, 10)
    return render_template("index.html", num=number, year=dt.datetime.now().year)

# ----------------- TERNYATA ADA AUTHENTICATION GUYS ----------------------
# @app.route('/guess/<name>')
# def name(name):
#     # ---------API----------
#     head = {
#         "name": name
#     }
#
#     # res = requests.get("https://api.genderize.io", headers=head)
#     # data = res.json()
#     # print(res.raise_for_status())
#     # gender = data["gender"]
#
#     res2 = requests.get("https://api.agify.io", headers=head)
#     data2 = res2.json()
#     print(res2.raise_for_status())
#     age = data2["age"]
#     return render_template("predict.html", name=name, age=age)
# ----------------- ------------------- ----------------------

@app.route('/blog/<int:num>')
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    res = requests.get(blog_url)
    posts = res.json()
    return render_template("blog.html", posts=posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)


