from validation.admin_validation import AdminValidation


class Admin:
    def __init__(self, admin_id: str, name: str, age: int, national_code: str, user_name: str, password: str):
        self.admin_id = admin_id
        self.name = name
        self.age = age
        self.national_code = national_code
        self.user_name = user_name
        self.password = password

    #  admin_id
    @property
    def admin_id(self):
        return self.__admin_id

    @admin_id.setter
    def admin_id(self, value):
        value = AdminValidation.admin_id_validate(value)
        self.__admin_id = value

    # name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        value = AdminValidation.name_validate(value)
        self.__name = value

    #  age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        value = AdminValidation.age_validate(value)
        self.__age = value

    @property
    def national_code(self):
        return self.__national_code

    @national_code.setter
    def national_code(self, value):
        value = AdminValidation.national_code_validate(value)
        self.__national_code = value

    # user_name
    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, value):
        value = AdminValidation.user_name_validate(value)
        self.__user_name = value

    # password
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        value = AdminValidation.password_validate(value)
        self.__password = value

    # user
    def __repr__(self):
        return f"Admin({self.name}, {self.age}, {self.user_name}, {self.password})"
