class Admin:
    def __init__(self, admin_id, name, age, user_name, password):
        self.__admin_id = admin_id
        self.__name = name
        self.age = age
        self.user_name = user_name
        self.password = password

    @property
    def admin_id(self):
        return self.__admin_id

    @admin_id.setter
    def set_admin_id(self, admin_id):
        self.__admin_id = admin_id


    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self):
        return self.__name
