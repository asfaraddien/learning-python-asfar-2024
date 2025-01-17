import requests
import datetime as dt
import smtplib

my_email = "asfar.addien@gmail.com"
my_pass = "wwkd tpvs mexb wpvn"

# ---------------buat email--------------
def send_mail(date, time, loc, anda):
    with smtplib.SMTP("smtp.gmail.com", port=587) as post:
        post.starttls()
        post.login(my_email, my_pass)
        post.sendmail(my_email, my_email, f"subject:Berita Terbaru!\n\n"
                                          f"ISS mendekat menuju rumahmu, adapun posisi ISS sekarang:\n"
                                          f"Tanggal      : {date}\n"
                                          f"Pukul         : {time}\n"
                                          f"Lokasi ISS   : {loc}\n"
                                          f"Lokasi anda : {anda}\n\n"
                                          f"Siapkan teleskopmu dan dongakan kepalamu!")


# ---------------iss coordinate--------------
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

iss_lng = float(data["iss_position"]["longitude"])
iss_lat = float(data["iss_position"]["latitude"])

# ---------------our sunset and sunrise--------------

my_lng = 106.669708
my_lat = -6.227181

parameter = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0,
}

response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response2.raise_for_status()
data2 = response2.json()

sunset = int(data2["results"]["sunset"].split("T")[1].split(":")[0])
sunrise = int(data2["results"]["sunrise"].split("T")[1].split(":")[0])


time_now = dt.datetime.now()
time_now = time_now.hour

print(f"{sunset}\n{sunrise}")
print(time_now)
print(iss_lat, iss_lng)
print(my_lat, my_lng)



# ---------------buat logika--------------
tanggal = dt.datetime.now().date()
pukul = dt.datetime.now().time().replace(microsecond=0)
loc = f"{iss_lat}, {iss_lng}"
anda = f"{my_lat}, {my_lng}"
if sunset <= time_now <= sunrise and abs(iss_lat - my_lat) <= 5 and abs(iss_lng - my_lng) <= 5:
    send_mail(tanggal, pukul, loc, anda)

print(pukul)