people={
    'poppy': {
        'first_name': 'poppy',
        'last_name': 'zhang',
        'age': 25,
        'city': 'dalian',
        'gender': 'female'
        },
    'ben': {
        'first_name':'ben',
        'last_name':'kueh',
        'age':29,
        'city':'bintulu',
        'gender':'male'
        },
    'sam': {
        'first_name':'sam',
        'last_name':'han',
        'age':27,
        'city':'kk',
        'gender':'female'
        }
}

for user,user_info in people.items(): 
    full_name=user_info['first_name']+" "+user_info['last_name']
    print(user+"\n\tName: "+full_name.title()+"\n\tAge: "+str(user_info\
    ['age'])+"\n\tCity: "+user_info['city'].title()+"\n\tGender: "+
    user_info['gender'].title())
