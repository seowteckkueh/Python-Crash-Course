from user_class import User

class Admin(User):
    def __init__(self,first_name,last_name,age,gender,height,weight):
        super().__init__(first_name,last_name,age,gender,height,weight)
        self.privileges=Privileges()

class Privileges(User):
    def __init__(self):
        self.privileges=['can add post','can delete post','can ban user']
    def show_privileges(self):
        return self.privileges
