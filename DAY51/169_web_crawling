import requests
import pandas
from bs4 import BeautifulSoup
base_url = "https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/"
soup = BeautifulSoup(requests.get(base_url).content, "html.parser")
All = soup.find_all("div", {"class": "infinite-item"})

for i in range(2, 8):
    new_url = base_url + "?p=" + str(i)
    soup = BeautifulSoup(requests.get(new_url).content, "html.parser")
    All += soup.find_all("div", {"class": "infinite-item"})
l = []
d = {}
for index, item in enumerate(All[:-1]):
    price = item.find_all("a", {"class": "listing-price"})
    address = item.find_all("div", {"class": "property-address-info"})
    area = item.find_all("div", {"class": "property-sqft"})
    bed = item.find_all("div", {"class": "property-beds"})
    baths = item.find_all("div", {"class": "property-baths"})
    halfBaths = item.find_all("div", {"class": "property-half-baths"})
    d["price"] = price[0].text.strip() if price else "N/A"
    d["address"] = address[0].text.strip().replace("\n", " ").replace(
        "                           ", " , ") if address else "N/A"
    d["area"] = area[0].text.strip().replace(
        ". ", ".").replace("\n", "") if area else "N/A"
    d["bed"] = bed[0].text.strip() if bed else "N/A"
    d["baths"] = baths[0].text.strip() if baths else "N/A"
    d["halfBaths"] = halfBaths[0].text.strip() if halfBaths else "N/A"
    l.append(d)
df = pandas.DataFrame(l)
df.to_csv("Output.csv")



