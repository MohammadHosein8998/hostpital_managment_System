from model.admission import Admission
from model.medicine import Medicine


class SubPrescription:

    def __init__(self , sub_prescription_id , prescription_id , medicine: Medicine , admission : Admission  ):
        self.sub_prescription_id = sub_prescription_id
        self.prescription_id = prescription_id
        self.medicine = medicine
        self.admission = admission

    def findings(self , findings):
        self.findings = findings
