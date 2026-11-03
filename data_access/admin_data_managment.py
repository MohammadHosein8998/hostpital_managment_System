import os
import pickle
from model.admin import Admin


class AdminDataManager:

    def __init__(self):
        self.file_name = "admins.data"
        if os.path.exists(self.file_name):
            file = open(self.file_name, "rb")
            self.__admin_list = pickle.load(file)
            file.close()
        else:
            file = open(self.file_name, "wb")
            pickle.dump([], file)
            file.close()
            self.__admin_list = []

    def clear_data(self):
        file = open(self.file_name, "wb")
        pickle.dump([], file)
        file.close()

    def save_admin_data(self, admin_data: Admin):
        self.__admin_list.append(admin_data)
        file = open(self.file_name, "wb")
        pickle.dump(self.__admin_list, file)
        file.close()

    def delete_admin_by_national_code(self, national_code: str):
        file = open(self.file_name, "rb")
        self.__admin_list = pickle.load(file)
        file.close()
        self.__admin_list = list(filter(lambda admin: admin.national_code != national_code, self.__admin_list))
        file = open(self.file_name, "wb")
        pickle.dump(self.__admin_list, file)
        file.close()

    def update_admin_by_national_code(self, national_code: str, admin_data: Admin):
        file = open(self.file_name, "rb")
        self.__admin_list = pickle.load(file)
        file.close()
        self.__admin_list = list(filter(lambda admin: admin.national_code != national_code, self.__admin_list))
        self.__admin_list.append(admin_data)
        file = open(self.file_name, "wb")
        pickle.dump(self.__admin_list, file)
        file.close()

    def get_all_admins(self):
        file = open(self.file_name, "rb")
        self.__admin_list = pickle.load(file)
        file.close()
        return self.__admin_list

    def get_admin_by_national_code(self, national_code):
        file = open(self.file_name, "rb")
        self.__admin_list = pickle.load(file)
        file.close()
        admin = list(filter(lambda x: x.national_code == national_code, self.__admin_list))
        if not admin:
            raise ValueError("there is no admin with this national code in database")
        return admin[0]


    def get_admin_by_user_name(self, user_name):
        file = open(self.file_name, "rb")
        self.__admin_list = pickle.load(file)
        file.close()
        admin = list(filter(lambda x: x.user_name == user_name, self.__admin_list))
        if not admin:
            raise ValueError("there is no admin with this user name in database")
        return admin[0]