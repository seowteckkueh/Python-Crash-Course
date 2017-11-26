class User():
    def __init__(self,first_name,last_name,age,gender,height,weight):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender
        self.height=height
        self.weight=weight
        self.login_attempts=0
    
    def describe_user(self):
        print("First name: "+self.first_name.title() +
        "\nLast name: "+self.last_name.title()+
        "\nAge: "+str(self.age)+
        "\nGender: "+self.gender.title()+
        "\nHeight: "+str(self.height)+ "cm"+
        "\nWeight: "+str(self.weight)+ "kg"+
        "\nLogin Attempts: "+str(self.login_attempts))
    def greet_user(self):
        full_name=self.first_name+" "+self.last_name
        print("Hello "+full_name.title()+"! Have a nice day!\n")

    def increment_login_attempts(self):
        self.login_attempts+=1
        
        
    def reset_login_attemps(self):
        self.login_attempts=0
        
user1=User('ben','kueh',29,'male',172,71)
user1.describe_user()
#increment
user1.increment_login_attempts()
user1.describe_user()
#increment 2
user1.increment_login_attempts()
user1.describe_user()
#increment 3
user1.increment_login_attempts()
user1.describe_user()
#reset
user1.reset_login_attemps()
user1.describe_user()
