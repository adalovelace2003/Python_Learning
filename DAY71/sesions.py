import requests

s = requests.Session()

userName = {"username":"John"}
location = {"location":"new york"}

setCookieUrl = "http://httpbin.org/cookies/set"
getCookieUrl = "http://httpbin.org/cookies"

s.get(setCookieUrl,params=userName)
s.get(setCookieUrl,params=location)

r = s.get(getCookieUrl)

print(r.text)

