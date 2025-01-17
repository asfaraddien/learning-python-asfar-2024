from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)


driver = webdriver.Chrome()
driver.get("https://www.python.org/")


order = {}
for i in range(1, 6):
    datat = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/time')
    datae = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/a')
    time = datat.get_attribute("datetime").split("T")[0]
    eve = datae.text
    order[i - 1]= {"time": time, "event": eve}
print(order)



