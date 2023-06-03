#!/usr/bin/env python3
import requests
import os

url = 'http://localhost/upload/'
directory = 'supplier-data/images'

for root, dirs, files in os.walk(directory):
    for filename in files:
        if '.jpeg' in filename:
          with open (os.path.join(root, filename), 'rb') as opened:
            r = requests.post(url, files={'file':opened})
