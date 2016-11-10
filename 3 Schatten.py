#!/usr/bin/python

from PIL import Image, ImageFilter

# Parameter
shift_left = 10
shift_up = 10 
blur_iterations = 20

# RGBA
transparent = (255,255,255,0)
white = (255,255,255,255)
black = (0,0,0,255)
grey = (30,30,30,255)

# aus Datei laden
tux = Image.open("tux.png")

# Schatten erzeugen
shadow = tux.copy() 

# in S/W verwandeln
pixels = shadow.load()
for y in range(shadow.size[1]):
    for x in range(shadow.size[0]):
        if pixels[x,y][3] > 0:
            pixels[x,y] = grey
        else:
            pixels[x,y] = transparent

# Weichzeichnen
for iteration in range(blur_iterations):
    shadow = shadow.filter(ImageFilter.BLUR)

# Zusammenfuegen
shadow.paste(tux, (), )

shadow.save("tux+shadow.png")
shadow.show()
