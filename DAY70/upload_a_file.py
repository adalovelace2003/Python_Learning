import requests
url = "https://httpbin.org/post"
files = [('copy1',('USCarBrands.csv',open('USCarBrands.csv','rb'),'csv')),
         ('copy2',('USCarBrands.csv',open('USCarBrands.csv','rb'),'csv')),
        ]
r = requests.post(url,files=files)

























# chatGPT
# import requests

# url = "https://example.com/upload"
# filename = "image.jpg"

# with open(filename, "rb") as file:
#     files = {"file": (filename, file, "image/jpeg")}
#     r = requests.post(url, files=files)
