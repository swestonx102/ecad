#importing libraries that the script needs, and a few that it doesnt

import numpy as np #numerical analysis/arrays. required for pandas
import pandas as pd #data analysis, used to create arrays and export spreadsheets
import urllib.request #unused so far, opens URLs
import bs4 #unused so far, webscraping library
from selenium import webdriver #unused so far, webscraping library
from selenium.webdriver.common.keys import Keys #unused
import time #literally a clock, used to pause the script so it doesn't overload the server of the site i am pulling data from or get my IP blocked for DDoS

def fbtw (s, first, last ): #a function, "find between". Finds text between two strings, called first and last
    try: #try is used because there will be empty lines. Without try, the code would crash if it got to an empty line.
        start = s.index( first ) + len( first ) #s.index( first ) finds the position of the string "first" in the line, s. It then adds the length of that string to give the point where we will start looking "between".
        end = s.index( last, start ) #searches for string "last" starting from the end of string "first" so as to not accidentally find string "last" inside string "first"
        return s[start:end] #returns the value between first and last
    except ValueError:
        return "" #returns nothing if the line has no text

def finder(searchString): #function that implements fbtw to search through every line of a text file
    with open('ecad2013.txt') as ecad: #creates a variable ecad that uses the in-built python method "open". The variable is the text file in a form that python can intrrpret line-by-line.
        data = {} #creates an empty array to put the data in
        ii = 0 #an iterator that will go up every time a value is found
        for i, line in enumerate(ecad): # "for every line in text file"
            tdata = fbtw(line, searchString,",") #using fbtw
            if len(tdata) > 0: #only adds the value to the array if it isn't empty
                data[ii] = tdata
                ii+= 1
    return data #returns the array


#calling the finder() function for various values:
cndata = finder("community_name: ") 
addata = finder("audit_date: ")
wsdata = finder("window_screens: ")
ybdata = finder("year_built: ")
udata = finder("utilities: ")
tudata = finder("total_units: ")
cedata = finder("community_eui_kwh_sqft_yr: ")
ladata = finder("latitude: ")
lodata = finder("longitude: ")

#creating a 2D array of the data
dataStored = pd.DataFrame([cndata,addata,wsdata,ybdata,udata,tudata,cedata,ladata,lodata])
dataStored.transpose() #flipping columns vs rows
dataStored.to_csv("ecad_data.csv") #exporting spreadsheet

dr = webdriver.Firefox() #creates instance of selenium webdriver

for i in cndata: #for all the community names:
    #create the URL of a search for the community name on craigslist:
    urlString = "https://austin.craigslist.org/search/apa?query=" + cndata[i].replace    (" ","+") +  "&availabilityMode=0&sale_date=all+dates"
    time.sleep(1) #wait 1 second
    dr.get(urlString) #open the webpage
    #
    # in here is where the actual 
    # finding of data will occur
    #
    dr.close() #close the webpage
