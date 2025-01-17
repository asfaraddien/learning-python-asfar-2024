from flask import Flask, render_template
from post import Post

post = Post()
data = post.data
app = Flask(__name__)

@app.route('/post')
def home():
    return render_template("index.html", posts=data)

@app.route('/post/<int:num>')
def blog(num):
    post.milih(num)
    return render_template('post.html', num=num, post=post)

if __name__ == "__main__":
    app.run(debug=True)
