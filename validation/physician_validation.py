

class PhysicianValidation:

    @staticmethod
    def license_number(license_number):
        if not license_number.isdigit() and not isinstance(license_number, str):
            raise ValueError("license_number must be an integer")

    @staticmethod
    def doctor_id(doctor_id):
        if not isinstance(doctor_id, int):
            raise ValueError("doctor_id must be an integer")