from shifter import Shifter
import time
import multiprocessing
from random import randint

class LED8x8():
  row = [
    0b10000000,
    0b01000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000,
    0b00000000 
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
    patternArray= multiprocessing.Array('i', 8)
    rowArray= multiprocessing.Array('i', 8)
    displayProcess= multiprocessing.Process(name='Display',target=LED8x8.lightningBug, args=(patternArray,rowArray))

    displayProcess.daemon = True
    displayProcess.start()
   

  def display(self):
    for n in range(0,8):
      self.shifter.shiftByte(LED8x8.patternArray[n]) # load the row values
      self.shifter.shiftByte(LED8x8.rowArray[n]) # select the given row
      self.shifter.ping(self.shifter.latchPin)
    time.sleep(0.001)

  def lightningBug(self):
    i=0
    j=0
    while True:
      try:
        x=randint(-1,1)  # defines motion along row                
        y=randint(-1,1) # defines motion along column
       
        if (x+i)>8 or (x+i)<0:
          x=-x
        if (y+j)>8 or (y+j)<0:
          y=-y
        i= x+i #current location on row (column #)
        j= y+j #current location on column (row #)
        LED8x8.patternArray[j]=0b00000000
        LED8x8.patternArray[y+j]=(0b00000000)|(1<<(x+i))
        time.sleep(.1)


      except Exception as e:
        print(e)