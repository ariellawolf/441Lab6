from shifter import Shifter
import time

class LED8x8():
  pattern=[
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000
  ]
  row=[
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
  ]


  
  'LED 8x8 Class'

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)

  def display(self):
    for n in range(0,8):
      self.shifter.shiftByte(LED8x8.pattern[n]) # load the row values
      self.shifter.shiftByte(LED8x8.row[n]) # select the given row
      self.shifter.ping(self.shifter.latchPin)
