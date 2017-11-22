def car_info(manufacturer,model,**other_info):
    car={}
    car['manufacturer']=manufacturer
    car['model']=model
    for key,value in other_info.items():
        car['key']=value
    return car

test=car_info('subaru','outback',color='blue',tow_package=True)
print(test)
