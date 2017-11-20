#Use a break statement to exit the loop when the user enters a 'quit' value.
age=str()
while age!='quit':
    age=input("What is your age?: ")
    if age=='quit':
        print("Exiting program.")
    elif int(age)<3:
        print("Ticket is free.")
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
    elif int(age)>12:
        print("Ticket is $15")



