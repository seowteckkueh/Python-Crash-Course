def user(first, last, **info):
    profile={}
    profile['first']=first
    profile['last']=last
    for key,value in info.items():
        profile[key]=value
    return profile
    

