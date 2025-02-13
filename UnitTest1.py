import random as rand
import sorter as boxes

def populate(iterations : int, rangeLow : float, rangeHigh : float, clear : bool):
        if(clear == False):
            with open("boxes.txt", "a") as data:
                for i in range(iterations):
                    boxes.add(rand.randrange(rangeLow,rangeHigh), rand.randrange(rangeLow,rangeHigh), rand.randrange(rangeLow,rangeHigh))
        else:
            with open("boxes.txt", "w") as data:
                for i in range(iterations):
                    temp = [rand.randrange(rangeLow,rangeHigh), rand.randrange(rangeLow,rangeHigh), rand.randrange(rangeLow,rangeHigh)]
                    temp = sorted(temp)
                    writeData = str(temp[0]) + " " + str(temp[1]) + " " + str(temp[2]) + "\n"
                    data.write(writeData)

def randFind(iterations : int, rangeLow : float, rangeHigh : float):
     for i in range(iterations):
          

