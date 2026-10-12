from typing import List, Tuple

from model.admission import Admission
from model.medicine import Medicine


class Prescription:
    def __init__(self, prescription_id, name:Medicine, details: Admission, date):
        self.prescription_id = prescription_id
        self.name = name
        self.details = details
        self.date = date

    def add(self):
        print("Prescription added")


    def update(self):
        print("Prescription update")

    def __repr__(self) -> str:
        return f"Prescription({self.prescription_id}, {self.name}, {self.details}, {self.date})"