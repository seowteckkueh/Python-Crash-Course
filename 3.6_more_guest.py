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
print(guest[5]+" would you like to join me for dinner tonight?")
