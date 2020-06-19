import board
import time
import analogio
import neopixel

analogIn = analogio.AnalogIn(board.A1)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0)

def scaleAndTranslate(inVal, inStart, inEnd, outStart, outEnd):
    inRange = inEnd - inStart
    inProportion = inVal / inRange
    outRange = outEnd - outStart
    scaledOut = inProportion * outRange
    return scaledOut + outStart

average = scaleAndTranslate(analogIn.value, 0, 65535, 0, 255)


def weightedSmooth(inVal, weight):
    global average
    average = weight * inVal + ((1 - weight) * average)
    return average


while True:

    analogValue = analogIn.value

    scaleValue = scaleAndTranslate(analogValue, 0, 65535, 0, 255)
    blueValue = weightedSmooth(scaleValue, 0.25)

    print((analogValue, blueValue))

    COLOR = (0, 0, int(blueValue))
    pixels.fill(COLOR)

    time.sleep(0.1)