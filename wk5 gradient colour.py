import time
from adafruit_circuitplayground import cp

print(int(time.monotonic()))

Value = time.monotonic()

time.sleep(1)

T = int(time.monotonic() - Value)

R = int(125 / T)
G = int(60 / T)
B = int(T * 5)
X = T - 30
Clear = (0, 0, 0)

cp.play_file("music3.wav")


while True:
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
        cp.pixels.fill(Clear)
        cp.pixels.show()


    print(T, R, G, B, X)
    time.sleep(1)
