#! /usr/bin/env python3

import os
import requests

path = "/data/feedback"
files = os.listdir(path)
reviews = []

for file_path in files: # iterates through files to store data in a list of dictionaries
  with open(path + '/' + file_path) as file:
    title = file.readline().strip()
    name = file.readline().strip()
    date = file.readline().strip()
    feedback = file.read().strip()

    review = {'title': title, 'name': name, 'date': date, 'feedback': feedback} 
    reviews.append(review)

for r in reviews: # post each list entry
  response = requests.post("http://<address>/feedback/", json=r) # posts to address
  response.raise_for_status()
