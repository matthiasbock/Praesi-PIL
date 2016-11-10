#!/usr/bin/python

from PIL import Image, ImageMath

Bild1 = Image.open("Original.png")
Bild2 = Image.open("Schluessel.png")

out = ImageMath.eval("a^b", a=Bild1, b=Bild2)

out.save("Ergebnis.png")
