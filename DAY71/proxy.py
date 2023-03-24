import requests
proxies = {"https": "192.211.101.99"}
r = requests.get("https://httbin.org/ip",proxies=proxies)
print(r.text)