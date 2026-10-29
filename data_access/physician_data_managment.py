import os
import pickle

from model.physician import Physician


class PhysicianDatAccess:
    def __init__(self):
        self.file_name = "physician.data"
        if os.path.exists(self.file_name):
            file = open(self.file_name , "rb")
            self.__physician_list = pickle.load(file)
            file.close()
        else:
            file = open(self.file_name, "wb")
            pickle.dump([] , file)
            file.close()
            self.__physician_list =[]


    def clear_data(self):
        file = open(self.file_name, "wb")
        pickle.dump([] , file)
        file.close()
        self.__physician_list = []

    def save_physician_data(self, physician_data : Physician):
        self.__physician_list.append(physician_data)
        file = open(self.file_name , "wb")
        pickle.dump(self.__physician_list , file)
        file.close()

    def delete_physician_by_national_code(self , national_code : str):
        file = open(self.file_name, "rb")
        self.__physician_list = pickle.load(file)
        file.close()
        self.__physician_list = list(filter(lambda physician : physician.national_code != national_code, self.__physician_list))
        file = open(self.file_name, "wb")
        pickle.dump(self.__physician_list, file)
        file.close()

    def update_physician_by_national_code(self, national_code: str , physician_data : Physician):
        file = open(self.file_name, "rb")
        self.__physician_list = pickle.load(file)
        file.close()
        self.__physician_list = list(filter(lambda physician: physician.national_code != national_code, self.__physician_list))
        self.__physician_list.append(physician_data)
        file = open(self.file_name, "wb")
        pickle.dump(self.__physician_list, file)
        file.close()

    def get_all_physicians(self):
        file = open(self.file_name , "rb")
        self.__physician_list = pickle.load(file)
        file.close()
        return self.__physician_list

    def get_physician_by_national_code(self , national_code):
        file = open(self.file_name, "rb")
        self.__physician_list = pickle.load(file)
        file.close()
        physician = list(filter( lambda x : x.national_code == national_code, self.__physician_list))
        return physician[0]
