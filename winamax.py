
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os  # permet d'aller écrire dans les répertoires
from openpyxl import Workbook
import pandas as pd


option = webdriver.ChromeOptions()
option.add_argument("--incognito")  # Navigation privée
# option.add_argument("kiosk")  # grand ecran sur mac
#prefs={"profile.managed_default_content_settings.images": 2, 'disk-cache-size': 4096 }
#option.add_experimental_option('prefs', prefs)

browser = webdriver.Chrome(
    executable_path="/Users/thomasbouiniere/Desktop/Scrapping/chromedriver", options=option)

# ---------------------------------------------------------------
# Winamax - Premier League
# ---------------------------------------------------------------

browser.get('https://www.winamax.fr/paris-sportifs/sports/1/1/1')
time.sleep(1)

'''On récupère les cotes'''

liens = browser.find_elements_by_xpath(
    '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a')
cotes_pl = []
try:
    for lien in liens:
        for i in range(0, 3):
            x = lien.get_property('lastChild')
            x = x.get_property('lastChild')
            x = x.get_property('lastChild')
            x = x.get_property('children')[0]
            x = x.get_property('children')[i]
            x = x.get_property('children')[1]
            x = x.get_property('children')[0]
            x = x.get_property('children')[1]
            cotes_pl.append(x.text)
except:
    None


'''On récupère les noms d'équipes'''
# noms_pl = browser.find_elements_by_xpath(
#     '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a/div[2]/div[1]/div[1]/div[1]/div/span')
# print(noms_pl)
