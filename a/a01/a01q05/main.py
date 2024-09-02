# File: main.py
# Directory: ciss450/a/a01/a01q05
# Author: Carl Dalebout

import requests

target = input()

s = requests.get(target).text
print(s)
 