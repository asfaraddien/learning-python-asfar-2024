from flask import Flask

app = Flask(__name__)


# ---------- Make decorators -----------
def make_bold(bolded):
    def decorations():
        return "<b>"+bolded()+"</b>"

    return decorations


@app.route("/")
@make_bold
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test/<int:number>")
def cal(number):
    return f"{number + 2}"


if __name__ == "__main__":
    app.run(debug=True)
