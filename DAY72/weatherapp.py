import requests
import json

city = input("Enter the name of city : ");
url = f"https://api.weatherapi.com/v1/current.json?key=b1c64480403232603&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)

for key, value in wdic.items():
    print(key + ':')
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            print('\t' + sub_key + ':', sub_value)
    else:
        print('\t' + value)


