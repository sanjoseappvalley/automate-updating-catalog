#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
imgPath = os.path.expanduser("~/supplier-data/images/")
for image in os.listdir(imgPath):
    if '.jpeg' in image:
        with open(imgPath + image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
