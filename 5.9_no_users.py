usernames=['admin','ben','poppy','alice','emily','jane']
if usernames:
    for username in usernames:
        if username=='admin':
            print("Hello admin, would ou like to see a status report?")
        else:
            print("Hello "+username.title()+" thank you for logging in again.")
else:
    print("We need to find some users!")

#removed all the usernames
usernames=[]
if usernames:
    for username in usernames:
        if username=='admin':
            print("Hello admin, would ou like to see a status report?")
        else:
            print("Hello "+username.title()+" thank you for logging in again.")
else:
    print("We need to find some users!")
        
