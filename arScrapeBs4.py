import numpy
import pandas as pd
import time
import requests
import urllib
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re




data = pd.read_csv("ecad_data.csv")

names = data.loc[0]

ii = 0

prices = {}

for i in names:
    time.sleep(0.1)
    if ii > 0:
        ua = UserAgent()
        query = i + "Austin TX"
        query = query.replace(" ","%20")
        gurl = "https://google.com/search?q=" + query + "apartmentratings.com&num=1"
        result = requests.get(gurl, {"User-Agent": ua.random})
        soup = BeautifulSoup(result.content, "html.parser")
        link = soup.findAll("a")
        linkstr = str(link)
        linkstr = re.findall(r'apartmentratings.com\/tx\/austin\/.+\/\&amp',linkstr)
        linkstr = str(linkstr)
        linkstr = linkstr[2:(len(linkstr)-6)]
        time.sleep(0.5)
        print(linkstr)
        input("press f to pay respects")
    ii+= 1


