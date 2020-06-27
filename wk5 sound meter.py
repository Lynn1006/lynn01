import array

import math

import time

import audiobusio

import board
from adafruit_circuitplayground import cp




def mean(values):

 return sum(values) / len(values)





def normalized_rms(values):

    minbuf = int(mean(values))

    sum_of_samples = sum(

        float(sample - minbuf) * (sample - minbuf)

        for sample in values

    )



    return math.sqrt(sum_of_samples / len(values))





mic = audiobusio.PDMIn(

    board.MICROPHONE_CLOCK,

    board.MICROPHONE_DATA,

    sample_rate=16000,

    bit_depth=16

)

samples = array.array('H', [0] * 160)

mic.record(samples, len(samples))

mic.record(samples, len(samples))

magnitude = normalized_rms(samples)

print(((magnitude),))

def scaleAndTranslate(inVal, inStart, inEnd, outStart, outEnd):
    inRange = inEnd - inStart
    inProportion = inVal / inRange
    outRange = outEnd - outStart
    scaledOut = inProportion * outRange
    return scaledOut + outStart

average = scaleAndTranslate(magnitude, 60, 100, 0, 10)

def weightedSmooth(inVal, weight):
    global average
    average = weight * inVal + ((1 - weight) * average)
    return average


while True:

    mic.record(samples, len(samples))

    magnitude = normalized_rms(samples)

    print(((magnitude),))


    scaleValue = scaleAndTranslate(magnitude, 0, 100, 0, 10)
    soundValue = weightedSmooth(scaleValue, 0.9)
    peak = soundValue

    for i in range(10):
        if i <= peak:
            cp.pixels[i] = (255, 0, 255)
            #cp.play_tone(265, 0.1)
        else:
            cp.pixels[i] = (0, 0, 0)
    cp.pixels.show()


    time.sleep(0.05)
