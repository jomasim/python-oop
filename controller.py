from user import User


class Controller():
    def register(self, name, phone, city):
        user = User(name, phone, city)
        ##abstraction
        ## user saving logic is done in the User class which is imported
        ## all that is needed is create a new instance of user and call save without 
        ##worrying of the saving logic
        return user.save()
