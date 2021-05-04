import requests
import json
from PIL import Image

url = 'http://127.0.0.1:8000/photos/'
JSON_FORMAT = '[]'

response = requests.get(url)
response_json = response.json()

names = map(lambda obj: obj.name, data)
imagesUrl = map(lambda obj: obj.image, data)
images = map(lambda url: Image.open(requests.get(url, stream=True).raw), imagesUrl)

print(names)
print(imagesUrl)
print(images)