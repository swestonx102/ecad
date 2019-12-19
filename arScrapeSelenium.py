from selenium import webdriver
import numpy
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.parse import urlencode, urlparse, parse_qs
import webbrowser

dr = webdriver.Firefox()

data = pd.read_csv("ecad_data.csv")

names = data.loc[0]

ii = 0

dr.get("http://google.com")

prices = {}

for i in names:
    time.sleep(0.1)
    tn = i
    if ii > 0:
        dr.find_element_by_name("q").send_keys(tn + " Austin TX")
        time.sleep(0.5)
        dr.find_element_by_name("btnI").click()
        time.sleep(0.5)
        dr.close()
        input("press f to pay respects: ")
    ii += 1



