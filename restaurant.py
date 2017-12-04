class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("Restaurant name: "+self.restaurant_name.title()+
        "\nCuisine type: "+self.cuisine_type.title())
    def open_restaurant(self):
        print("Restaurant " + self.restaurant_name.title() + " is open.")
        
