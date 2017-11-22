magicians=['ace','ben','cris']
great_magicians=[]
def show_magicians(input):
    for name in input:
        print(name.title())
    
show_magicians(magicians)

def make_great(input):
    while input:
        current_magician="Great "+input.pop().title()
        great_magicians.append(current_magician)

make_great(magicians)
show_magicians(great_magicians)
