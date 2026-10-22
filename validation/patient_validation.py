import re

from persian_tools import phone_number


class PatientValidation:
    @staticmethod
    def validate_phone_number(phone_num):
        if not isinstance(phone_num, str) :
            raise TypeError('Phone Number must be a string')
        elif not phone_number.validate(phone_num):
            raise ValueError('Phone Number must be a valid phone number')