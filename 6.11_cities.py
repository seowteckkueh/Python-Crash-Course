cities={
    'bintulu':{
        'country':'malaysia',
        'population':114058,
        'fact':'The name of Bintulu was derived from the local native\
         \n\tlanguage "Mentu Ulau" (picking heads).'
         },
    'dalian':{
        'country':'china',
        'population':6690432,
        'fact':'Modern Dalian originated from Qingniwa pinyin: Qīngníwā\
        \n\tor Qingniwaqiao , a small fishing village.'
        },
    'melbourne':{
        'country':'australia',
        'population':4725316,
        'fact':'Melbourne is located in the south-eastern part of\
        \n\tmainland Australia, within the state of Victoria.'
         }
    }

for city, info in cities.items():
    print("City: "+city.title()+"\n\tCountry: "+info['country'].title()+
    "\n\tPopulation: "+str(info['population'])+
    "\n\tFact: "+info['fact'])
    
