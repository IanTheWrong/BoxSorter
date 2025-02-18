import os
import sorter as boxes
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
            boxes.add(s1,s2,s3)
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
        iterations = input("Closest amount of Boxes: ")
        print("finding " + iterations + " boxes with sides: " + s1 + ", " + s2 + ", and " + s3)
        confirm = input("confirm? y/n >>> ")
        if(confirm.lower() == "y" or confirm.lower() == "yes"):
                temp = [s1, s2, s3]
                temp = sorted(temp)
                s1 = temp[0]
                s2 = temp[1]
                s3 = temp[2]
                output = boxes.find(float(s1),float(s2),float(s3),int(iterations))
                if(output[0] == -1):
                    print("No Boxes For Specifications")
                else:
                    print("Find the box with size: " + output[0] + " x " + output[1] + " x " + output[2])
                    bestDifference = 1000
                    confirm = input("Remove? y/n >>>")
                    if(confirm):
                        boxes.remove(output[3])
                        os.system('cls')
                        print("------------------------Find the box with size: " + output[0] + " x " + output[1] + " x " + output[2] + "------------------------")
                    else:
                        os.system('cls')
                        print("------------------------Find the box with size: " + output[0] + " x " + output[1] + " x " + output[2] + "------------------------")

        else:
            os.system('cls')
            continue
    elif(action == "3"):
        exit()
    else:
        os.system('cls')
        print("------------------------Invalid Command------------------------")
        continue
