import requests
from bs4 import BeautifulSoup
import pandas
import csv
import re
import scrapper
import xlwt 
from xlwt import Workbook 
import json


def getJson(filepath):
    with open (filepath, 'r') as fp:
        return json.load(fp)

wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1') 
data = getJson('./stationCodetoName.json')
data_len = len(data)
dataframe = []
len=0
for key in data:
    results = {}
    print("Scraping for " + key + " " + str(data_len-len) + " to go")
    train_details = scrapper.scraping(key)
    results[key]=train_details
    sheet1.write(len, 0, key)
    row_len=1
    for i in train_details:
        if row_len%250 == 0:
            len = len+1
            sheet1.write(len,0,key)
            row_len=1

        sheet1.write(len, row_len, str({i :train_details[i]}))
        row_len += 1

    len=len+1
    wb.save('results.xls') 
  
