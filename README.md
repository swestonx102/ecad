This folder contains the following files: 

ecad2013raw.txt, the "raw" JSON code from austindata.org. It differs 
from the JSON code in that I have removed all of the double quotations. JSON 
is not actually used for this project.

ecad2013.txt, a version of ecad2013raw.txt which has had all of the 
unnecessary lines removed with vim. Done to make the python code more 
efficient.

ecadtoCSV.py, python script that turns the data in ecad2013 into a .csv

ecadtoCSVwComments.py, commented version of script

ecad_data.csv, the spreadsheet generated

ecadData.m, a Matlab script that interprets the data. Not a point of focus,
I just wanted to mess around with the data in Matlab. It would be better to
do so in Pandas.




