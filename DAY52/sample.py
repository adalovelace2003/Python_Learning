import requests
from bs4 import BeautifulSoup

i = 0
base_url = "https://www.booking.com/searchresults.html?label=gen173rf-1FCAEoggI46AdIM1gDaKsBiAEBmAExuAEZyAEM2AEB6AEB-AECiAIBogINcHJvamVjdHByby5pb6gCA7gCy9SUnwbAAgHSAiRjYmI2NTRmNS1mYzMzLTRhNzgtYjFhNy0xMmE4NTE4MWE2YjDYAgXgAgE&aid=304142&dest_id=-1022136&dest_type=city&group_adults=null&req_adults=null&no_rooms=null&group_children=null&req_children=null&offset="
url = base_url + str(i*35)
soup = BeautifulSoup(requests.get(url).content,"html.parser")
# all = soup.find_all("div",{"class":"a826ba81c4"})

with open("sample.html","w") as file:
    file.write(str(soup))


# name = all[0].find_all("div", {"class": "fcab3ed991"})
# print(name[0].text)

# d["name"] = name[0].text.strip() if price else "N/A"





# print(len(all))
# for i in range(1,16):
    # url = base_url + str(i*35)
    # soup = BeautifulSoup(requests.get(url).content,"html.parser")
    # all += soup.find_all("div",{"class":"a826ba81c4"})
    # print(len(all))




