import board
import time
import pulseio
import adafruit_irremote
from adafruit_circuitplayground import cp

irIn = pulseio.PulseIn(board.A1, maxlen=120, idle_state=True)

decoder = adafruit_irremote.GenericDecode()

NEC_PWR = [255,0,157,98]
NEC_A = [255,0,221,34]


PURPLE = (255, 0, 255)
CLEAR = (0, 0, 0)

print(int(time.monotonic()))

Value = time.monotonic()

time.sleep(1)

T = int(time.monotonic() - Value)

R = int(125 / T)
G = int(60 / T)
B = int(T * 5)
X = T - 30

color = CLEAR

lightMode1 = False
lightMode2 = False

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
        lightMode1 = not lightMode1

        if lightMode1 is True:
            cp.play_file("music3.wav")

    elif incomingCode == NEC_A:
        lightMode2 = not lightMode2

        if lightMode2 is True:
            T = int(time.monotonic() - Value)
            COLOR_1 = (R, G, B)
            if T < 30:
                R = int(125 / T)
                G = int(60 / T)
                B = int(T * 5)
                COLOR_1 = (R, G, B)
                cp.pixels.fill(COLOR_1)
                cp.pixels.show()

            if T > 30:
                X = T - 30
                COLOR_2 = (X, X * 2, int(150 / X))
                cp.pixels.fill(COLOR_2)
                cp.pixels.show()

            if T > 80:
                cp.pixels.fill(CLEAR)
                cp.pixels.show()


            print(T, R, G, B, X)
            time.sleep(1)



