
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
# Betclic
# ---------------------------------------------------------------
compets_betclic = {'ldc': 'https://www.betclic.fr/football-s1/ligue-des-champions-c8',
                   'pl': 'https://www.betclic.fr/football-s1/angl-premier-league-c3',
                   'l1': 'https://www.betclic.fr/football-s1/ligue-1-uber-eats-c4',
                   'liga': 'https://www.betclic.fr/football-s1/espagne-liga-primera-c7'}

res_betclic = {'ldc': {'cotes': [], 'noms': [], 'dates': []},
               'pl': {'cotes': [], 'noms': [], 'dates': []},
               'l1': {'cotes': [], 'noms': [], 'dates': []},
               'liga': {'cotes': [], 'noms': [], 'dates': []}}

for i, compet in enumerate(compets_betclic):
    browser.get(compets_betclic[compet])
    time.sleep(1)
    if i == 1:
        time.sleep(2)
        button = browser.find_element_by_xpath(
            '//*[@id="popin_tc_privacy_button_2"]')
        button.click()

    cotes_temp = browser.find_elements_by_xpath(
        '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/sports-events-event-markets/sports-markets-default[1]/div/sports-selections-selection/div[1]/span[2]')
    for x in cotes_temp:
        res_betclic[compet]['cotes'].append(x.text)

    nom_temp = browser.find_elements_by_xpath(
        '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/scoreboards-scoreboard/scoreboards-scoreboard-global/div/div/div')
    for x in nom_temp:
        res_betclic[compet]['noms'].append(x.text)

    date_temp = browser.find_elements_by_xpath(
        '/html/body/app-desktop/div[1]/div/bcdk-content-scroller/div/sports-competition/div/sports-events-list/bcdk-vertical-scroller/div/div[2]/div/div/div/div[2]/div/sports-events-event/a/div/sports-events-event-info/div')
    for x in date_temp:
        res_betclic[compet]['dates'].append(x.text)

# ---------------------------------------------------------------
# Winamax
# ---------------------------------------------------------------

compets_winamax = {'ldc': 'https://www.winamax.fr/paris-sportifs/sports/1/800000542/23',
                   'pl': 'https://www.winamax.fr/paris-sportifs/sports/1/1/1',
                   'l1': 'https://www.winamax.fr/paris-sportifs/sports/1/7/4',
                   'liga': 'https://www.winamax.fr/paris-sportifs/sports/1/32/36'}

res_winamax = {'ldc': {'cotes': [], 'noms': [], 'dates': []},
               'pl': {'cotes': [], 'noms': [], 'dates': []},
               'l1': {'cotes': [], 'noms': [], 'dates': []},
               'liga': {'cotes': [], 'noms': [], 'dates': []}}

for i, compet in enumerate(compets_winamax):
    browser.get(compets_winamax[compet])
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
                res_winamax[compet]['cotes'].append(x.text)
    except:
        None

    '''On récupère les noms d'équipes'''
    noms_temp = browser.find_elements_by_xpath(
        '//*[@id="app"]/div/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a/div[2]/div[1]/div[1]/div[1]/div/span')
    for x in noms_temp:
        res_winamax[compet]['noms'].append(x.text)

    '''On récupère les dates des matchs'''

    dates_temp = browser.find_elements_by_xpath(
        '//*[@id="app"]/div/div[1]/div/div[2]/div/section/div[3]/div[1]/div/div/div/div/div[1]/a/div[1]/div[2]/div')
    dates_temp = dates_temp[:-1]

    for x in dates_temp:
        res_winamax[compet]['dates'].append(x.text)

# ---------------------------------------------------------------
# Unibet
# ---------------------------------------------------------------

compets_unibet = {'ldc': 'https://www.unibet.fr/sport/football/ligue-des-champions/ligue-des-champions-matchs',
                  'pl': 'https://www.unibet.fr/sport/football/premier-league/matchs',
                  'l1': 'https://www.unibet.fr/sport/football/ligue-1-ubereats/ligue-1-matchs',
                  'liga': 'https://www.unibet.fr/sport/football/liga/matchs'}

res_unibet = {'ldc': {'cotes': [], 'noms': [], 'dates': []},
              'pl': {'cotes': [], 'noms': [], 'dates': []},
              'l1': {'cotes': [], 'noms': [], 'dates': []},
              'liga': {'cotes': [], 'noms': [], 'dates': []}}

for i, compet in enumerate(compets_unibet):
    browser.get(compets_unibet[compet])
    time.sleep(2)
    '''On cherche les côtes '''
    cotes_temp = browser.find_elements_by_xpath(
        '//*[@id="page__competitionview"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]')
    for match in cotes_temp:
        for i in range(0, 3):
            x = match.get_property('children')[0]
            x = x.get_property('children')[0]
            x = x.get_property('children')[0]
            x = x.get_property('children')[0]
            x = x.get_property('children')[i]
            x = x.get_property('children')[0]
            x = x.get_property('children')[2]
            res_unibet[compet]['cotes'].append(x.text)

    '''On cherche les noms d'équipes'''

    noms_temp = browser.find_elements_by_xpath(
        '//*[@id="page__competitionview"]/div[1]/div/div[2]/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div[1]/div/span')
    for x in noms_temp:
        res_unibet[compet]['noms'].append(x.text.split('-'))
