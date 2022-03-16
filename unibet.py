
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
# Unibet - Ligue des champions
# ---------------------------------------------------------------
browser.get(
    'https://www.unibet.fr/sport/football/ligue-des-champions/ligue-des-champions-matchs')
time.sleep(2)
'''On cherche les côtes '''
cotes_ldc_temp = browser.find_elements_by_xpath(
    '//*[@id="page__competitionview"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]')
cotes_ldc = []
for match in cotes_ldc_temp:
    for i in range(0, 3):
        x = match.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[i]
        x = x.get_property('children')[0]
        x = x.get_property('children')[2]
        cotes_ldc.append(x.text)

'''On cherche les noms d'équipes'''

noms_ldc_temp = browser.find_elements_by_xpath(
    '//*[@id="page__competitionview"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/span')
noms_ldc = []
for x in noms_ldc_temp:
    noms_ldc.append(x.text.split('-'))


# ---------------------------------------------------------------
# Unibet - Ligue1
# ---------------------------------------------------------------
browser.get(
    'https://www.unibet.fr/sport/football/ligue-1-ubereats/ligue-1-matchs')
time.sleep(2)
'''On cherche les côtes '''
cotes_l1_temp = browser.find_elements_by_xpath(
    '//*[@id="page__competitionview"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]')
cotes_l1 = []
for match in cotes_l1_temp:
    for i in range(0, 3):
        x = match.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[i]
        x = x.get_property('children')[0]
        x = x.get_property('children')[2]
        cotes_l1.append(x.text)
'''On cherche les noms d'équipes'''

noms_l1_temp = browser.find_elements_by_xpath(
    '//*[@id="page__competitionview"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/span')
noms_l1 = []
for x in noms_l1_temp:
    noms_l1.append(x.text.split('-'))


# ---------------------------------------------------------------
# Unibet - Premier League
# ---------------------------------------------------------------
browser.get(
    'https://www.unibet.fr/sport/football/premier-league/matchs')
time.sleep(2)
'''On cherche les côtes '''
cotes_pl_temp = browser.find_elements_by_xpath(
    '//*[@id="page__competitionview"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]')
cotes_pl = []
for match in cotes_pl_temp:
    for i in range(0, 3):
        x = match.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[i]
        x = x.get_property('children')[0]
        x = x.get_property('children')[2]
        cotes_pl.append(x.text)
'''On cherche les noms d'équipes'''

noms_pl_temp = browser.find_elements_by_xpath(
    '//*[@id="page__competitionview"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/span')
noms_pl = []
for x in noms_pl_temp:
    noms_pl.append(x.text.split('-'))


# ---------------------------------------------------------------
# Unibet - Liga
# ---------------------------------------------------------------
browser.get(
    'https://www.unibet.fr/sport/football/liga/matchs')
time.sleep(2)
'''On cherche les côtes '''
cotes_liga_temp = browser.find_elements_by_xpath(
    '//*[@id="page__competitionview"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]')
cotes_liga = []
for match in cotes_liga_temp:
    for i in range(0, 3):
        x = match.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[0]
        x = x.get_property('children')[i]
        x = x.get_property('children')[0]
        x = x.get_property('children')[2]
        cotes_liga.append(x.text)
'''On cherche les noms d'équipes'''

noms_liga_temp = browser.find_elements_by_xpath(
    '//*[@id="page__competitionview"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/span')
noms_liga = []
for x in noms_liga_temp:
    noms_liga.append(x.text.split('-'))
