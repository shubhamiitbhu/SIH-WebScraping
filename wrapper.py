import requests
from bs4 import BeautifulSoup
import pandas
import csv
import re
import scrapper
import json

def getJson(filepath):
    with open (filepath, 'r') as fp:
        return json.load(fp)

data = getJson('./stationCodetoName.json')
data_len = len(data)
results = {}
dataframe = []
len=0
for key in data:
    print("Scraping for " + key + " " + str(data_len-len) + " to go")
    train_details = scrapper.scraping("AADR")
    results[key]=train_details
    len=len+1
    
    

dataframe.append(results)
df = pandas.DataFrame(dataframe)
df.to_json("train_schedule.json")