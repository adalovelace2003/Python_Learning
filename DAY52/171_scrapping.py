import requests
from bs4 import BeautifulSoup

base_url = "https://www.scrapethissite.com/pages/forms/"


soup = BeautifulSoup(requests.get(base_url).content, "html.parser")

All = soup.find_all("tr",{ "class":"team"})

team_name = All[0].find_all("td",{"class":"name"})
print(team_name[0].text.strip())


year = All[0].find_all("td",{"class":"year"})
print(year[0].text.strip())

wins = All[0].find_all("td",{"class":"wins"})
print(wins[0].text.strip())

losses = All[0].find_all("td",{"class":"losses"})
print(losses[0].text.strip())

otLosses = All[0].find_all("td",{"class":"ot-losses"})
print(otLosses[0].text.strip())

pct = All[0].find_all("td",{"class":"pct"})
print(pct[0].text.strip())

gf = All[0].find_all("td",{"class":"gf"})
print(gf[0].text.strip())

ga = All[0].find_all("td",{"class":"ga"})
print(ga[0].text.strip())

diff = All[0].find_all("td",{"class":"diff"})
print(diff[0].text.strip())



# print(All[0])
