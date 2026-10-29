from jdatetime import datetime

from model.physician import Physician
from service.physician_service import PhysicianService
from utils.decorators import Error_handler


class PhysicianController:
    doctor_id = 0

    def __init__(self):
        self.__physician_service = PhysicianService()

    def __make_new_physician(self, physician):
        (name, family, national_code, birth_date, license) = physician.values()

        birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date().togregorian()

        PhysicianController.doctor_id += 1

        new_physician = Physician(PhysicianController.doctor_id, name, family, national_code, birth_date, license)

        return new_physician

    @Error_handler
    def save(self, physician_data):
        physician = self.__make_new_physician(physician_data)
        self.__physician_service.save(physician)
        return f"doctor with name {physician.name} {physician.family} save successfully"

    @Error_handler
    def delete(self , physician_data):
        physician = self.__make_new_physician(physician_data)
        self.__physician_service.delete(physician)
        return f"doctor with name {physician.name} deleted successfully"

    @Error_handler
    def update(self , physician_data):
        physician = self.__make_new_physician(physician_data)
        self.__physician_service.update_physician_by_national_code(physician.national_code , physician)
        return f"doctor with name {physician.name} and national_code {physician.national_code} updated successfully"

    @Error_handler
    def get_all_physician(self):
        physicians = self.__physician_service.get_all_physicians()
        return physicians
