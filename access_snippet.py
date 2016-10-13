"""
File: access_snippet.py

An example from the Open Exoplanet Catalogue repo 
on accessing the catalogue. 
"""

import xml.etree.ElementTree as ET, urllib.request, gzip, io, sys

def main():
    url = 'http://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz'
    oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))

    # Output mass and radius of all planets
    for planet in oec.findall('.//planet'):
        print([planet.findtext('mass'), planet.findtext('radius')])

    print('-' * 40)

    # Find all circumbinary planets
    for planet in oec.findall('.//binary/planet'):
        print(planet.findtext('name'))

    print('-' * 40)

    # Output distance to planetary system (in pc, if known) and number of planets in system
    for system in oec.findall('.//system'):
        print(system.findtext('name'), system.findtext('distance'), len(system.findall('.//planet')))


if __name__ == '__main__':
    main()
