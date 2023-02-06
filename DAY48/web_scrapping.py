import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.scrapethissite.com/pages/simple/")
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("h3", {"class" : "country-name"})

for index, item in enumerate(all):
    print(f"{index}.  {item.text.strip()}")
    
    
