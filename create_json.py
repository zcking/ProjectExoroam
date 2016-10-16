"""
File: create_json.py
Author: Zachary King

Description: takes the exodata module and creates 
a json file with the necessary data and hierarchy 
for the planetary map.

If you are wondering how the json file should be 
formatted to work with the D3 example I am 
using, refer to the `flare.json` file (from their example).
"""

import json

import exodata

# Load the open exoplanet catalog data
exocat = exodata.load_db_from_url()


# Create the starter container, which will be outputted to json later
data = {"name": "universe", "children": []}

# Add each system to the container
for i, system in enumerate(exocat.systems[:99] + [exocat.systemDict['Sun']]):
    data["children"].append({"name": system.name, "children": [], "size": 50})
    # The catalog names our system 'Sun' which is weird, 
    # so rename it in the container
    if system.name == 'Sun':
        data["children"][i]["name"] = "Our Solar System"
    
    # And then add each planet for that corresponding system
    for planet in [p for p in exocat.planets if p.system.name == system.name]:
        try:
            s = planet.R.item() % 21
        except:
            s = 20
        planet_data = {"name": planet.name, "size": s}
        data["children"][i]["children"].append(planet_data)


# Now write the json data to the file, which the site will use
json_str = json.dumps(data)
with open('universe.json', 'w') as f:
    f.write(json_str)
