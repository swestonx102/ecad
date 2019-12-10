It doesn't seem like there are really many reliable sites to get *all* the data from.

I think that apartmentratings.com is the best place to start.

Okay, so.

Searching in the search box for just the name of the place on ApartmentRatings will work if after that, 
we run a ctrl+f (however one might do that with selenium) for the address (or maybe just for Austin)

pseudocode:

import numpy (dependency for pandas)
import pandas (to interpret the .csv)

searchData = pandas code to import csv

names = searchData(row0)
addresses = searchData(row9)
zips = searchData(row10)
prices = {}
searchURL = "http://apartmentlistings.fcom/searchresults/?query=" + names(i).replace(" ","-")

selenium.findonpage(searchURL,zips(i))

(download JSON)

tprice = (filter through for price)

if len.(tprice) > 0
	prices(i) = tprice
else
	prices(i) = notFoundOnApartmentRatings
