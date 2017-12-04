from collections import OrderedDict
glossary=OrderedDict()


glossary['len']='Count the number of elements in a database.'
glossary['append']='Add an element to the end of a database.'
glossary['del']='Delete an element from a database.'
glossary['pop']='Cut one of the element in a database for later use.'
glossary['sort']='Arrange the data in assending order.'


for function, definition in glossary.items():
    print("'"+function+"'"+" means: \n"+ definition+"\n" )
