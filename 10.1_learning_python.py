filename='10.1_learning_python_text.txt'

with open(filename) as file_object:
    text=file_object.read()
    print(text)



#reading line by line from file_object
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


#reading line by line from a list created by readlines()
with open(filename) as file_object:
    text=file_object.readlines()
    
for line in text:
    print(line.rstrip())

