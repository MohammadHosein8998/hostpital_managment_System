

class Medicine:

    def __init__(self, medicine_id , name , description , price , datedue):
        self.medicine_id = medicine_id
        self.name = name
        self.description = description
        self.price = price
        self.datedue = datedue

    def add(self):
        print("adding medicine")
    def update(self):
        print("updating medicine")

    def __repr__(self) -> str:
        return f"{self.medicine_id} {self.name} {self.description} {self.price} {self.datedue}"