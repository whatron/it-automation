#! /usr/bin/env python3

import locale
import os
import requests

path = "supplier-data/descriptions/"
files = os.listdir(path)
descs = []

for filename in files: # iterates through files to store data in a list of dictionaries
  with open(path + filename) as file:
    name = file.readline().strip()
    weight_str = file.readline().strip().strip(' lbs')
    weight = locale.atof(weight_str)
    description = file.read().strip()
    
    desc = {'name': name, 'weight': weight, 'description': description, 'image_name': os.path.splitext(filename)[0] + '.jpeg'} 
    descs.append(desc)

for d in descs:
  response = requests.post("http://34.31.136.51/fruits/", json=d) # posts to address
  response.raise_for_status()
