import requests
from crud_functions import *

# This script should only be used about once in every 5 minutes, because raw github content gets cached for 5 minutes

# Initialize data
r = requests.get('https://raw.githubusercontent.com/silvan12/silvan.tech/master/Projects/current_projects.json')
data = json.loads(r.text)

# Choice
choice = input("Update or Delete? (Please answer with u or d)\n>")

# Update
if choice == "u":
    Update(data)

# Delete
if choice == "d":
    Delete(data)

# Dumbass
else:
    print("Please enter only u or d")
