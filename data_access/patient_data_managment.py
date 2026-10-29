import os
import pickle
from dataclasses import field

from model.patient import Patient
from model.user import User


class PatientDataAccess:
    def __init__(self):
        self.file_name = "patients.data"
        if os.path.exists(self.file_name):
            file = open(self.file_name , "rb")
            self.__patient_list = pickle.load(file)
            file.close()
        else:
            file = open(self.file_name, "wb")
            pickle.dump([] , file)
            file.close()
            self.__patient_list =[]

    def clear_data(self):
        file = open(self.file_name, "wb")
        pickle.dump([] , file)
        file.close()

    def save_patient_data(self, patient_data : Patient):
        self.__patient_list.append(patient_data)
        file = open(self.file_name , "wb")
        pickle.dump(self.__patient_list , file)
        file.close()

    def delete_patient_by_national_code(self , national_code : str):
        file = open(self.file_name, "rb")
        self.__patient_list = pickle.load(file)
        file.close()
        self.__patient_list = list(filter(lambda patient : patient.national_code != national_code, self.__patient_list))
        file = open(self.file_name, "wb")
        pickle.dump(self.__patient_list, file)
        file.close()

    def update_patient_by_national_code(self, national_code: str , patient_data : Patient):
        file = open(self.file_name, "rb")
        self.__patient_list = pickle.load(file)
        file.close()
        self.__patient_list = list(filter(lambda patient: patient.national_code != national_code, self.__patient_list))
        self.__patient_list.append(patient_data)
        file = open(self.file_name, "wb")
        pickle.dump(self.__patient_list, file)
        file.close()

    def get_all_patients(self):
        file = open(self.file_name , "rb")
        self.__patient_list = pickle.load(file)
        file.close()
        return self.__patient_list

    def get_patient_by_national_code(self , national_code):
        file = open(self.file_name, "rb")
        self.__patient_list = pickle.load(file)
        file.close()
        patient = list(filter( lambda x : x.national_code == national_code, self.__patient_list))
        return patient[0]
