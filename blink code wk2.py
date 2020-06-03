import board
from digitalio import DigitalInOut, Direction
import time

# variables

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# time
onTime1 = 0.2
offTime1 = 0.5


# loop forever
while True:
    led.value = True
    time.sleep(onTime1)
    led.value = False
    time.sleep(offTime1)
