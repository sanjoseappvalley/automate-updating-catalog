#!/usr/bin/env python3
import os
from PIL import Image

samePath = "supplier-data/images/"
for image in os.listdir(samePath):
    """Some images are not image files, need to check for .tiff files"""
    if '.tiff' in image:
        img = Image.open(samePath + image)
        img.resize((600, 400)).convert("RGB").save(samePath + image.split('.')[0] + '.jpeg', "JPEG")
        img.close()
