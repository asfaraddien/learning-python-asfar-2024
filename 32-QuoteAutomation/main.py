import datetime as dt
import smtplib
from random import choice
my_email = "asfar.addien@gmail.com"
my_pass = "wwkd tpvs mexb wpvn"

# ---------------buat waktu--------------
now = dt.datetime.now()

if now.weekday() == 0:
# ---------------buka file--------------

    with open("quotes.txt") as data:
        quotes = data.readlines()
        quote = choice(quotes).strip()

# ---------------buat email automation--------------

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as postman:
        postman.starttls()
        postman.login(user=my_email, password=my_pass)
        postman.sendmail(from_addr=my_email,
                            to_addrs="asfaraddien05@gmail.com",
                            msg=f"subject:Quote of the day\n\n{quote}")

