# Write your code here :-)
# import the modules
import time
import board
import pulseio

# declare objects and direction
led = pulseio.PWMOut(board.A1, duty_cycle=0)

# set the variables
fadeInc = 1000

# declare the variables and initailize it
newDutyCycle = 0

"""
pulseio.PWMOut creates a PWMOut object with the name led

you can set the duty_cycle with the property led.duty_cycle

led.duty_cycle accepts a 16-bit integer value from 0 - 65535
"""

# loop forever
while True:
    # Adds a value and the variable and assigns the result to that variable
    newDutyCycle += fadeInc

    # if the value of the variable is larger than 65535
    if newDutyCycle > 65535:
        # the number will equal to:
        newDutyCycle = 65535
        # and the fadeinc will be:
        fadeInc = -1000
    # if the condition for if is False, and the value is less than:
    elif newDutyCycle < 0:
        # the number will equal to:
        newDutyCycle = 0
        # and the fadeinc will be:
        fadeInc = 1000

    # The result will be the led dutycycle:
    led.duty_cycle = newDutyCycle
    # print out the actual number on console:
    print(led.duty_cycle)
    # stop per 0.01 second:
    time.sleep(0.01)