num1=int(input("Enter a number : "))
num2=int(input("Enter a number : "))
num3=int(input("Enter a number : "))
if(num1>num2):
    if(num1>num3):
        print("Greatet number is number 1")
    else:
        print("Greatet number is number 3")
elif(num2>num3):
    print("Greatet number is number 2" )
else:
    print("Greatet number is number 3" )       