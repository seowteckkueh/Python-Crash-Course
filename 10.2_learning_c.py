filename='10.1_learning_python_text.txt'
with open(filename) as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.replace('Python','C'))

