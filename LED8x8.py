from shifter import Shifter
import time
import multiprocessing
from random import randint

class LED8x8():
  row = [
    0b00000001,
    0b00000010,
    0b00000100,
    0b00001000,
    0b00010000,
    0b00100000,
    0b01000000,
    0b10000000 
    ]

  pattern = [
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111,
    0b11111111
    ]

  'LED 8x8 Class'

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
    self.patternArray= multiprocessing.Array('i', 8)
    self.rowArray= multiprocessing.Array('i', 8)
    self.displayProcess= multiprocessing.Process(name='Display',target=self.display, args=(self.patternArray,self.rowArray))

    self.displayProcess.daemon = True
    self.displayProcess.start()
   

  def display(self, patternArray, rowArray):
    for n in range(0,8):
      self.shifter.shiftByte(patternArray[n]) # load the row values
      self.shifter.shiftByte(rowArray[n]) # select the given row
      self.shifter.ping(self.shifter.latchPin)
    time.sleep(0.001)

  def lightningBug(self):
    i=0
    j=0
    while True:
      try:
        x=randint(-1,1)  # defines motion along row                
        y=randint(-1,1) # defines motion along column
       
        if (x+i)>7 or (x+i)<0:
          x=-x
        if (y+j)>7 or (y+j)<0:
          y=-y
        i= x+i #current location on row (column #)
        j= y+j #current location on column (row #)
        self.patternArray[j]=0b11111111
        self.patternArray[y+j]=(~((0b11111111)|(0<<(x+i)))&(0b11111111))
        time.sleep(.1)


      except Exception as e:
        print(e)