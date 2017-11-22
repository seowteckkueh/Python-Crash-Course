def make_album(artist_name,album_title,track_num):
    """dictionary describing music album"""
    if track_num:
        album={'artist name':artist_name,'album title':album_title,'track number': track_num}
    else:
        album={'artist name':artist_name,'album title':album_title}
    return album
    
active=True
while active:
    artist_name=input("Please enter artist name: \nEnter 'q' to quit.\n")
    if artist_name =='q':
        break
        
    album_title=input("Please enter album title: \nEnter 'q' to quit.\n")
    print("Enter 'q' to quit.")
    if album_title =='q':
        break
    
    track_num=input("Please enter track number: \nEnter 'q' to quit.\n")
    print("Enter 'q' to quit.")
    if track_num =='q':
        break
        
    record=make_album(artist_name,album_title,track_num)
    print("-------RESULT-------")
    print(record)
    active=False
    

