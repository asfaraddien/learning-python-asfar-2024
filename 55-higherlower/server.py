from flask import Flask
from random import randint

ditebak = randint(1, 9)
myapp = Flask(__name__)


# def dec_ran(fungsi):
#     def hiasan(*args):
#         fungsi()
#     return hiasan


@myapp.route('/')
def home():
    return ('<h1>Guess the number please</h1>'
            '<iframe src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="480" height="480" style="" '
            'frameBorder="0" class="giphy-embed" allowFullScreen></iframe>')


@myapp.route('/<int:num>')
def guess(num):
    if num == ditebak:
        return f"<h1>Kerja bagus</h1>"
    elif num > ditebak:
        return f"<h1>Ketinggian tebakan lu!</h1>"
    elif num < ditebak:
        return f"<h1>kerendahan tebakan lu!</h1>"

if __name__ == "__main__":
    myapp.run(debug=False)
