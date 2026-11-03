import re


class AdminValidation:

    @staticmethod
    def admin_id_validate(value):
        if not isinstance(value, int):
            raise ValueError("Invalid admin id . must be int")

    @staticmethod
    def name_validate(value):
        if not isinstance(value, str) or not re.match(r"^[a-zA-Z0\s\d_-]{3,40}$", value, re.I):
            raise ValueError("Please enter a valid name")

    # @staticmethod
    # def birth_date_validation(value):
        # if not isinstance(value, str) or not re.match()

    @staticmethod
    def age_validate(value):
        if not isinstance(value, int) or not value > 0:
            raise ValueError("Please enter a valid age (int), age > 0 ")

    @staticmethod
    def national_code_validate(value):
        if not isinstance(value, str) or len(value) != 10:
            raise ValueError("Please enter a valid national code. length == 10 !!!")

    @staticmethod
    def user_name_validate(value):
        if not isinstance(value, str) or not re.match(r"^[a-zA-Z0-9@\\.]{3,20}$", value, re.I):
            raise ValueError("Please enter a valid user name")

    @staticmethod
    def password_validate(value):
        if not isinstance(value, str) or not re.match(
                r"^[A-Za-z1-9\d@$!%*#?&\\.]{4,100}$",
                value, re.I):
            raise ValueError(
                "Minimum four characters, include a-z ,A-Z , 1-9 and [@$!%*#?&]")
