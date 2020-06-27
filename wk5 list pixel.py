import board
import time
import neopixel

pixels = neopixel.Neopixel(board.NEOPIXEL, 10, auto_write=False, brightness=0.05)

colors = [(0, 255, 0), (25, 255, 0),
        (50, 255, 0), (75, 255, 0),
        (100, 255, 0), (125, 255, 0),
        (150, 255, 0), (175, 255, 0),
        (200, 255, 0), (225, 255, 0)


while True:
    popColour = colors.pop(0)
    colors.append(popColour)

    for x xin range(len(pixels)):
        pixels[x] = colors[x]

    pixels.show()

    time.sleep(0.1)