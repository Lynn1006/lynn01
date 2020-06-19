import board
import time
import analogio
import neopixel

analogIn_1 = analogio.AnalogIn(board.A1)
analogIn_2 = analogio.AnalogIn(board.A2)
analogIn_3 = analogio.AnalogIn(board.A3)


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1.0)

def scaleAndTranslate(inVal, inStart, inEnd, outStart, outEnd):
    inRange = inEnd - inStart
    inProportion = inVal / inRange
    outRange = outEnd - outStart
    scaledOut = inProportion * outRange
    return scaledOut + outStart


# average = scaleAndTranslate(analogIn_1.value, 0, 65535, 0, 255)


def weightedSmooth(inVal, weight):
    global average
    average = weight * inVal + ((1 - weight) * average)
    return average


while True:

    if analogIn_1.value > 1000:
        analogValue = analogIn_1.value

        average = scaleAndTranslate(analogIn_1.value, 0, 65535, 0, 255)

        scaleValue = scaleAndTranslate(analogValue, 0, 65535, 0, 255)
        blueValue = weightedSmooth(scaleValue, 0.25)

        print((analogValue, blueValue))

        COLOR = (0, 0, int(blueValue))
        pixels.fill(COLOR)

        time.sleep(0.1)


    elif analogIn_2.value > 32000:
        analogValue = analogIn_2.value

        average = scaleAndTranslate(analogIn_2.value, 0, 65535, 0, 255)

        scaleValue = scaleAndTranslate(analogValue, 0, 65535, 0, 255)
        blueValue = weightedSmooth(scaleValue, 0.25)

        print((analogValue, blueValue))

        COLOR = (0, 0, int(blueValue))
        pixels.fill(COLOR)

        time.sleep(0.1)


    elif analogIn_3.value < 62000:
        analogValue = analogIn_3.value

        average = scaleAndTranslate(analogIn_3.value, 0, 65535, 0, 255)

        scaleValue = scaleAndTranslate(analogValue, 0, 65535, 0, 255)
        blueValue = weightedSmooth(scaleValue, 0.25)

        print((analogValue, blueValue))

        COLOR = (0, 0, int(blueValue))
        pixels.fill(COLOR)

        time.sleep(0.1)

    else:
        COLOR = (0, 0, 80)
        pixels.fill(COLOR)



