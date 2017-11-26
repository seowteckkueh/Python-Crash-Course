class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print("Restaurant name: "+self.restaurant_name.title()+
        "\nCuisine type: "+self.cuisine_type.title()+
        "\nNumber served: "+ str(self.number_served))
    def open_restaurant(self):
        print("Restaurant " + self.restaurant_name.title() + " is open.")
    def increment_number_served(self,number):
        self.number_served=number

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors
    def display_flavor(self):
        return "Flavors: "+ self.flavors
        
user1=IceCreamStand('sweethut','desert','chocolate')
print(user1.display_flavor())
