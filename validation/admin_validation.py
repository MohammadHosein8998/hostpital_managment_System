import re


class AdminValidation:

    @staticmethod
    def admin_id_validate(value):
        if not isinstance(value, str) or not re.match(r"^[a-z0-9_-]+$", value, re.I):
            raise ValueError("Please enter a valid admin_id")
        return value

    @staticmethod
    def name_validate(value):
        if not isinstance(value, str) or not re.match(r"^[a-zA-Z0\s\d_-]{3,40}$", value, re.I):
            raise ValueError("Please enter a valid name")
        return value

    @staticmethod
    def age_validate(value):
        if not isinstance(value, int) or not value > 0:
            raise ValueError("Please enter a valid age (int), age > 0 ")
        return value

    @staticmethod
    def national_code_validate(value):
        if not isinstance(value, str) or len(value) != 10:
            raise ValueError("Please enter a valid national code. length == 10 !!!")
        return value

    @staticmethod
    def user_name_validate(value):
        if not isinstance(value, str) or not re.match(r"^[a-zA-Z0-9_-]{3,20}$", value, re.I):
            raise ValueError("Please enter a valid user name")
        return value

    @staticmethod
    def password_validate(value):
        if not isinstance(value, str) or not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,256}$",
                                                  value, re.I):
            raise ValueError(
                "Minimum eight characters, at least one letter, one number and one special character [@$!%*#?&]")
        return value
