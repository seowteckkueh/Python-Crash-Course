favorite_number={
    'apple':[1,5],
    'ben':[2,23],
    'poppy':[23,42],
    'zen':[5,4,12],
    'chris':[7,123,1,3]
    }
for name,numbers in favorite_number.items():
    print("Name: "+name.title()+"\nFavorite numbers:")
    for number in numbers:
        print(number)
    print("\n")
