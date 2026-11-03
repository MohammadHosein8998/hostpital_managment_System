import jdatetime

from service.admin_service import AdminService
from model.admin import Admin
from utils.decorators import Error_handler


class AdminController:
    admin_id = 0

    def __init__(self):
        self.__admin_service = AdminService()

    def __make_new_admin(self, admin):
        (name, family, national_code, birth_date, user_name, password) = admin.values()

        birth_date = jdatetime.datetime.strptime(birth_date, '%Y-%m-%d').date().togregorian()
        AdminController.admin_id += 1
        new_admin = Admin(AdminController.admin_id, name, family, national_code, birth_date, user_name,
                          password)

        return new_admin

    @Error_handler
    def save(self, admin_data):
        admin = self.__make_new_admin(admin_data)
        self.__admin_service.save_admin_data(admin)
        return f"admin {admin.name} {admin.family} saved successfully."

    @Error_handler
    def update(self, admin_data):
        admin = self.__make_new_admin(admin_data)
        self.__admin_service.update_admin_by_national_code(admin.national_code, admin)
        return f"admin with national code {admin.national_code} updated successfully."

    @Error_handler
    def delete(self, admin_data):
        admin = self.__make_new_admin(admin_data)
        self.__admin_service.delete_admin_by_national_code(admin.national_code)
        return f"admin with national code {admin.national_code} deleted successfully."

    @Error_handler
    def find_by_national_code(self, admin_data):
        admin = self.__make_new_admin(admin_data)
        self.__admin_service.get_admin_by_national_code(admin.national_code)
        return admin

    @Error_handler
    def find_all(self):
        admins = self.__admin_service.get_all_admins()
        return admins

    @Error_handler
    def login(self, username: str, password: str):
        admin = self.__admin_service.get_admin_by_user_name(username)
        if not admin.login(password):
            raise ValueError(f"Invalid username or password!")
        return f"admin with user name {admin.user_name} login successfully."

    @Error_handler
    def find_admin_by_user_name(self , user_name):
        admin = self.__admin_service.get_admin_by_user_name(user_name)
        return admin