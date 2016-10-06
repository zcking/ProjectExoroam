"""
File: helpers.py
Author: Zachary King
Copyright (c) 2016

Description: defines several helper functions for accessing data 
within the Open Exoplanet Catalog.
"""

import exodata
import exodata.astroquantities as aq
from exodata.equations import KeplersThirdLaw

# Load the most current database
# In the future, change this to try/except
# and implement offline cache usage
exocat = exodata.load_db_from_url()


def getSurfaceGravity(planet_name):
    planet = exocat.planetDict[planet_name]
    return planet.calcSurfaceGravity().item()