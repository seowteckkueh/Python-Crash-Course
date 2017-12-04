class User():
    def __init__(self,first_name,last_name,age,gender,height,weight):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.height=height
        self.weight=weight
    
    def describe_user(self):
        print("First name: "+self.first_name.title() +
        "\nLast name: "+self.last_name.title()+
        "\nAge: "+str(self.age)+
        "\nGender: "+self.gender.title()+
        "\nHeight: "+str(self.height)+ "cm"+
        "\nWeight: "+str(self.weight)+ "kg")
        
    def greet_user(self):
        full_name=self.first_name+" "+self.last_name
        print("Hello "+full_name.title()+"! Have a nice day!\n")
        
class Admin(User):
    def __init__(self,first_name,last_name,age,gender,height,weight):
        super().__init__(first_name,last_name,age,gender,height,weight)
        self.privileges=Privileges()

class Privileges(User):
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        return self.privileges
