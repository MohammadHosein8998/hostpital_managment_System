from data_access.admin_data_managment import AdminDataManager
from model.admin import Admin


class AdminService:
    def __init__(self):
        self.__admin_data_access = AdminDataManager()

    def save_admin_data(self, admin_data: Admin):
        registered_admins = self.__admin_data_access.get_all_admins()
        is_exist = list(
            filter(lambda registered_admin: registered_admin.national_code == admin_data.national_code,
                   registered_admins))
        if is_exist:
            raise ValueError(f"admin with this national code : {admin_data.national_code} already registered")
        self.__admin_data_access.save_admin_data(admin_data)

    def get_all_admins(self):
        admins = self.__admin_data_access.get_all_admins()
        return admins

    def update_admin_by_national_code(self, national_code: str, admin_data: Admin):
        registered_admins = self.__admin_data_access.get_all_admins()
        is_exist = list(
            filter(lambda registered_admin: registered_admin.national_code == admin_data.national_code,
                   registered_admins))
        if len(is_exist) > 1:
            raise ValueError(f"admin with this national code : {admin_data.national_code} already registered")
        self.__admin_data_access.update_admin_by_national_code(national_code, admin_data)

    def delete_admin_by_national_code(self, national_code: str):
        self.__admin_data_access.delete_admin_by_national_code(national_code)

    def get_admin_by_national_code(self, national_code: str):
        admin = self.__admin_data_access.get_admin_by_national_code(national_code)
        return admin

    def get_admin_by_user_name(self, user_name: str):
        admin = self.__admin_data_access.get_admin_by_user_name(user_name)
        return admin