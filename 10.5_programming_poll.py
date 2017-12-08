active=True

with open('reasons.txt','a') as file_object:
    while active:
        reason=input("Why do you like programming?")
        if reason!='quit':
            file_object.write(reason+"\n")
        else:
            break
                
