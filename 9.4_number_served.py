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
user1=Restaurant('mama mia','italian')
user1.describe_restaurant()

#directly change the value of number_served
user1.number_served=20
user1.describe_restaurant()


#use the increment_number_served method to change number_served
user1.increment_number_served(30)
user1.describe_restaurant()

