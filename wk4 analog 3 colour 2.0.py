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
        pixels[7] = (COLOR)
        pixels[8] = (COLOR)
        pixels[9] = (COLOR)

        time.sleep(0.1)


    elif analogIn_2.value > 32000:
        analogValue = analogIn_2.value

        average = scaleAndTranslate(analogIn_2.value, 0, 100000, 0, 255)

        scaleValue = scaleAndTranslate(analogValue, 0, 100000, 0, 255)
        greenValue = weightedSmooth(scaleValue, 0.25)

        print((analogValue, greenValue))

        COLOR = (0, int(greenValue), 0)
        pixels[3] = (COLOR)
        pixels[4] = (COLOR)
        pixels[5] = (COLOR)
        pixels[6] = (COLOR)

        time.sleep(0.1)


    elif analogIn_3.value < 62000:
        analogValue = analogIn_3.value

        average = scaleAndTranslate(analogIn_3.value, 0, 65535, 0, 255)

        scaleValue = scaleAndTranslate(analogValue, 0, 65535, 0, 255)
        redValue = weightedSmooth(scaleValue, 0.25)

        print((analogValue, redValue))

        COLOR = (int(redValue), 0, 0)
        pixels[0] = (COLOR)
        pixels[1] = (COLOR)
        pixels[2] = (COLOR)


        time.sleep(0.1)

    else:
        pixels[0] = (255, 0, 0)
        pixels[1] = (255, 0, 0)
        pixels[2] = (255, 0, 0)
        pixels[3] = (0, 255, 0)
        pixels[4] = (0, 255, 0)
        pixels[5] = (0, 255, 0)
        pixels[6] = (0, 255, 0)
        pixels[7] = (0, 0, 255)
        pixels[8] = (0, 0, 255)
        pixels[9] = (0, 0, 255)




