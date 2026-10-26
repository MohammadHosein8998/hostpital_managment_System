from model.user import User


class Physician(User):

    @staticmethod
    def license_number(license_number):
        if not license_number.isdigit():
            raise ValueError("license_number must be an integer")
