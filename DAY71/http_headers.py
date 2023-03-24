import requests

headers = {'content-type':'multippart/form-data'}
r = requests.post('https://httpbin.org/post',headers = headers)
print(r.headers)