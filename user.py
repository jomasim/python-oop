
class User():
    ## Enscapsulation
    ## class user ties together all user attributes(name,phone,city)
    # and methods(getUsername,save)
    users = list()
    role = "normal"

    def __init__(self, name, phone, city):
        self.name = name
        self.phone = phone
        self.city = city

    def save(self):
        user = list()
        user.append(self.name)
        user.append(self.phone)
        user.append(self.city)
        self.users.append(user)

    def deleteUser(self):
        if self.role == "admin":
           return True
        else:
            return False

    def getUsername(self):
        return self.name


class Admin(User):
    ## inheritance
    ## admin inherits user attributes
    def __init__(self, name, phone, city, dept):
        self.dept = dept
        User.role = "admin"
        User.__init__(self, name, phone, city)
