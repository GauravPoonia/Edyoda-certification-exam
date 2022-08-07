class User:

    def __init__(self, name, userName, password, userType):
        self.name = name
        self.userName = userName
        self.password = password
        self.userType = userType

    def __str__(self):
        return f"Name : {self.name} \nuserName : {self.userName} \password : {self.password} \nuserType : {self.userType}"

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def set_userName(self,userName):
        self.userName = userName

    def get_userName(self):
        return self.userName

    def set_password(self,password):
        self.password = password

    def get_password(self):
        return self.password

    def set_userType(self,userType):
        self.userType = userType

    def get_userType(self):
        return self.userType

    