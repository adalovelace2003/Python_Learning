import requests
from bs4 import BeautifulSoup


r = requests.get("https://www.scrapethissite.com/pages/simple/")
c = r.content
soup = BeautifulSoup(c, "html.parser")

# [0] #  #[0] is indexing , you can also remove this
all = soup.find_all("h3", {"class" : "country-name"})
# print(all.find_all("i")) # going more deeper

        #My Approach                # # print(all[1].text.strip())
        #My Approach                
        #My Approach                # j = 0
        #My Approach                
        #My Approach                # for item in all:
        #My Approach                #     print(all[j].text.strip())
        #My Approach                #     j += 1
        
        #My Approach2 
        
# for item in all:
    # print(item.text.strip())
    
for index, item in enumerate(all):
    print(f"{index}.  {item.text.strip()}")


#Creator Approach

# he is using the different site for scrapping so, the approach to scrapping 
# is a bit different.

# print(all[0].text)

# for item in all:
    # print(item.find_all("h3")[0].text)


# Note: You cannot directly grab the text from the all the elements at once
# like from the all, where 100's of data is present , print(all)
# you have to iterate through each and extract , print(all[0])
# print(soup.find_all("h3",{"class":"country-name"}).text)

# print(all.text.strip()) # here strip removes before and after spaces
