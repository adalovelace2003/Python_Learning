import requests
payload = {"firstname":"John","lastName":"Smith"}
r_get = requests.get("https://httpbin.org/get",params=payload)
r_post = requests.post("https://httpbin.org/get",data=payload)
print(r_post.text)




