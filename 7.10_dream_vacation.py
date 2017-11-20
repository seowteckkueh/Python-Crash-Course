responses={}
active=True
while active:
    name=input("what is your name? :")
    response=input("If you could visit one place in the world, where would \
    \nyou go?: ")
    responses[name]=response
    repeat=input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        active=False

print("\n---Poll Results--")
for name,response in responses.items():
    print(name+" would like to visit "+response+".")

