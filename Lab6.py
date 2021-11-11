import time
from LED8x8 import LED8x8

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 23, 24, 25

# Pick a number sequence
sequence = [1, 2, 3, 4, 5, 6, 7, 8]

ourLED= LED8x8(dataPin, latchPin, clockPin)

while True:
  try:
    ourLED.display()
    time.sleep(0.001)
  except Exception as e:
    print(e)