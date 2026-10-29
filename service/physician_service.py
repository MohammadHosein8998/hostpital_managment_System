from data_access.physician_data_managment import PhysicianDatAccess
from model.physician import Physician


class PhysicianService:

    def __init__(self):
        self.__physician_data_access = PhysicianDatAccess()

    def save(self, physician_data):
        registered_physicians = self.__physician_data_access.get_all_physicians()
        is_exist = list(
            filter(lambda registered_patient: registered_patient.national_code == physician_data.national_code,
                   registered_physicians))
        if is_exist:
            raise ValueError(f"patient with this national code : {physician_data.national_code} already registered")
        self.__physician_data_access.save_physician_data(physician_data)

    def get_all_physicians(self):
        physicians = self.__physician_data_access.get_all_physicians()
        return physicians

    def update_physician_by_national_code(self, national_code: str, physician_data: Physician):
        registered_physicians = self.__physician_data_access.get_all_physicians()
        is_exist = list(
            filter(lambda registered_physician: registered_physician.national_code == physician_data.national_code,
                   registered_physicians))
        if len(is_exist) > 1:
            raise ValueError(f"physician with this national code : {physician_data.national_code} already registered")
        self.__physician_data_access.update_physician_by_national_code(national_code, physician_data)

    def delete(self, physician_national_code):
        self.__physician_data_access.delete_physician_by_national_code(physician_national_code)

    def get_physician_by_national_code(self, national_code: str):
        physicians = self.__physician_data_access.get_physician_by_national_code(national_code)
        return physicians
