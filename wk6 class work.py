import board
import neopixel
import time
import rotaryio
from adafruit_circuitplayground.express import cpx
from digitalio import DigitalInOut, Direction, Pull

# delare variables and settings
strip = neopixel.NeoPixel(board.D1, 10, auto_write=False)
ledMode = 0

button = DigitalInOut(board.A3)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
buttonPre = False
buttonPressTime = 0
click = False

knob = rotaryio.IncrementalEncoder(board.A1, board.A2)
POSMIN = 0

POSMAX = 255

cpx.pixels.auto_write = False  # Update only when we say
cpx.pixels.fill((0, 0, 0))  # Turn off the NeoPixels if they're on!

count = knob.position



WHITE = (int(count), int(count), int(count))
RED = (int(count), 0, 0)
BLUE = (0, 0, int(count))

while True:
    cpx.pixels.brightness = 0.5

    count = knob.position


    if count < POSMIN:

        count = POSMIN

    elif count > POSMAX:

        count = POSMAX

        knob.position = count

    print(count)

    if button.value != buttonPre:
        buttonPre = button.value
        if button.value:
            buttonPressTime = time.monotonic()
            click = True
        else:
            if time.monotonic() >= buttonPressTime + 1:
                ledMode = 0
            ledMode += 1
            if ledMode > 4:
                ledMode = 0
            if ledMode == 1:
                count = 10


    if ledMode == 1:
        knob.position = count
        WHITE = (int(count), int(count), int(count))
        cpx.pixels.fill(WHITE)
        cpx.pixels.show()

    elif ledMode == 2:
        RED = (int(count), 0, 0)
        cpx.pixels.fill(RED)
        cpx.pixels.show()

    elif ledMode == 3:
        BLUE = (0, 0, int(count))
        cpx.pixels.fill(BLUE)
        cpx.pixels.show()

    else:
        cpx.pixels.fill((0, 0, 0))
        cpx.pixels.show()