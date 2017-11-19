rivers={
    'nile':'egypt',
    'brahmaputra river':'india',
    'yellow river':'china'
    }
    
for river,country in rivers.items():
    print("The "+river.title()+" runs throuth "+country+".")
    
for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)
