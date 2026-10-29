from unittest import result

import jdatetime

from model import patient
from service.patient_service import PatientService
from model.patient import Patient
from utils.decorators import Error_handler


# def Error_handler(func_name):
#     def inner(*args, **kwargs):
#         try:
#             result = func_name(*args, **kwargs)
#             return True, result
#         except Exception as e:
#             return False, e
#
#     return inner


class PatientController:
    patient_id = 0
    def __init__(self):
        self.__patient_service = PatientService()


    def __make_new_patient(self, patient):
        (name, family, national_code, birth_date, phone_number) = patient.values()

        birth_date = jdatetime.datetime.strptime(birth_date, '%Y-%m-%d').date().togregorian()
        PatientController.patient_id += 1
        new_patient = Patient(PatientController.patient_id , name, family, national_code, birth_date, phone_number)

        return new_patient

    @Error_handler
    def save(self, patient_data):
        patient = self.__make_new_patient(patient_data)
        self.__patient_service.save_patient_data(patient)
        return f"patient {patient.name} {patient.family} saved successfully."

    @Error_handler
    def update(self, patient_data):
        patient = self.__make_new_patient(patient_data)
        self.__patient_service.update_patient_by_national_code(patient.national_code , patient)
        return f"patient with national code {patient.national_code} updated successfully."

    @Error_handler
    def delete(self, patient_data):
        patient = self.__make_new_patient(patient_data)
        self.__patient_service.delete_patient_by_national_code(patient.national_code)
        return f"patient with national code {patient.national_code} deleted successfully."


    @Error_handler
    def find_by_national_code(self, patient_data):
        patient = self.__make_new_patient(patient_data)
        self.__patient_service.get_patient_by_national_code(patient.national_code)
        return patient

    @Error_handler
    def find_all(self):
        patients = self.__patient_service.get_all_patients()
        return patients
