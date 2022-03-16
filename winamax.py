
from matplotlib import dates
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
noms_pl_temp = browser.find_elements_by_xpath(
    '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a/div[2]/div[1]/div[1]/div[1]/div/span')
noms_pl = []
for x in noms_pl_temp:
    noms_pl.append(x.text)

'''On récupère les dates des matchs'''

dates_pl_temp = browser.find_elements_by_xpath(
    '//*[@id="app"]/div/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a/div[1]/div[2]/div')
dates_pl_temp = dates_pl_temp[:-1]

dates_pl = []
for x in dates_pl_temp:
    dates_pl.append(x.text)


# ---------------------------------------------------------------
# Winamax - Ligue des champions
# ---------------------------------------------------------------

browser.get('https://www.winamax.fr/paris-sportifs/sports/1/800000542/23')
time.sleep(1)


'''On récupère les cotes'''

liens = browser.find_elements_by_xpath(
    '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a')
cotes_ldc = []
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
            cotes_ldc.append(x.text)
except:
    None


'''On récupère les noms d'équipes'''
noms_ldc_temp = browser.find_elements_by_xpath(
    '//*[@id="app"]/div/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a/div[2]/div[1]/div[1]/div[1]/div/span')
noms_ldc = []
for x in noms_ldc_temp:
    noms_ldc.append(x.text)

'''On récupère les dates des matchs'''

dates_ldc_temp = browser.find_elements_by_xpath(
    '//*[@id="app"]/div/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a/div[1]/div[2]/div')
dates_ldc_temp = dates_ldc_temp

dates_ldc = []
for x in dates_ldc_temp:
    dates_ldc.append(x.text)


# ---------------------------------------------------------------
# Winamax - Ligue 1
# ---------------------------------------------------------------

browser.get('https://www.winamax.fr/paris-sportifs/sports/1/7/4')
time.sleep(1)


'''On récupère les cotes'''

cotes_l1_temp = browser.find_elements_by_xpath(
    '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a')
cotes_l1 = []
try:
    for lien in cotes_l1_temp:
        for i in range(0, 3):
            x = lien.get_property('lastChild')
            x = x.get_property('lastChild')
            x = x.get_property('lastChild')
            x = x.get_property('children')[0]
            x = x.get_property('children')[i]
            x = x.get_property('children')[1]
            x = x.get_property('children')[0]
            x = x.get_property('children')[1]
            cotes_l1.append(x.text)
except:
    None


'''On récupère les noms d'équipes'''
noms_l1_temp = browser.find_elements_by_xpath(
    '//*[@id="app"]/div/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a/div[2]/div[1]/div[1]/div[1]/div/span')
noms_l1 = []
for x in noms_l1_temp:
    noms_l1.append(x.text)

'''On récupère les dates des matchs'''

dates_l1_temp = browser.find_elements_by_xpath(
    '//*[@id="app"]/div/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a/div[1]/div[2]/div')
dates_l1_temp = dates_l1_temp[:-1]

dates_l1 = []
for x in dates_l1_temp:
    dates_l1.append(x.text)


# ---------------------------------------------------------------
# Winamax - Liga
# ---------------------------------------------------------------

browser.get('https://www.winamax.fr/paris-sportifs/sports/1/32/36')
time.sleep(1)


'''On récupère les cotes'''

cotes_liga_temp = browser.find_elements_by_xpath(
    '//*[@id="app"]/div[1]/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a')
cotes_liga = []
try:
    for lien in cotes_liga_temp:
        for i in range(0, 3):
            x = lien.get_property('lastChild')
            x = x.get_property('lastChild')
            x = x.get_property('lastChild')
            x = x.get_property('children')[0]
            x = x.get_property('children')[i]
            x = x.get_property('children')[1]
            x = x.get_property('children')[0]
            x = x.get_property('children')[1]
            cotes_liga.append(x.text)
except:
    None


'''On récupère les noms d'équipes'''
noms_liga_temp = browser.find_elements_by_xpath(
    '//*[@id="app"]/div/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a/div[2]/div[1]/div[1]/div[1]/div/span')
noms_liga = []
for x in noms_liga_temp:
    noms_liga.append(x.text)

'''On récupère les dates des matchs'''

dates_liga_temp = browser.find_elements_by_xpath(
    '//*[@id="app"]/div/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a/div[1]/div[2]/div')
dates_liga_temp = dates_liga_temp[:-1]

dates_liga = []
for x in dates_liga_temp:
    dates_liga.append(x.text)

print(cotes_liga, noms_liga, dates_liga)
