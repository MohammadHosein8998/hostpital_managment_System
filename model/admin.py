class Admin:
    def __init__(self, admin_id, name, age, user_name, password):
        self.admin_id = admin_id
        self.name = name
        self.age = age
        self.user_name = user_name
        self.password = password

    def create(self):
        print("Admin created")

    def update(self):
        print("Admin updated")
