#! /usr/bin/env python3

import os
import requests

path = 'supplier-data/descriptions/'
for file in os.listdir(path):
  datalist = []
  with open(path + file) as f:
    for line in f:
      datalist.append(line.strip())
  datalist[1] = datalist[1].split(' ')[0]

  image_name = ""
  if datalist[0] == "Lemon":
    image_name = "006.jpeg"
  elif datalist[0] == "Grape":
    image_name = "004.jpeg"
  if datalist[0] == "Kiwifruit":
    image_name = "005.jpeg"
  elif datalist[0] == "Avocado":
    image_name = "002.jpeg"
  if datalist[0] == "Apple":
    image_name = "001.jpeg"
  elif datalist[0] == "Strawberry":
    image_name = "009.jpeg"
  if datalist[0] == "Plum":
    image_name = "008.jpeg"
  elif datalist[0] == "Mango":
    image_name = "007.jpeg"
  elif datalist[0] == "Blackberry":
    image_name = "003.jpeg"
  elif datalist[0] == "Watermelon":
    image_name = "010.jpeg"
  p = {'name': datalist[0], 'weight': int(datalist[1]), 'description': datalist[2], "image_name": image_name}

  r = requests.post("http://35.188.182.214/fruits/", data=p)
  r.raise_for_status()
