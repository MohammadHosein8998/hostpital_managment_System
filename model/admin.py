class Admin:
    def __init__(self, admin_id, name, age, user_name, password):
        self.admin_id = admin_id
        self.name = name
        self.age = age
        self.user_name = user_name
        self.password = password

    #  admin_id
    @property
    def admin_id(self):
        return self.__admin_id

    @admin_id.setter
    def admin_id(self, value):
        self.__admin_id = value

    # name
    @property
    def name(self):
        return self.__name + " hello "

    @name.setter
    def name(self, value):
        self.__name = value

    #  age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    # user_name
    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, value):
        self.__user_name = value

    # password
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    # user
    def __repr__(self):
        return f"Admin({self.name}, {self.age}, {self.user_name}, {self.password})"
