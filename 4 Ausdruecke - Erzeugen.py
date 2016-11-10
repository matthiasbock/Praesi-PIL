#!/usr/bin/python

from PIL import Image, ImageMath

Bild1 = Image.open("beuth-original.png")
Bild2 = Image.open("steganographie.png")

# kleinstmoegliche Aenderung
pixel = Bild2.load()
for y in range(Bild2.size[1]):
    for x in range(Bild2.size[0]):
        if pixel[x,y][0] == 0:
            pixel[x,y] = (1,0,0)
        else:
            pixel[x,y] = (0,0,0)

# Layer auftrennen
(r1,g1,b1) = Bild1.split()
(r2,g2,b2) = Bild2.split()

# auf den R-Layer Addition anwenden
r3 = ImageMath.eval("a+b", a=r1, b=r2).convert("P")

# Layer wieder zusammenfuehren
out = Image.merge(Bild1.mode, (r3, g1, b1))

out.save("beuth-verarbeitet.png")
out.show()
