# variable=input("This is the input that will take the response")
# print(variable)

# #going to ride the coney island rollar coster
# # 4' or 48inch
# iheight = int(input("How tall are you.Please enter the Age in inches?"))
# if iheight >= 48:
#     print("You may ride")
# else:
#     print("Sorry Kid,Come back next year")

# #Create a password checker
# password="test"
# strUsername = input("Please enter Username")
# strPassword= input("Enter password:")
# if(strPassword== password):
#     print("Open Sesame")
# else:
#     print("Access denied")

# # check the number is even or odd
# iEnterNumber =int(input("Please enter the number"))
# if(iEnterNumber % 2 == 0):
#     print("Even number!")
# else:
#     print("Odd Number!")

# for loop numbers 1 - 152
for inumber in range(1,152):
    print(inumber)

inumjuices = input("Number of bottles of juices")
for inumber in range(int(inumjuices),1,-1):
    print(f"juicebottle{inumber}")
