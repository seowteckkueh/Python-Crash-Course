active=True
filename='guest_book.txt'
with open(filename, 'a') as file_object:
    while active:
        name=input("Key in your name: ")
        if name!='quit':
            print("Hello "+name)
            file_object.write(name+"\n")
        else:
            break
