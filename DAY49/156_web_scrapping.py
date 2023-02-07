import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/')
c = r.content
soup = BeautifulSoup(c,"html.parser")
all = soup.find_all("div",{"class" :"infinite-item"})

for index,item in enumerate(all):
    price = item.find_all("a",{"class":"listing-price"})
    address = item.find_all("div",{"class":"property-address-info"}) 
    area = item.find_all("div",{"class":"property-sqft"}) 
    bed =  item.find_all("div",{"class":"property-beds"}) 
    baths = item.find_all("div",{"class":"property-baths"}) 
    halfBaths = item.find_all("div",{"class":"property-half-baths"}) 
    
    print(f"****({index+1})****")
    try:
        print("Price      : "+   price[0].text.strip())
    except:
        print("Price      : Not Specified")
    try:    
        print("Address    : "+   address[0].text.strip().replace('\n',' ').replace('                           ',' || '))
    except:
        print("Address    : Not Specified")
    try:
        print("Area       : "+   area[0].text.replace(". ",".").replace("\n",""))
    except:
        print("Area       : Not Specified")
    try:
        print("Bed        : "+   bed[0].text.strip())
    except:
        print("Bed        : Not Specified")
    try:
        print("Baths      : "+   baths[0].text.strip())
    except:
        print("Baths      : Not Specified")
    try:
        print("Half Baths : "+   halfBaths[0].text.strip())
    except:
        print("Half Baths : Not Specified ")
    print("\n\n")
