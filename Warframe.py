from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import pandas as pd

data = datetime.now()

options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1920,1080')

item = input("Qual item deseja pesquisar? ")
preco = int(input("Qual o valor maximo em PL? "))

url = 'https://warframe.market/items/'

driver = webdriver.Chrome(options=options)
driver.get(url + item)

valor = driver.find_element('xpath','//*[@id="panel"]/section[2]/div[2]/div[2]/div/div[3]/div[1]/input')
valor.send_keys(preco)

BTN_Online = driver.find_element('xpath','//*[@id="panel"]/section[2]/div[2]/div[2]/div/div[2]/div/label[3]')
BTN_Online.click()

BTN_Price = driver.find_element('xpath','//*[@id="panel"]/section[2]/div[3]/div[2]/div[1]/div[4]')
BTN_Price.click()
sleep(0.5)
BTN_Price.click()
sleep(0.5)
BTN_Price.click()

sleep(1)
driver.execute_script("window.scrollTo(0, 550)")
sleep(2)

site = BeautifulSoup(driver.page_source, 'html.parser')

name_finder = site.find('div', attrs={'class':'name--aAXSV'})
print("Item: {}".format(name_finder.text))

item_finders = site.findAll('div', attrs={'class':'row order-row--Alcph'}) + site.findAll('div', attrs={'class':'row order-row--Alcph odd--ZOeJx'})

for item_finder in item_finders:

    user_finder = item_finder.find('span', attrs={'class':'user__name--xF_ju'})
    print("User: {}".format(user_finder.text))

    status_finder = item_finder.find('div', attrs={'class':'order-row__user-status--RkMKE'})
    print("Status: {}".format(status_finder.text))

    rep_finder = item_finder.find('div', attrs={'class':'order-row__user-reputation--lGJbY'})
    print("Reputation: {}".format(rep_finder.text))

    price_finder = item_finder.find('div', attrs={'class':'platinum-price--DQ63t sell--UxmH0'})
    print("Price: {}".format(price_finder.text))

    quant_finder = item_finder.find('div', attrs={'class':'quantity--Z_gE9'})
    print("Quantity: {}".format(quant_finder.text))

    print(" ")
    print("Link to Call:")
    print("/w {} Hi! I want to buy: {} for {} platinum. (warframe.market)".format(user_finder.text, name_finder.text, price_finder.text))
    print(" ")
    print(" ")