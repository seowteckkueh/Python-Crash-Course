try:
    num1=int(input("please enter the first number: "))
    num2=int(input("please enter the second number: "))
    
except ValueError:
    print("That's not a number, please try again")
    
else:
    total=num1+num2
    print(total)
