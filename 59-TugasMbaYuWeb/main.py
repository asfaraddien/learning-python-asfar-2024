from flask import Flask, render_template, request as rq
import requests
import smtplib

my_email = "asfar.addien@gmail.com"
my_pass = "wwkd tpvs mexb wpvn"

url = "https://api.npoint.io/7b56f37af897ff14a77a"
res = requests.get(url)
data = res.json()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', blog=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if rq.method == "POST":
        name = rq.form['name']
        email = rq.form['email']
        phone = rq.form['phone']
        msg = rq.form['message']
        with smtplib.SMTP("smtp.gmail.com", port=587) as postman:
            postman.starttls()
            postman.login(user=my_email, password=my_pass)
            postman.sendmail(my_email, my_email, msg=f"subject:TEST DOANG\n\n"
                                                     f"name     :{name}\n"
                                                     f"email    :{email}\n"
                                                     f"phone    :{phone}\n"
                                                     f"message  :{msg}")

        return "<h1>Successfully Sent</h1>"
    return render_template('contact.html')

@app.route('/post/<int:num>')
def blog(num):
    chosen = [post for post in data if post['id'] == num][0]
    return render_template('post.html', data=chosen)

if __name__ == "__main__":
    app.run(debug=True)