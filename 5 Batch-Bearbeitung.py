#!/usr/bin/python
#
# Alle Bilder im uebergebenen Ordner bearbeiten 
#

import sys, os
from PIL import Image, ImageEnhance

if len(sys.argv) < 2:
    print "Dieses Skript muss man so aufrufen: skript.py <Ordner/>"
    exit()

# unveraenderliche Parameter
new_size = (1280,1024)
sharpness = 2.0
brightness = 0.5
contrast = 2.0

# finde und bearbeite alle PNGs im uebergebenen Ordner
files = os.listdir( sys.argv[1] )
for f in files:
    if f[-4:] == '.png':
        print "Verarbeite "+f+" ..."

        # Oeffnen
        img = Image.open(f)

        # Skalieren
        img.resize( new_size )
    
        # Bild editieren
        img = ImageEnhance.Sharpness(img).enhance( sharpness )
        img = ImageEnhance.Brightness(img).enhance( brightness )
        img = ImageEnhance.Contrast(img).enhance( contrast )
    
        # unter neuem Namen speichern
        img.save(f[:-4]+"-enhanced.jpg")
