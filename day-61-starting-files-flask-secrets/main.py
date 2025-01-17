from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

admin_email = "admin@gmail.com"
admin_pass = "1234567890"

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[Email()])
    password = PasswordField(label='Password', validators=[Length(min=8)])
    submit = SubmitField(label='OK')


app = Flask(__name__)
app.secret_key = "bismillahlancar"
boot = Bootstrap5(app)

@app.route("/")
def home():
    return render_template('index.html', boot=boot)


@app.route("/login", methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == admin_email and login_form.password.data == admin_pass:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form, boot=boot)


if __name__ == '__main__':
    app.run(debug=True, port=5001)

