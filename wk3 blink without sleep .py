import board
from digitalio import DigitalInOut, Direction, Pull
import time

led = DigitalInOut(board.A7)
led.direction = Direction.OUTPUT
ledMode = 0

button = DigitalInOut(board.A1)
button.direction = Direction.INPUT
button.pull = Pull.DOWN
buttonPre = False
buttonPressTime = 0

blinkInterval = 0.5

blinkTime = time.monotonic() + blinkInterval

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
        blinkInterval = 0.5
        if time.monotonic() >= blinkTime:
            led.value = not led.value
            blinkTime += blinkInterval

    else:
        led.value = False
        blinkTime = time.monotonic()