while True:
    try:
        num1=input("please enter the first number: ")
        break
    except ValueError:
        print("That's not a number, please try again")
        
while True:
    try:
        num2=int(input("please enter the second number: "))
        break
    except ValueError:
        print("That's not a number, please try again")
total=num1+num2
print(total)
