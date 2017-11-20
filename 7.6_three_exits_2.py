#Use an active variable to control how long the loop runs
count=0
while count<10:
    age=input("What is your age?: ")
    if int(age)<3:
        print("Ticket is free.")
        count+=1
    elif int(age)>=3 and int(age)<=12:
        print("Ticket is $10")
        count+=1
    elif int(age)>12:
        print("Ticket is $15")
        count+=1

