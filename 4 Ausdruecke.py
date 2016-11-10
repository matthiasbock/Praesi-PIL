#!/usr/bin/python

from PIL import Image, ImageMath

# beide Bilder laden
Bild1 = Image.open("beuth-original.png")
Bild2 = Image.open("beuth-verarbeitet.png")

# Bild in einen Layer pro Farbkanal zerlegen
(r1,g1,b1) = Bild1.split()
(r2,g2,b2) = Bild2.split()

# Bilder voneinander abziehen
secret = ImageMath.eval("(b-a)*255", a=r1, b=r2).convert("P")

secret.show()
