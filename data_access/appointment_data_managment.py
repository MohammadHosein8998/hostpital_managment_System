import os
import pickle

from model.appointment import Appointment


class AppointmentDataAccess:
    def __init__(self):
        self.file_name = "appointments.data"
        if os.path.exists(self.file_name):
            file = open(self.file_name, "rb")
            self.__appointment_list = pickle.load(file)
            file.close()
        else:
            file = open(self.file_name, "wb")
            pickle.dump([], file)
            file.close()
            self.__appointment_list = []

    def clear_data(self):
        file = open(self.file_name, "wb")
        pickle.dump([], file)
        file.close()
        self.__appointment_list = []

    def save_appointment_data(self, appointment_data: Appointment):
        self.__appointment_list.append(appointment_data)
        file = open(self.file_name, "wb")
        pickle.dump(self.__appointment_list, file)
        file.close()

    def delete_appointment_by_appointment_id(self, appointment_id: int):
        file = open(self.file_name, "rb")
        self.__appointment_list = pickle.load(file)
        file.close()
        self.__appointment_list = list(
            filter(lambda appointment: appointment.appointment_id != appointment_id, self.__appointment_list))
        file = open(self.file_name, "wb")
        pickle.dump(self.__appointment_list, file)
        file.close()

    def update_appointment_by_appointment_id(self, appointment_id: int, appointment_data: Appointment):
        file = open(self.file_name, "rb")
        self.__appointment_list = pickle.load(file)
        file.close()
        self.__appointment_list = list(
            filter(lambda appointment: appointment.appointment_id != appointment_id, self.__appointment_list))
        self.__appointment_list.append(appointment_data)
        file = open(self.file_name, "wb")
        pickle.dump(self.__appointment_list, file)
        file.close()

    def get_all_appointments(self):
        file = open(self.file_name, "rb")
        self.__appointment_list = pickle.load(file)
        file.close()
        return self.__appointment_list

    def get_appointment_by_appointment_id(self, appointment_id: int):
        file = open(self.file_name, "rb")
        self.__appointment_list = pickle.load(file)
        file.close()
        appointment = list(filter(lambda x: x.appointment_id == appointment_id, self.__appointment_list))
        return appointment[0]
