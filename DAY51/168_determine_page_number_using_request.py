# determining the no of page 
# only works if the webpage doesn't throw status of 200 if the page no is not available
import requests
import pandas
from bs4 import BeautifulSoup

i = 1
baseUrl = "https://www.century21.com/real-estate/new-york-ny/LCNYNEWYORK/"
r = requests.get(baseUrl)

newUrl = baseUrl +"?p="+ str(i)
while ("200" in str(r) ):
    print(newUrl)
    print(200)
    r = requests.get(newUrl)
    i+=1
    newUrl = baseUrl +"?p="+ str(i)




    

# print(r)