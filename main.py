
best = ""
bestDifference = 100

def add(width, length, height):
    temp = [width, length, height]
    temp = sorted(temp)
    width = temp[0]
    length = temp[1]
    height = temp[2]

    with open("boxes.txt", "a") as data:
        writeData = str(width) + " " + str(length) + " " + str(height) + "\n"
        data.write(writeData)

def find(width, length, height):
    global best
    global bestDifference
    iteration = 0
    index = 0
    with open("boxes.txt", "r") as data:
        for current in data:
            if(getWidth(current) >= width and getLength(current) >= length and getHeight(current) >= height):
                difference = (getWidth(current) - width) + (getLength(current)) + (getHeight(current))
                if(difference < bestDifference):
                    bestDifference = difference
                    print(bestDifference)
                    best = str(getWidth(current)) + " " + str(getLength(current)) + " " + str(getHeight(current))
                    index = iteration
            iteration += 1
    remove(index)
    print(best)

def remove(index):
    filtered = []
    with open("boxes.txt", "r") as data:
        readFile = data.readlines()
        increment = 0
        for line in readFile:
            if(increment != index):
                filtered.append(readFile[increment])
            increment += 1
    with open("boxes.txt", "w") as data:
        data.writelines(filtered)



#gets the values for a single readline
def getWidth(width):
    index = width.find(" ")
    return int(width[:index])

def getLength(length):
    start = length.find(" ")
    end = length.find(" ", start+1)
    return int(length[start+1:end])

def getHeight(height):
    start = height.rfind(" ")
    return int(height[start:])

add(3, 7, 2)
add(8, 1, 9)
add(5, 6, 4)
add(2, 10, 3)
add(9, 4, 6)
add(1, 8, 7)
add(6, 9, 5)
add(7, 3, 10)
add(4, 2, 8)
add(10, 5, 1)
add(6, 8, 9)
add(3, 4, 7)
add(1, 9, 6)
add(2, 5, 10)
add(8, 7, 3)
add(9, 2, 5)
add(4, 6, 8)
add(7, 10, 1)
add(5, 3, 9)
add(10, 6, 2)
add(3, 8, 4)
add(1, 7, 9)
add(9, 5, 3)
add(2, 6, 10)
add(6, 4, 8)
add(7, 2, 1)
add(8, 10, 5)
add(4, 9, 7)
add(5, 1, 6)
find(2,3,4)
