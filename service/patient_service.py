from data_access.patient_data_managment import PatientDataAccess
from model.patient import Patient


class PatientService:
    def __init__(self):
        self.__patient_data_access = PatientDataAccess()

    def save_patient_data(self, patient_data: Patient):
        registered_patients = self.__patient_data_access.get_all_patients()
        is_exist = list(
            filter(lambda registered_patient: registered_patient.national_code == patient_data.national_code,
                   registered_patients))
        if is_exist:
            raise ValueError(f"patient with this national code : {patient_data.national_code}already registered")
        self.__patient_data_access.save_patient_data(patient_data)

    def get_all_patients(self):
        patients = self.__patient_data_access.get_all_patients()
        return patients

    def update_patient_by_national_code(self, national_code: str, patient_data: Patient):
        registered_patients = self.__patient_data_access.get_all_patients()
        is_exist = list(
            filter(lambda registered_patient: registered_patient.national_code == patient_data.national_code,
                   registered_patients))
        if len(is_exist) > 1:
            raise ValueError(f"patient with this national code : {patient_data.national_code} already registered")
        self.__patient_data_access.update_patient_by_national_code(national_code, patient_data)

    def delete_patient_by_national_code(self, national_code: str):
        self.__patient_data_access.delete_patient_by_national_code(national_code)

    def get_patient_by_national_code(self, national_code: str):
        patient = self.__patient_data_access.get_patient_by_national_code(national_code)
        return patient
