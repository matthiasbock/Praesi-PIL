#!/usr/bin/python

from PIL import Image, ImageMath

Bild1 = Image.open("beuth-original.png")
Bild2 = Image.open("beuth-verarbeitet.png")

(r1,g1,b1) = Bild1.split()
(r2,g2,b2) = Bild2.split()

r3 = ImageMath.eval("b-a", a=r1, b=r2).convert("P")
out = Image.merge(Bild1.mode, (r3, g1, b1))

out.save("beuth-ergebnis.png")
out.show()
