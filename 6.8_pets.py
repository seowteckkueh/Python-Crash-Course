pets={
    'xiaobao': {
        'species':'dog',
        'owner':'leah'
        },
    'erbao': {
        'species':'dog',
        'owner':'leah'
        },
    'kai xin':{
        'species':'dog',
        'owner':'poppy'
        }
    }

for pet, pet_detail in pets.items():
    print("Pet name: "+pet.title()+"\n\tSpecies: "+pet_detail['species']\
    .title()+"\n\tOwner: "+pet_detail['owner'].title())
