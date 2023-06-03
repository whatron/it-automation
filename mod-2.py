#! /usr/bin/env python3

import os
import requests

path = "/data/feedback"
files = os.listdir(path)
reviews = []

for file_path in files:
  with open(path + '/' + file_path) as file:
    title = file.readline().strip()
    name = file.readline().strip()
    date = file.readline().strip()
    feedback = file.read().strip()

    review = {'title': title, 'name': name, 'date': date, 'feedback': feedback} 
    reviews.append(review)

for r in reviews:
  response = requests.post("http://34.30.245.53/feedback/", json=r)
  response.raise_for_status()
