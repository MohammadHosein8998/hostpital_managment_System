from model.admin import Admin
from model.medicine import Medicine


class Physician(Admin):

    def __init__(self,  admin_id, name, age, user_name, password , license: str):
        super().__init__(admin_id, name, age, user_name, password)
        self.license = license


    def add(self ,medicine : Medicine):
        print("add to physician")
        print(f"medicine : {medicine.name}")

    def update(self):
        print("update in  physician")