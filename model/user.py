from datetime import date

from validation.user_validation import UserValidation

class User:

    def __init__(self, name: str, family: str, national_code: str, birth_date: date):
        self.name = name
        self.family = family
        self.national_code = national_code
        self.birth_date = birth_date

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        UserValidation.validate_name(value)
        self.__name = value

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        UserValidation.validate_family(value)
        self.__family = value

    @property
    def national_code(self):
        return self.__national_code

    @national_code.setter
    def national_code(self, value):
        UserValidation.validate_national_code(value)
        self.__national_code = value

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        UserValidation.validate_birth_date(value)
        self.__birth_date = value

    def __repr__(self) -> str:
        return f"user(name : {self.name} , family : {self.family}, national_code : {self.national_code} , birth_date : {self.birth_date})"
