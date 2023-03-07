import random
response = "y"
while(response == "y"):
    roll = random.randint(1,6)

    if(roll == 1):
        print("-----")
        print("     ")
        print("  0  ")
        print("     ")
        print("-----")
    elif(roll == 2):
        print("-----")
        print("     ")
        print("0   0")
        print("     ")
        print("-----")
    elif(roll == 3):
        print("-----")
        print("    0")
        print("  0  ")
        print("0    ")
        print("-----")
    elif(roll == 4):
        print("-----")
        print("0   0")
        print("     ")
        print("0   0")
        print("-----")
    elif(roll == 5):
        print("-----")
        print("0   0")
        print("  0  ")
        print("0   0")
        print("-----")
    else:
        print("-----")
        print("0   0")
        print("0   0")
        print("0   0")
        print("-----")

    response = input("Enter y to continue and n to stop: ")
