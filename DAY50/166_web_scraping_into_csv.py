import requests
import pandas
from bs4 import BeautifulSoup

r = requests.get('https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/')
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class": "infinite-item"})
l=[]

for index, item in enumerate(all):
    if index == len(all) - 1:   # this will not print the last one
        continue
    d = {}

    price = item.find_all("a", {"class": "listing-price"})
    address = item.find_all("div", {"class": "property-address-info"})
    area = item.find_all("div", {"class": "property-sqft"})
    bed = item.find_all("div", {"class": "property-beds"})
    baths = item.find_all("div", {"class": "property-baths"})
    halfBaths = item.find_all("div", {"class": "property-half-baths"})

    d["price"] = price[0].text.strip() if price else "N/A"
    d["address"] = address[0].text.strip().replace("\n"," ").replace("                           "," , ") if address else "N/A"
    d["area"] = area[0].text.strip().replace(". ", ".").replace("\n", "") if area else "N/A"
    d["bed"] = bed[0].text.strip() if bed else "N/A"
    d["baths"] = baths[0].text.strip() if baths else "N/A"
    d["halfBaths"] = halfBaths[0].text.strip() if halfBaths else "N/A"
    
    l.append(d)

df = pandas.DataFrame(l)
df.to_csv("Output.csv")

