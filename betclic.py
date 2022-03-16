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

cotes_ldc = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/sports-events-event-markets/sports-markets-default[1]/div/sports-selections-selection/div[1]/span[2]')


'''On cherche les noms des équipes'''

nom_ldc = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/scoreboards-scoreboard/scoreboards-scoreboard-global/div/div/div')


'''On cherche les dates'''

date_ldc = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/sports-events-event-info/div')
'''Mise en forme des données'''


# ---------------------------------------------------------------
# Betclic Premier League
# ---------------------------------------------------------------

browser.get('https://www.betclic.fr/football-s1/angl-premier-league-c3')
time.sleep(2)

cotes_pl = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/sports-events-event-markets/sports-markets-default[1]/div/sports-selections-selection/div[1]/span[2]')

nom_pl = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/scoreboards-scoreboard/scoreboards-scoreboard-global/div/div/div')

date_pl = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/sports-events-event-info/div')


# ---------------------------------------------------------------
# Betclic Ligue 1
# ---------------------------------------------------------------

browser.get('https://www.betclic.fr/football-s1/ligue-1-uber-eats-c4')
time.sleep(1)

cotes_l1 = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/sports-events-event-markets/sports-markets-default[1]/div/sports-selections-selection/div[1]/span[2]')

nom_l1 = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/scoreboards-scoreboard/scoreboards-scoreboard-global/div/div/div')

date_l1 = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/sports-events-event-info/div')


# ---------------------------------------------------------------
# Betclic Liga
# ---------------------------------------------------------------

browser.get('https://www.betclic.fr/football-s1/espagne-liga-primera-c7')
time.sleep(1)

cotes_liga = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/sports-events-event-markets/sports-markets-default[1]/div/sports-selections-selection/div[1]/span[2]')

nom_liga = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/scoreboards-scoreboard/scoreboards-scoreboard-global/div/div/div')

date_liga = browser.find_elements_by_xpath(
    '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/sports-events-event-info/div')
