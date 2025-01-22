best = ""
bestDifference = 1000

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
                    best = str(getWidth(current)) + " " + str(getLength(current)) + " " + str(getHeight(current))
                    s1 = str(getWidth(current))
                    s2 = str(getLength(current))
                    s3 = str(getHeight(current))
                    index = iteration
            iteration += 1
        if(bestDifference == 1000):
            print("No Boxes For Specifications")
        else:
            remove(index)
            print("Find the box with size: " + s1 + " x " + s2 + " x " + s3)
            bestDifference = 1000

def remove(index):
    filtered = []
    with open("boxes.txt", "r") as data:
        increment = 0
        for line in data:
            if(increment != index):
                filtered.append(line)
            increment += 1
    with open("boxes.txt", "w") as data:
        data.writelines(filtered)



#gets the values for a single readline
def getWidth(width):
    index = width.find(" ")
    print(index)
    return int(width[:index])

def getLength(length):
    start = length.find(" ")
    end = length.find(" ", start+1)
    return int(length[start+1:end])

def getHeight(height):
    start = height.rfind(" ")
    return int(height[start:])

while(True):
    print("Box Find & Sort")
    print("What would you like to do? (add, find, exit)")
    action = input(">>> ")
    if(action == "add"):
        print("Adding New Box...")
        s1 = input("First Side: ")
        s2 = input("Second Side: ")
        s3 = input("Third Side: ")
        print("adding box with sides: " + s1 + ", " + s2 + ", and " + s3)
        confirm = input("confirm? y/n >>> ")
        if(confirm.lower() == "y" or confirm.lower() == "yes"):
            add(s1,s2,s3)
            print("added\n\n")
        else:
            continue
    elif(action == "find"):
        print("Item Dimensions:")
        s1 = input("First Side: ")
        s2 = input("Second Side: ")
        s3 = input("Third Side: ")
        print("finding box with sides: " + s1 + ", " + s2 + ", and " + s3)
        confirm = input("confirm? y/n >>> ")
        if(confirm.lower() == "y" or confirm.lower() == "yes"):
                temp = [s1, s2, s3]
                temp = sorted(temp)
                s1 = temp[0]
                s2 = temp[1]
                s3 = temp[2]
                find(int(s1),int(s2),int(s3))
        else:
            continue
    elif(action == "exit"):
        exit()
    else:
        print("Invalid Command")
        continue
