import jdatetime


from service.appointment_service import AppointmentService
from model.appointment import Appointment
from utils.decorators import Error_handler


class AppointmentController:
    appointment_id = 0

    def __init__(self):
        self.__appointment_service = AppointmentService()

    def __make_new_appointment(self, appointment)-> Appointment:
        ( physician_id , patient_id , date , time) = appointment.values()

        milady_date = jdatetime.datetime.strptime(date, '%Y-%m-%d').date().togregorian()
        AppointmentController.appointment_id += 1
        miladay_time = jdatetime.time.strptime(time , "%H:%M:%S")
        new_appointment = Appointment(AppointmentController.appointment_id, int(physician_id), int(patient_id), milady_date, miladay_time)

        return new_appointment

    @Error_handler
    def save(self, appointment_data):
        appointment = self.__make_new_appointment(appointment_data)
        self.__appointment_service.save(appointment)
        return f"appointment {appointment.appointment_id} saved successfully."

    @Error_handler
    def update(self, appointment_id , appointment_data):
        appointment = self.__make_new_appointment(appointment_data)
        self.__appointment_service.update_appointment_by_appointment_id(int(appointment_id), appointment)
        return f"appointment with appointment id {appointment_id} updated successfully."

    @Error_handler
    def delete(self,appointment_id):
        self.__appointment_service.delete_appointment_by_appointment_id(int(appointment_id))
        return f"appointment with national code {appointment_id} deleted successfully."

    @Error_handler
    def find_by_appointment_id(self, appointment_data):
        appointment = self.__make_new_appointment(appointment_data)
        self.__appointment_service.get_appointment_by_appointment_id(appointment.appointment_id)
        return appointment

    @Error_handler
    def find_all(self):
        appointments = self.__appointment_service.get_all_appointments()
        return appointments