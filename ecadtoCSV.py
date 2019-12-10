import numpy as np
import pandas as pd

def fbtw (s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def finder(searchString):
    with open('ecad2013.txt') as ecad:
        data = {}
        ii = 0
        for i, line in enumerate(ecad):
            tdata = fbtw(line, searchString,",")
            if len(tdata) > 0:
                data[ii] = tdata
                ii+= 1
    return data

cndata = finder("community_name: ")
addata = finder("audit_date: ")
wsdata = finder("window_screens: ")
ybdata = finder("year_built: ")
udata = finder("utilities: ")
tudata = finder("total_units: ")
cedata = finder("community_eui_kwh_sqft_yr: ")
ladata = finder("latitude: ")
lodata = finder("longitude: ")

dataStored = pd.DataFrame([cndata,addata,wsdata,ybdata,udata,tudata,cedata,ladata,lodata])
dataStored.transpose()
dataStored.to_csv("ecad_data.csv")

