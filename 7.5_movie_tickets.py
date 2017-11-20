active=True
while active:
    age=input("What is your age?: ")
    if int(age)<3:
        print("Ticket is free.")
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
    elif int(age)>12:
        print("Ticket is $15")
