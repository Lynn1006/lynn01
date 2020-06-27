import board
import time
import analogio

analogIn = analogio.AnalogIn(board.A9)


def scaleAndTranslate(inVal, inStart, inEnd, outStart, outEnd):
    inRange = inEnd - inStart
    inProportion = inVal / inRange
    outRange = outEnd - outStart
    scaledOut = inProportion * outRange
    return scaledOut + outStart


while True:
        temperature = scaleAndTranslate(analogIn.value, 0, 65535, 0, 50)
        # centigrade temperature
        print("Temperature C:", temperature)
        # fahrenheit temperature
        print("Temperature F:", temperature * 1.8 + 32)
        #plot both temperature
        print((temperature, temperature * 1.8 + 32))
        #print((analogIn.value,))
        time.sleep(1)