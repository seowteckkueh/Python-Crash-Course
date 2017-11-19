favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people_list=['jen','edward','phil','ben','poppy','will','jill']
for people in people_list:
    if people in favorite_languages.keys():
        print("Thanks for participating in the poll!")
    else:
        print("Please participate in the poll.")
