# Write your code here :-)
 import board
 import timeimport analogio

 analogIn = analogio.AnalogIn(board.A1)
 analogOut = analogio.AnalogOut(board.A0)

 while True:
     print((analogin.value))

     analogIn.value = analogOut.value

     time.sleep(0.1)