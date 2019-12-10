import numpy as np
import pandas as pd
import re
import time
def fbtw (s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def finder(searchString,endString):
    with open('ecad2013.txt') as ecad:
        data = {}
        ii = 0
        for i, line in enumerate(ecad):
            tdata = fbtw(line, searchString,endString)
            if len(tdata) > 0:
                data[ii] = tdata
                ii+= 1
    return data

def zipfinder():
    with open('ecad2013.txt') as ecad:
        data = {}
        ii = 0
        for i, line in enumerate(ecad):
            if 'human_address' in line:
                tdata = re.findall('\*\d{5}\*', line)
                tdata = tdata[0]
                tdata = tdata.replace("*","")
                data[ii] = tdata
                ii+= 1
    return data

cndata = finder("community_name: ",",")
addata = finder("audit_date: ",",")
wsdata = finder("window_screens: ",",")
ybdata = finder("year_built: ",",")
udata = finder("utilities: ",",")
tudata = finder("total_units: ",",")
cedata = finder("community_eui_kwh_sqft_yr: ",",")
ladata = finder("latitude: ",",")
lodata = finder("longitude: ",",")
sadata = finder("human_address:*address*: *","*, ")
zidata = zipfinder()
dataStored = pd.DataFrame([cndata,addata,wsdata,ybdata,udata,tudata,cedata,ladata,lodata,sadata,zidata])
dataStored.transpose()
dataStored.to_csv("ecad_data.csv")


