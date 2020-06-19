 import board
 import time
 import analogio
 from digitalio import DigitalInOut, Direction

 analogIn = analogio.AnalogIn(board.A1)

 led1 = DigitalInOut(board.A2)
 led1.direction = Direction.OUTPUT
 led2 = DigitalInOut(board.A3)
 led2.direction = Direction.OUTPUT
 led3 = DigitalInOut(board.A4)
 led3.direction = Direction.OUTPUT
 led4 = DigitalInOut(board.A5)
 led4.direction = Direction.OUTPUT
 led5 = DigitalInOut(board.A6)
 led5.direction = Direction.OUTPUT






TH1 = 5000
TH2 = 17000
TH3 = 29000
TH4 = 41000
TH5 = 53000



 while True:
     analogValue = analogIn.value

     print((analogIn.value, TH1, TH2, TH3, TH4, TH5))

     if analogValue > TH5:
        led1.value = True
        led2.value = True
        led3.value = True
        led4.value = True
        led5.value = True
     elif analogValue > TH4:
        led1.value = True
        led2.value = True
        led3.value = True
        led4.value = True
        led5.value = False
     elif analogValue > TH3:
        led1.value = True
        led2.value = True
        led3.value = True
        led4.value = False
        led5.value = False
     elif analogValue > TH2:
        led1.value = True
        led2.value = True
        led3.value = False
        led4.value = False
        led5.value = False
     elif analogValue > TH1:
        led1.value = True
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False


     else:
         led1.value = False

     time.sleep(0.1)