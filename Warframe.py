import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import pandas as pd

data = datetime.now()

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1920,1080")


# preco = int(input("What is the maximum value you'd pay in Platinum? "))

url = "https://warframe.market/items/"

driver = webdriver.Chrome(options=options)


with (
    "cleaned-data.json",
    "r+",
) as file:
    item = [file]

    for object in item:
        driver.get(url + object["url_name"])


# driver.get(url + item)

valor = driver.find_element(
    "xpath", '//*[@id="panel"]/section[2]/div[2]/div[2]/div/div[3]/div[1]/input'
)
# valor.send_keys(preco)

BTN_Online = driver.find_element(
    "xpath", '//*[@id="panel"]/section[2]/div[2]/div[2]/div/div[2]/div/label[3]'
)
BTN_Online.click()

BTN_Price = driver.find_element(
    "xpath", '//*[@id="panel"]/section[2]/div[3]/div[2]/div[1]/div[4]'
)
BTN_Price.click()
sleep(0.5)
BTN_Price.click()
sleep(0.5)
BTN_Price.click()

sleep(1)
driver.execute_script("window.scrollTo(0, 550)")
sleep(2)

site = BeautifulSoup(driver.page_source, "html.parser")

name_finder = site.find("div", attrs={"class": "name--aAXSV"})
print("Item: {}".format(name_finder.text))

item_finders = site.findAll(
    "div", attrs={"class": "row order-row--Alcph"}
) + site.findAll("div", attrs={"class": "row order-row--Alcph odd--ZOeJx"})

temp = []
for item_finder in item_finders:

    price_finder = item_finder.find(
        "div", attrs={"class": "platinum-price--DQ63t sell--UxmH0"}
    )
    temp.append(price_finder.text)
print(f"Price: {temp[0]}")
# print("Price: {}".format(price_finder.text))

print(" ")
print(" ")
