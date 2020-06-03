import board
from digitalio import DigitalInOut, Direction
import time

# variables

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# time
onTime1 = 0.2
offTime1 = 0.5
onTime2 = 1
offTime2 = 1

# loop forever
while True:
    count = 0
    while count < 3:
        led.value = True
        time.sleep(onTime1)
        led.value = False
        time.sleep(offTime1)
        count = count + 1
    while count < 6:
        led.value = True
        time.sleep(onTime2)
        led.value = False
        time.sleep(offTime2)
        count = count + 1