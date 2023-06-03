#!/usr/bin/env python3

import sys
import os
import datetime
import reports
import emails

def process(path):
  files = os.listdir(path)
  descs = []

  for filename in files: # iterates through files to store data in a list of dictionaries
    with open(path + filename) as file:
      name = file.readline().strip()
      weight = file.readline().strip()
      descs.append('name: ' + name)
      descs.append("<br/>")
      descs.append('weight: ' + weight)
      descs.append("<br/><br/>")
  return descs

def main(argv):
  path = "supplier-data/descriptions/"
  descs = process(path)
  descs.pop()
  reports.generate_report('/tmp/processed.pdf', 'Processed Update on June 3, 2023', ('').join(descs))
  message = emails.generate("automation@example.com", "<usrname>@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "/tmp/processed.pdf")
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)
