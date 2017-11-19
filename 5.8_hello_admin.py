usernames=['admin','ben','poppy','alice','emily','jane']
for username in usernames:
    if username=='admin':
        print("Hello admin, would ou like to see a status report?")
    else:
        print("Hello "+username.title()+" thank you for logging in again.")
        
