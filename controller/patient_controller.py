from model import patient
from service.patient_service import PatientService
from model.patient import Patient

class PatientController:
    def __init__(self):
        self.__patient_service = PatientService()


    def save(self , name , family , age , patient_id):
        try:

            patient = Patient()
            self.__patient_service.save_patient_data()
        except Exception as e:
            return False , e
