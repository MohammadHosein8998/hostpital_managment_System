from model.admin import Admin

class Patient(Admin):
    def __init__(self, category, admin_id, name, age, user_name, password):
        super().__init__(admin_id, name, age, user_name, password)
        self.category = category

    def enableUser(self):
        print(f"user {self.name} enabled")

    def disableUser(self):
        print(f"user {self.name} disabled")