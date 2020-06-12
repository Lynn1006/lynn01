import board
import neopixel
import time
from adafruit_circuitplayground.express import cpx
import adafruit_fancyled.adafruit_fancyled as fancy
from digitalio import DigitalInOut, Direction, Pull

# delare variables and settings
strip = neopixel.NeoPixel(board.D1, 10, auto_write=False)
ledMode = 0

button = DigitalInOut(board.A1)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
buttonPre = False
buttonPressTime = 0

cpx.pixels.auto_write = False  # Update only when we say
cpx.pixels.fill((0, 0, 0))  # Turn off the NeoPixels if they're on!
cpx.pixels.brightness = 0.1   # make less blinding

palette = [fancy.CRGB(251, 126, 253),  # pink
           fancy.CRGB(184, 22, 180),    # purple
           fancy.CRGB(227, 37, 107),      # violet red
           fancy.CRGB(0, 0, 0)]          # Black

offset = 0  # Position offset into palette to make it "spin"


while True:
    if button.value != buttonPre:
        buttonPre = button.value
        if button.value:
            buttonPressTime = time.monotonic()
        else:
            if time.monotonic() >= buttonPressTime + 1:
                ledMode = 0
            ledMode += 1
            if ledMode > 2:
                ledMode = 0

    if ledMode == 1:
        for i in range(10):
            color = fancy.palette_lookup(palette, offset + i / 9)
            cpx.pixels[i] = color.pack()
        cpx.pixels.show()
        offset += 0.033  # Bigger number = faster spin
    # turn off the neopixels when button release

    else:
        cpx.pixels.fill((0, 0, 0))
        cpx.pixels.show()