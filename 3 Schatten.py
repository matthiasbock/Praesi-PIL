#!/usr/bin/python

from PIL import Image, ImageFilter

# ein paar Operationsvariablen
shift_right = -20
shift_down = -20
blur_iterations = 20

# unsere RGBA-Konstanten
transparent = (255,255,255,0)
white = (255,255,255,255)
black = (0,0,0,255)
grey = (30,30,30,255)

# Bild aus Datei laden
tux = Image.open("tux.png")

# neues Bild fuer den Schatten erzeugen
grey_tux = tux.copy()

# Bild in Graustufen-Abbild konvertieren
pixel = grey_tux.load()
for y in range(grey_tux.size[1]):
    for x in range(grey_tux.size[0]):
        if pixel[x,y][3] > 0:
            pixel[x,y] = grey
        else:
            pixel[x,y] = transparent

# den Schatten mehrmals weichzeichnen
shadow = grey_tux.copy()
for iteration in range(blur_iterations):
    shadow = shadow.filter(ImageFilter.BLUR)

# Zusammenfuegen
shadow.paste(tux, (shift_right,shift_down), grey_tux)

shadow.save("tux+shadow.png")
