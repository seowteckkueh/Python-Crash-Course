guest=['Ben','Sam','Carrissa']
print(guest[0]+" would you like to join me for dinner tonight?")
print(guest[1]+" would you like to join me for dinner tonight?")
print(guest[2]+" would you like to join me for dinner tonight?\n")

print(guest[0]+"\n")
guest[0]='Poppy'
print(guest[0]+" would you like to join me for dinner tonight?")
print(guest[1]+" would you like to join me for dinner tonight?")
print(guest[2]+" would you like to join me for dinner tonight?\n")

print("I've found a bigger dinner table.\n")
guest.insert(0,'Ben')
guest.insert(2,'Gordon')
guest.append('Emily')

print(guest[0]+" would you like to join me for dinner tonight?")
print(guest[1]+" would you like to join me for dinner tonight?")
print(guest[2]+" would you like to join me for dinner tonight?")
print(guest[3]+" would you like to join me for dinner tonight?")
print(guest[4]+" would you like to join me for dinner tonight?")
print(guest[5]+" would you like to join me for dinner tonight?\n")

print("I can only invite two people for dinner.\n")

print(guest.pop(5)+", sorry you're uninvited for the dinner.")
print(guest.pop(4)+", sorry you're uninvited for the dinner.")
print(guest.pop(3)+", sorry you're uninvited for the dinner.")
print(guest.pop(2)+", sorry you're uninvited for the dinner.\n")

print(guest[0]+", you're still invited for the dinner.")
print(guest[1]+", you're still invited for the dinner.\n")

del guest[0]
del guest[0]

print(guest)

