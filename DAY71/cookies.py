import requests

url = "https://httpbin.org/post"
cookie = {"location":"new york"}

r = requests.post(url,cookies = cookie)
print(r.text)

r2 = requests.get("https://google.com")
print(r2.cookies)
