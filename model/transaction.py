from model.patient import Patient
from model.physician import Physician


class Transaction:
    def __init__(self , transaction_id , details , date):
        self.transaction_id = transaction_id
        self.details = details
        self.date = date

    def update(self , physician:Physician , patient : Patient):
        print("update in Transaction")
        print(f"update physician id : {physician.admin_id} , name : {physician.name}")
        print(f"update patient id : {patient.admin_id} , name : {patient.name}")