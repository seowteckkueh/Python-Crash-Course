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


user1=User('ben','kueh',29,'male',172,71)
user1.describe_user()
user1.greet_user()

user2=User('poppy','zhang',25,'female',162,68)
user2.describe_user()
user2.greet_user()
