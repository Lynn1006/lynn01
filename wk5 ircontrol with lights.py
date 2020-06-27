import board
import time
import pulseio
import adafruit_irremote
import neopixel

irIn = pulseio.PulseIn(board.A1, maxlen=120, idle_state=True)

decoder = adafruit_irremote.GenericDecode()

NEC_PWR = [255,0,157,98]

pixels= neopixel.NeoPixel(board.NEOPIXEL, 10)

PURPLE = (255, 0, 255)
CLEAR = (0, 0, 0)

color = CLEAR

lightMode = False

while True:
    pulses = decoder.read_pulses(irIn)
    print(pulses)

    try:
        incomingCode = decoder.decode_bits(pulses)

    except adafruit_irremote.IRNECRepeatException:
        print("NEC repeat!")
        continue

    except adafruit_irremote.IRNECRepeatException as e:
        print("Failed to decode:", e.args)
        continue

    print("NEC Infrared code recieved: ", incomingCode)

    if incomingCode == NEC_PWR:
        lightMode = not lightMode

    if lightMode is True:
        color = PURPLE

    else:
        color = CLEAR

    pixels.fill(color)
