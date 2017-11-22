magicians=['ace','ben','cris']
great_magicians=[]
def show_magicians(input):
    """print out the name of the magicians"""
    for name in input:
        print(name.title())
    
show_magicians(magicians)

def make_great(input):
    """add 'Great' in front of the magicians name"""
    while input:
        current_magician="Great "+input.pop().title()
        great_magicians.append(current_magician)

make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
