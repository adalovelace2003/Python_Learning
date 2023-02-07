import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/')
c = r.content
soup = BeautifulSoup(c,"html.parser")
all = soup.find_all("div",{"class" :"infinite-item"})

for index,item in enumerate(all[-1]):
    price = item.find_all("a",{"class":"listing-price"})
    address = item.find_all("div",{"class":"property-address-info"}) 
    area = item.find_all("div",{"class":"property-sqft"}) 
    bed =  item.find_all("div",{"class":"property-beds"}) 
    baths = item.find_all("div",{"class":"property-baths"}) 
    halfBaths = item.find_all("div",{"class":"property-half-baths"}) 
    
    print(f"****({index+1})****")
    
    print("Price      : " + (price[0].text.strip() if price else "Not Specified "))
    print("Address    : " + (address[0].text.strip().replace('\n',' ').replace('                           ',' || ') if address else "Not Specified "))
    print("Area       : " + (area[0].text.strip().replace(". ",".").replace("\n","") if area else "Not Specified "))
    print("Bed        : " + (bed[0].text.strip() if bed else "Not Specified "))
    print("Baths      : " + (baths[0].text.strip() if baths else "Not Specified "))
    print("Half_Baths : " + (halfBaths[0].text.strip() if halfBaths  else "Not Specified " ) + "\n\n")