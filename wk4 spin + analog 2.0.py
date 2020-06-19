import board
import time
import analogio
import neopixel
from adafruit_circuitplayground.express import cpx
import adafruit_fancyled.adafruit_fancyled as fancy


cpx.pixels.auto_write = False  # Update only when we say
cpx.pixels.fill((0, 0, 0))  # Turn off the NeoPixels if they're on!
cpx.pixels.brightness = 0.1   # make less blinding

palette_purple = [fancy.CRGB(251,126,253),  # pink
           fancy.CRGB(138,43,226),    # purple
           fancy.CRGB(227,37,107),      # violet red
           fancy.CRGB(0,0,0)]          # Black

palette_blue = [fancy.CRGB(83, 42, 133),  # evening red
            fancy.CRGB(38, 36, 96),    # midnight blue
           fancy.CRGB(6, 170, 252),      # bay blue
           fancy.CRGB(0, 0, 0)]          # Black



offset = 0  # Position offset into palette to make it "spin"


analogIn_1 = analogio.AnalogIn(board.A1)
analogIn_2 = analogio.AnalogIn(board.A2)
analogIn_3 = analogio.AnalogIn(board.A3)



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

    if cpx.switch:


        if analogIn_1:
            analogValue = analogIn_1.value

            average = scaleAndTranslate(analogIn_1.value, 0, 65535, 0, 3)
            scaleValue = scaleAndTranslate(analogValue, 0, 65535, 0, 3)
            cpx.pixels.brightness = weightedSmooth(scaleValue, 0.8)

            for i in range(10):
                color = fancy.palette_lookup(palette_purple, offset + i / 9)
                cpx.pixels[i] = color.pack()
            cpx.pixels.show()
            offset += 0.033  # Bigger number = faster spin

            time.sleep(0.01)

        if analogIn_2:
            analogValue = analogIn_2.value
            average = scaleAndTranslate(analogIn_2.value, 0, 65535, 0, 10)
            scaleValue = scaleAndTranslate(analogValue, 0, 65535, 0, 10)

            for i in range(10):
                color = fancy.palette_lookup(palette_purple, offset + i / 9)
                cpx.pixels[i] = color.pack()
            cpx.pixels.show()

            offset += weightedSmooth(scaleValue, 0.8)

            time.sleep(0.01)

        if analogIn_3.value < 62000:

            analogValue = analogIn_3.value
            average = scaleAndTranslate(analogIn_3.value, 0, 65535, 0, 225)
            scaleValue = scaleAndTranslate(analogValue, 0, 65535, 0, 225)

            blueValue = weightedSmooth(scaleValue, 0.25)
            print((analogValue, blueValue))


            palette_bluee = [fancy.CRGB(int(blueValue),126,253),  # pink
                fancy.CRGB(int(blueValue),43,226),    # purple
                fancy.CRGB(int(blueValue),37,107),      # violet red
                fancy.CRGB(0,0,0)]          # Black

            for i in range(10):
                color = fancy.palette_lookup(palette_bluee, offset + i / 9)
                cpx.pixels[i] = color.pack()
                cpx.pixels.show()
                offset += 0.033  # Bigger number = faster spin
                time.sleep(0.05)
    else:
        if analogIn_1:
            analogValue = analogIn_1.value

            average = scaleAndTranslate(analogIn_1.value, 0, 65535, 0, 3)
            scaleValue = scaleAndTranslate(analogValue, 0, 65535, 0, 3)
            cpx.pixels.brightness = weightedSmooth(scaleValue, 0.8)

            for i in range(10):
                color = fancy.palette_lookup(palette_blue, offset + i / 9)
                cpx.pixels[i] = color.pack()
            cpx.pixels.show()
            offset += 0.033  # Bigger number = faster spin

            time.sleep(0.01)

        if analogIn_2:
            analogValue = analogIn_2.value
            average = scaleAndTranslate(analogIn_2.value, 0, 65535, 0, 10)
            scaleValue = scaleAndTranslate(analogValue, 0, 65535, 0, 10)

            for i in range(10):
                color = fancy.palette_lookup(palette_blue, offset + i / 9)
                cpx.pixels[i] = color.pack()
            cpx.pixels.show()

            offset += weightedSmooth(scaleValue, 0.8)

            time.sleep(0.01)

        if analogIn_3.value < 62000:

            analogValue = analogIn_3.value
            average = scaleAndTranslate(analogIn_3.value, 0, 65535, 0, 225)
            scaleValue = scaleAndTranslate(analogValue, 0, 65535, 0, 225)

            redValue = weightedSmooth(scaleValue, 0.25)
            print((analogValue, redValue))


            palette_redd = [fancy.CRGB(251,126,int(redValue)),  # pink
                fancy.CRGB(138,43,int(redValue)),    # purple
                fancy.CRGB(227,37,int(redValue)),      # violet red
                fancy.CRGB(0,0,0)]          # Black

            for i in range(10):
                color = fancy.palette_lookup(palette_redd, offset + i / 9)
                cpx.pixels[i] = color.pack()
                cpx.pixels.show()
                offset += 0.033  # Bigger number = faster spin
                time.sleep(0.05)





