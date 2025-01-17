from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
# ------------------NYARI SENDIRI--------------------
# sc = webdriver.Chrome(options=option)
# sc.get("https://en.wikipedia.org/wiki/Main_Page")

# data = sc.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text
# print(data)

# ------------------ISI SENDIRI--------------------
# sc2 = webdriver.Chrome(options=option)
# sc2.get("https://secure-retreat-92358.herokuapp.com/")
#
# sc2.find_element(By.NAME, "fName").send_keys("test")
# sc2.find_element(By.NAME, "lName").send_keys("test2")
# sc2.find_element(By.NAME, "email").send_keys("email@email.com", Keys.ENTER)

# ------------------TUGAS DARI MBA YU--------------------
clicker = webdriver.Chrome(options=option)
clicker.get(url="http://orteil.dashnet.org/experiments/cookie/")
# clicker.find_element(By.ID, "langSelect-EN").click()

def cookie_clicker():
    clicker.find_element(By.ID, 'cookie').click()

while True:
    cookie_clicker()

# sc.quit()