import smtplib
import pandas as pd
import datetime as dt
from random import randint

PLACEHOLDER = "[NAME]"
my_email = "asfar.addien@gmail.com"
my_pass = "wwkd tpvs mexb wpvn"

# ---------------buat smptlib--------------
def send_wish(to, msg):
    with smtplib.SMTP("smtp.gmail.com", port=587) as postman:
        postman.starttls()
        postman.login(user=my_email, password=my_pass)
        postman.sendmail(my_email,to, msg=f"subject:Happy Birthday\n\n{msg}")

# ---------------import file--------------
data = pd.read_csv("birthdays.csv")


# ---------------buat waktu--------------
now = dt.datetime.now()
month_now = now.month
day_now = now.day

# ---------------cek hari--------------
global name, email, birth
for (i, v) in data.iterrows():
    if v.month == month_now and v.day == day_now:
        name = v["name"]
        email = v.email
        birth = dt.datetime(int(v.year), int(v.month), int(v.day))
        print(f"{name}\n{email}\n{birth}")
# ---------------rubah template--------------
        pilih = randint(1, 3)
        with open(f"letter_templates/letter_{pilih}.txt") as temp:
            text = temp.readlines()
            text = "".join(text).replace(PLACEHOLDER, name)

# ---------------kirim--------------
        send_wish(email, text)





