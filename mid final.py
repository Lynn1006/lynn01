import array, math, time
import audiobusio, board, analogio
from adafruit_circuitplayground.express import cpx
import adafruit_fancyled as fancy
import myfunction
Value = time.monotonic()
time.sleep(1)
T2 = int(time.monotonic() - Value)
T1 = int(time.monotonic() - Value)

analogIn_1 = analogio.AnalogIn(board.A1)

CURVE = 2
SCALE_EXPONENT = math.pow(10, CURVE * -0.1)

samples = array.array('H', [0] * 80)
buttonPre = False


TH = 600


cpx.pixels.brightness = 0.1
cpx.pixels.fill(0)
offset = 0

mic = audiobusio.PDMIn(

    board.MICROPHONE_CLOCK,

    board.MICROPHONE_DATA,

    sample_rate=16000,

    bit_depth=16

)


colorList = [0, 0, 0]

listIndex = 0
TH = 600



sampleTime = time.monotonic()

sampleInterval = 0.05

soundLevels = []
for x in range(10):

    mic.record(samples, len(samples))

    RMS = myfunction.normalized_rms(samples)

    soundLevels.append(RMS)

    time.sleep(sampleInterval)


averageRMS = myfunction.mean(soundLevels)


magnitude = 0

ledMode = 0

lightMode = 0
SOUND_VISUALIZER = 1

Value = time.monotonic()

time.sleep(1)


B2 = (173, 216, 230)
B1 = (0, 0, 255)

Y1 = (255, 69, 0)
Y2 = (100,100, 0)

def loop():
    pointValue = scaleAndTranslate(T1, 1, 60, 0, 9)
    i = int(pointValue)
    cpx.pixels[i] = B2
    cpx.pixels[M] = B1

while True:



    if cpx.button_b != buttonPre:
        buttonPre = cpx.button_b
        if cpx.button_b:
            buttonPressTime = time.monotonic()
        else:
            if time.monotonic() >= buttonPressTime + 0.05:
                lightMode += 1
                print('plus')
                if lightMode > 3:
                    lightMode = 0
                    cpx.pixels.fill(0)


    if lightMode == 1:


        if time.monotonic() >= sampleTime:

            sampleTime += sampleInterval


            mic.record(samples, len(samples))

            RMS = myfunction.normalized_rms(samples)



            input_floor = myfunction.normalized_rms(samples) + 10

            input_ceiling = input_floor + 500



            soundLevels.pop(0)

            soundLevels.append(RMS)

            averageRMS = myfunction.mean(soundLevels)




        colorVal = int(myfunction.scaleAndTranslate(RMS, min(soundLevels), max(soundLevels), 0, 255))


        if colorVal > 255:

            colorVal = 255


        if analogIn_1:
            analogValue = analogIn_1.value
            positionVal = myfunction.scaleAndTranslate(analogIn_1.value, 0, 65535, 1, 4)

        threshold = averageRMS * (int(positionVal))

        if RMS > threshold:

            listIndex += 1

            if listIndex > 2:

                listIndex = 0




        for value in range(3):

            temp = colorList[value]

            temp -= 12

            if temp < 0:

                temp = 0

            colorList[value] = temp


        colorList[listIndex] = colorVal



        cpx.pixels.fill(tuple(colorList))
        print('1mode')
        time.sleep(0.01)

    if lightMode == 2:
        print('2mode')
        if analogIn_1:
            analogValue = analogIn_1.value
            senseVal = myfunction.scaleAndTranslate(analogIn_1.value, 0, 65535, 0, 1500)
            TH = int(senseVal)


        mic.record(samples, len(samples))
        magnitude = myfunction.normalized_rms(samples)

        if magnitude > TH:
            ledMode += 1

        if ledMode > 3:
            ledMode = 0



        if ledMode == 1:
            for i in range(10):
                color = fancy.palette_lookup(myfunction.palette_purple, offset + i / 9)
                cpx.pixels[i] = color.pack()
            cpx.pixels.show()
            offset += 0.08  # Bigger number = faster spin
            time.sleep(0.01)

        if ledMode == 2:
            for i in range(10):
                color = fancy.palette_lookup(myfunction.palette_blue, offset + i / 9)
                cpx.pixels[i] = color.pack()
            cpx.pixels.show()
            offset += 0.08  # Bigger number = faster spin
            time.sleep(0.01)

        if ledMode == 3:
            cpx.pixels.fill(0)
            cpx.pixels.show()

    if lightMode == 3:
        print('3mode')
        T1 = int(time.monotonic() - Value)
        T2 = int(time.monotonic() - Value)
        M = int(T2 / 60)
        cpx.pixels.fill(0)
        if T1 > 59:
            T1 -= 60
            if T1 < 60:
                myfunction.loop()

        if T1 > 59:
            T1 -= 60
            if T1 < 60:
                myfunction.loop()
        if T1 > 59:
            T1 -= 60
            if T1 < 60:
                myfunction.loop()
        if T1 > 59:
            T1 -= 60
            if T1 < 60:
                myfunction.loop()
        if T1 > 59:
            T1 -= 60
            if T1 < 60:
                myfunction.loop()
        if T1 > 59:
            T1 -= 60
            if T1 < 60:
                    myfunction.loop()
        if T1 > 59:
            T1 -= 60
            if T1 < 60:
                myfunction.loop()

        if T1 > 59:
            T1 -= 60
            if T1 < 60:
                myfunction.loop()

        if M == 9:
            cpx.pixels.fill(0)

        if T1 < 60:
            pointValue = myfunction.scaleAndTranslate(T1, 1, 60, 0, 9)
            i = int(pointValue)
            cpx.pixels[i] = B2
            cpx.pixels[M] = B1
        time.sleep(1)
    print(lightMode)