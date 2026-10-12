

class Admission:
    def __init__(self , admission_id , date , patient_name , findings):
        self.admission_id = admission_id
        self.date = date
        self.patient_name = patient_name
        self.findings = findings

    def update(self):
        print("Update Admission")

    def __repr__(self) -> str:
        return f"{self.admission_id} {self.patient_name} {self.findings}"
