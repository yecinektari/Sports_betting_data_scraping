# Projet

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
# Betclic - Ligue des champions
# ---------------------------------------------------------------

'''On cherche les côtes'''

browser.get('https://www.betclic.fr/football-s1/ligue-des-champions-c8')
time.sleep(2)
button = browser.find_element_by_xpath('//*[@id="popin_tc_privacy_button_2"]')
button.click()

cotes_ldc_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/sports-events-event-markets/sports-markets-default[1]/div/sports-selections-selection/div[1]/span[2]')
cotes_ldc = []
for x in cotes_ldc_temp:
    cotes_ldc.append(x.text)

'''On cherche les noms des équipes'''

nom_ldc_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/scoreboards-scoreboard/scoreboards-scoreboard-global/div/div/div')
nom_ldc = []
for x in nom_ldc_temp:
    nom_ldc.append(x.text)

'''On cherche les dates'''

date_ldc_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/sports-events-event-info/div')
'''Mise en forme des données'''
date_ldc = []
for x in date_ldc_temp:
    date_ldc.append(x.text)

# ---------------------------------------------------------------
# Betclic Premier League
# ---------------------------------------------------------------

browser.get('https://www.betclic.fr/football-s1/angl-premier-league-c3')
time.sleep(2)

cotes_pl_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/sports-events-event-markets/sports-markets-default[1]/div/sports-selections-selection/div[1]/span[2]')
cotes_pl = []
for x in cotes_pl_temp:
    cotes_pl.append(x.text)

nom_pl_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/scoreboards-scoreboard/scoreboards-scoreboard-global/div/div/div')
nom_pl = []
for x in nom_pl_temp:
    nom_pl.append(x.text)


date_pl_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/sports-events-event-info/div')
date_pl = []
for x in date_pl_temp:
    date_pl.append(x.text)


# ---------------------------------------------------------------
# Betclic Ligue 1
# ---------------------------------------------------------------

browser.get('https://www.betclic.fr/football-s1/ligue-1-uber-eats-c4')
time.sleep(1)

cotes_l1_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/sports-events-event-markets/sports-markets-default[1]/div/sports-selections-selection/div[1]/span[2]')
cotes_l1 = []
for x in cotes_l1_temp:
    cotes_l1.append(x.text)


nom_l1_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/scoreboards-scoreboard/scoreboards-scoreboard-global/div/div/div')
nom_l1 = []
for x in nom_l1_temp:
    nom_l1.append(x.text)


date_l1_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/sports-events-event-info/div')
date_l1 = []
for x in date_l1_temp:
    date_l1.append(x.text)

# ---------------------------------------------------------------
# Betclic Liga
# ---------------------------------------------------------------

browser.get('https://www.betclic.fr/football-s1/espagne-liga-primera-c7')
time.sleep(1)

cotes_liga_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/sports-events-event-markets/sports-markets-default[1]/div/sports-selections-selection/div[1]/span[2]')
cotes_liga = []
for x in cotes_liga_temp:
    cotes_liga.append(x.text)


nom_liga_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/scoreboards-scoreboard/scoreboards-scoreboard-global/div/div/div')
nom_liga = []
for x in nom_liga_temp:
    nom_liga.append(x.text)


date_liga_temp = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/sports-events-event-info/div')
date_liga = []
for x in date_liga_temp:
    date_liga.append(x.text)
