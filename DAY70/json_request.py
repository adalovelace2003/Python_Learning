import requests
data = {'firstname': 'john'}
r = requests.get("https://api.github.com/events",json=data)
events = r.json()
print(events[0]['id'])



