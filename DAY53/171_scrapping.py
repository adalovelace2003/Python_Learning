import requests
from bs4 import BeautifulSoup
import pandas

base_url = "https://www.scrapethissite.com/pages/forms/"
soup = BeautifulSoup(requests.get(base_url).content, "html.parser")
All = soup.find_all("tr", {"class": "team"})

for i in range(1,25):
    url = base_url + "?page_num="+ str(i)
    soup = BeautifulSoup(requests.get(base_url).content, "html.parser")
    All += soup.find_all("tr", {"class": "team"})
    
l = []
for index, item in enumerate(All[:-1]):
    d = {}
    team_name = All[index].find_all("td", {"class": "name"})
    year = All[index].find_all("td", {"class": "year"})
    wins = All[index].find_all("td", {"class": "wins"})
    losses = All[index].find_all("td", {"class": "losses"})
    otLosses = All[index].find_all("td", {"class": "otXlosses"})
    pct = All[index].find_all("td", {"class": "pct"})
    gf = All[index].find_all("td", {"class": "gf"})
    ga = All[index].find_all("td", {"class": "ga"})
    diff = All[index].find_all("td", {"class": "diff"})

    d["team_name"] = team_name[0].text.strip() if team_name else "N/A"
    d["year"] = year[0].text.strip() if year else "N/A"
    d["wins"] = wins[0].text.strip() if wins else "N/A"
    d["losses"] = losses[0].text.strip() if losses else "N/A"
    d["otLosses"] = otLosses[0].text.strip() if otLosses else "N/A"
    d["pct"] = pct[0].text.strip() if pct else "N/A"
    d["gf"] = gf[0].text.strip() if gf else "N/A"
    d["ga"] = ga[0].text.strip() if ga else "N/A"
    d["diff"] = diff[0].text.strip() if diff else "N/A"

    l.append(d)

df = pandas.DataFrame(l)
df.to_csv("DAY53/Output.csv")

