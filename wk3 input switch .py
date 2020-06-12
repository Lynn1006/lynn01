import board
import time
from digitalio import DigitalInOut, Direction

switch = DigitalInOut(board.A1)
switch.direction = Direction.INPUT

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

while True:
    print(switch.value)
    led.value = switch.value

    time.sleep(0.1)