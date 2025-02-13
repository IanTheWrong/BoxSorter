import os
best = ""
bestDifference = 1000

#TODO: Write alternate program for unit testing, random population of database + Self test results onto another txt file
#TODO: Make Text UI 1,2,3 selection menus DONE
#TODO: Allow find() to be able to find "Nearest" X amount of boxes
#TODO: List all boxes function DONE
#TODO: Make it so that a "removal" just marks it for deletion DONE

def add(width, length, height):
    temp = [width, length, height]
    temp = sorted(temp)
    width = temp[0]
    length = temp[1]
    height = temp[2]

    with open("boxes.txt", "a") as data:
        writeData = str(width) + " " + str(length) + " " + str(height) + "\n"
        data.write(writeData)

def find(width : float,length : float, height : float):
    global best
    global bestDifference
    iteration = 0
    index = 0
    with open("boxes.txt", "r") as data:
        for current in data:
            #isAvailible must go first to make sure the current line isn't deleted
            if(isAvailible(current) and getWidth(current) >= width and getLength(current) >= length and getHeight(current) >= height):
                difference = float(getWidth(current) - width) + float(getLength(current)) + float(getHeight(current))
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
            print("Find the box with size: " + s1 + " x " + s2 + " x " + s3)
            bestDifference = 1000
            confirm = input("Remove? y/n >>>")
            if(confirm.lower() == "y" or confirm.lower() == "yes"):
                remove(index)
                os.system('cls')
                print("------------------------Find the box with size: " + s1 + " x " + s2 + " x " + s3 + "------------------------")
            else:
                os.system('cls')
                print("------------------------Find the box with size: " + s1 + " x " + s2 + " x " + s3 + "------------------------")


def remove(index):
    filtered = []
    with open("boxes.txt", "r") as data:
        increment = 0
        for line in data:
            if(increment != index):
                filtered.append(line)
            else:
                filtered.append(line + " -")
            increment += 1

    with open("boxes.txt", "w") as data:
        data.writelines(filtered)

def listBoxes():
    with open("boxes.txt", "r") as data:
        total = data.readlines()
        for i in range(len(total)):
            print(total[i], end="")



#gets the values for a single readline
def getWidth(width):
    if(isAvailible(width)):
        index = width.find(" ")
        print(index)
        return float(width[:index])

def getLength(length):
    if(isAvailible(length)):
        start = length.find(" ")
        end = length.find(" ", start+1)
        return float(length[start+1:end])

def getHeight(height):
    if(isAvailible(height)):
        start = height.rfind(" ")
        return float(height[start:])

def isAvailible(index):
    if(index.find("-") == -1):
        return True
    else:
        return False

while(True):
    print("Box Find & Sort")
    print("What would you like to do? (add (1), find (2), exit (3))")
    action = input(">>> ")
    if(action == "1"):
        print("Adding New Box...")
        s1 = input("First Side: ")
        s2 = input("Second Side: ")
        s3 = input("Third Side: ")
        print("adding box with sides: " + s1 + ", " + s2 + ", and " + s3)
        confirm = input("confirm? y/n >>> ")
        if(confirm.lower() == "y" or confirm.lower() == "yes"):
            add(s1,s2,s3)
            os.system('cls')
            print("------------------------ADDED------------------------")
            
        else:
            os.system('cls')
            continue
    elif(action == "2"):
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
                find(float(s1),float(s2),float(s3))
        else:
            os.system('cls')
            continue
    elif(action == "3"):
        exit()
    else:
        os.system('cls')
        print("------------------------Invalid Command------------------------")
        continue
