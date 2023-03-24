import requests
 
r= requests.get("https://httpbin.org/status/404",timeout=0.1)

r.raise_for_status()

