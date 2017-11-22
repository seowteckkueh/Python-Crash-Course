def make_album(artist_name,album_title):
    """dictionary describing music album"""
    album={'artist name':artist_name,'album title':album_title}
    return album
    
record=make_album('henry','hello')
record2=make_album('ben','haha')
record3=make_album('poppy','love you')

print(record)
print(record2)
print(record3)

def make_album(artist_name,album_title,track_num):
    """dictionary describing music album"""
    if track_num:
        album={'artist name':artist_name,'album title':album_title,'track number': track_num}
    else:
        album={'artist name':artist_name,'album title':album_title}
    return album

record4=make_album('carri','byebye',12)
print(record4)
