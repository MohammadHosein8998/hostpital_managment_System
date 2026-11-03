from datetime import date

import jdatetime

from model.user import User
from validation.admin_validation import AdminValidation


class Admin(User):
    def __init__(self, admin_id: int, name: str, family: str, national_code: str, birth_date: date, user_name: str,
                 password: str):
        super().__init__(name, family, national_code, birth_date)
        self.admin_id = admin_id
        self.user_name = user_name
        self.password = password

    #  admin_id
    @property
    def admin_id(self):
        return self.__admin_id

    @admin_id.setter
    def admin_id(self, value):
        AdminValidation.admin_id_validate(value)
        self.__admin_id = value

    # user_name
    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, value):
        AdminValidation.user_name_validate(value)
        self.__user_name = value

    # password
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        AdminValidation.password_validate(value)
        self.__password = value

    def __eq__(self, other: Admin) -> bool:
        if not isinstance(other, Admin):
            return NotImplemented

        return (
                self.admin_id == other.admin_id
                and self.name == other.name
                and self.family == other.family
                and self.national_code == other.national_code
                and self.birth_date == other.birth_date
                and self.password == other.password
        )

    # user
    def __repr__(self):
        return f"Admin({self.name}, {self.family} , {self.national_code}, {self.birth_date}, {self.admin_id}, {self.user_name} , {self.password})"

    def values(self):

        persian_birth_date = jdatetime.datetime.fromgregorian(date=self.birth_date)

        string_persian = jdatetime.datetime.strftime(persian_birth_date, "%Y-%m-%d")

        return (
            self.admin_id,
            self.name,
            self.family,
            self.national_code,
            string_persian,
            self.user_name,
            self.password
        )

    def login(self , password : str):
        if self.password == password:
            return True
        return False