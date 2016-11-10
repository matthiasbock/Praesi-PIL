#!/usr/bin/python

from PIL import Image, ImageFilter

# Parameter
shift_right = -20
shift_down = -20
blur_iterations = 20

# RGBA
transparent = (255,255,255,0)
white = (255,255,255,255)
black = (0,0,0,255)
grey = (30,30,30,255)

# aus Datei laden
tux = Image.open("tux.png")

# Schatten erzeugen
tux_mask = tux.copy() 

# S/W-Maske erzeugen
pixel = tux_mask.load()
for y in range(tux_mask.size[1]):
    for x in range(tux_mask.size[0]):
        if pixel[x,y][3] > 0:
            pixel[x,y] = grey
        else:
            pixel[x,y] = transparent

# Schatten weichzeichnen
shadow = tux_mask.copy()
for iteration in range(blur_iterations):
    shadow = shadow.filter(ImageFilter.BLUR)

# Zusammenfuegen
shadow.paste(tux, (shift_right,shift_down), tux_mask)

shadow.save("tux+shadow.png")
