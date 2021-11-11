from shifter import Shifter
import time

class LED8x8():
  pattern = [
    0b11000011, 
    0b10111101, 
    0b01011010,
    0b01111110,
    0b01011010,
    0b01100110, 
    0b10111101, 
    0b11000011]

  row = [
    0b10000000,
    0b01000000,
    0b00100000,
    0b00010000,
    0b00001000,
    0b00000100,
    0b00000010,
    0b00000001
  ]


  
  'LED 8x8 Class'

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)

  def display(self):
    for n in range(0,8):
      self.shifter.shiftByte(LED8x8.pattern[n]) # load the row values
      self.shifter.shiftByte(LED8x8.row[n]) # select the given row
      self.shifter.ping(self.shifter.latchPin)
