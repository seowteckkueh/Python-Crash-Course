favorite_places={
    'andy': ['melbourne','kk'],
    'bill': ['kl'],
    'chris': ['singapore','kk']
    }
    
for name, places in favorite_places.items():
        print(name.title()+"'s favorite place are: ") 
        for place in places:
                print("\t"+place.title())
        print("\n")
