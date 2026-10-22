from persian_tools import national_id, phone_number as phone_num
from datetime import date
import re



class UserValidation:


    @staticmethod
    def validate_name(name):
        if not isinstance(name , str) or not re.match(r'^[A-Za-z\s\-_]{0,60}$', name , re.I):
            raise ValueError("name is not valid")

    @staticmethod
    def validate_family(family):
        if not isinstance(family , str) or not re.match(r'^[A-Za-z\s\-_]{0,40}$', family , re.I):
            raise ValueError("family is not valid")

    @staticmethod
    def validate_national_code(national_code):
        if not isinstance(national_code, str) or not re.match(r'^[0-9]{0,10}$', national_code):
            raise ValueError("national_code is not valid")
        elif not national_id.validate(national_code):
            raise ValueError("national_code number is not valid")

    @staticmethod
    def validate_birth_date(birth_date):
        if not isinstance(birth_date, date):
            raise ValueError("birth_date must be a Date type")
        elif birth_date > birth_date.today():
            raise ValueError("birth_date cannot be in the future")
        