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
     open("log.txt", "w").close()
     with open("log.txt", "a") as data:
        for i in range(iterations):
            temp = [float(rand.randrange(rangeLow,rangeHigh)), float(rand.randrange(rangeLow,rangeHigh)), float(rand.randrange(rangeLow,rangeHigh))]
            temp = sorted(temp)
            output = boxes.find(temp[0],temp[1],temp[2])
            boxes.remove(output[3])
            if(output[0] == -1):
                data.write("No Boxes For Specifications")
            else:
                data.write(str(output[0]) + " x " + str(output[1]) + " x " + str(output[2]) + " ORIGINAL: " + str(temp[0]) + " x " + str(temp[1]) + " x " + str(temp[2]) + "\n")
populate(1000, 1, 300, True)
randFind(300, 2, 100)



          

