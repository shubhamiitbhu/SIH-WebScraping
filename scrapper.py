import requests
from bs4 import BeautifulSoup
import pandas
import csv
import re


def scraping(url_end):

    agent = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    base_url = "https://etrain.info/in?STATION=" + url_end



    response = requests.get(base_url, headers=agent)
    soup = BeautifulSoup(response.content, "html.parser")



    arr_eve = soup.find_all("tr", {"class": "even"})
    arr_odd = soup.find_all("tr", {"class": "odd"})
    days = soup.find_all("td", {"class": "wd18 bgrn"})

    results = {}
    
    for key in arr_eve:
        days = key.find_all('td')[7:14]
        day = []
        for i in days:
            if i.text=="X":
                day.append(False)
            elif i.text=="Y":
                day.append(True)
            else:
                day.append("Error")
        results[key.a.text] = day

    for key in arr_odd:
        days = key.find_all('td')[7:14]
        day = []
        for i in days:
            if i.text=="X":
                day.append(False)
            elif i.text=="Y":
                day.append(True)
            else:
                day.append("Error")
        results[key.a.text] = day

    return results
    
    


    