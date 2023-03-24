import requests

r = requests.get("http://github.com",allow_redirects=True )
# r = requests.get("http://github.com",allow_redirects=False )

print(r.history)
print(r.url)
print(r.status_code)
