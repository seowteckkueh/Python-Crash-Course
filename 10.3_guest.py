name=input("Key in your name: ")
filename='guest.txt'
with open(filename, 'w') as file_object:
    file_object.write(name)
