from data_access.appointment_data_managment import AppointmentDataAccess
from model.appointment import Appointment

class AppointmentService:

    def __init__(self):
        self.__appointment_data_access = AppointmentDataAccess()

    def save(self, appointment_data):
        registered_appointments = self.__appointment_data_access.get_all_appointments()
        is_exist = list(
            filter(lambda registered_patient: registered_patient.national_code == appointment_data.national_code,
                   registered_appointments))
        if is_exist:
            raise ValueError(f"appointment with this id : {appointment_data.appointment_id} already saved")
        self.__appointment_data_access.save_appointment_data(appointment_data)

    def get_all_appointments(self):
        appointments = self.__appointment_data_access.get_all_appointments()
        return appointments

    def update_appointment_by_appointment_id(self, appointment_id: int, appointment_data: Appointment):
        save_appointments = self.__appointment_data_access.get_all_appointments()
        is_exist = list(
            filter(lambda save_appointment: save_appointment.appointment_id == appointment_data.appointment_id,
                   save_appointments))
        if len(is_exist) > 1:
            raise ValueError(f"appointment with this is : {appointment_data.appointment_id} already saved")
        self.__appointment_data_access.update_appointment_by_appointment_id(appointment_id, appointment_data)
