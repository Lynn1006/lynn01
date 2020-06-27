import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3


minimum_temp = 30
maximum_temp = 35

#sign the scale of temperature to neopixels
def scale_range(value):
    return int((value - minimum_temp) / (maximum_temp - minimum_temp) * 10)


while True:
    peak = scale_range(cp.temperature)
    print(cp.temperature)
    print((cp.temperature, cp.temperature * 1.8 + 32))
    print(int(peak))

    for i in range(10):
        if i <= peak:
            cp.pixels[i] = (255, 0, 255)
            #cp.play_tone(265, 0.1)
        else:
            cp.pixels[i] = (0, 0, 0)
    cp.pixels.show()
    time.sleep(0.05)