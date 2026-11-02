from datetime import date, datetime, time

from data_access.appointment_data_managment import AppointmentDataAccess
# from datetime import time
from model.appointment import Appointment
from service.appointment_service import AppointmentService

############################################
#       appointment model test             #
############################################


meeting_date = datetime(2020, 8, 9)

meeting_date_1 = datetime(2015, 10, 1)

meeting_time = time(10, 30, 45)

meeting_time_1 = time(8, 23, 10)

appointment_1 = Appointment(1, 1, 1, meeting_date, meeting_time)

appointment_2 = Appointment(2, 2, 4, meeting_date_1, meeting_time_1)

print(appointment_1)

print(appointment_2)

############################################
#       appointment data access test       #
############################################

appointment_data_managment = AppointmentDataAccess()

appointment_data_managment.clear_data()

appointment_data_managment.save_appointment_data(appointment_1)

print(appointment_data_managment.get_all_appointments())

updated_meeting_time = time(12, 30, 45)

updated_appointment_1 = Appointment(1, 13, 10, meeting_date, updated_meeting_time)

appointment_data_managment.update_appointment_by_appointment_id(1, updated_appointment_1)

print(appointment_data_managment.get_all_appointments())

print(appointment_data_managment.get_appointment_by_appointment_id(1))

appointment_data_managment.delete_appointment_by_appointment_id(1)

print(appointment_data_managment.get_all_appointments())

############################################
#       appointment service test           #
############################################

appointment_data_managment.clear_data()

appointment_service = AppointmentService()

appointment_service.save(appointment_1)

print(appointment_service.get_all_appointments())

appointment_service.update_appointment_by_appointment_id(1,updated_appointment_1)

print(appointment_service.get_all_appointments())

print(appointment_service.get_appointment_by_appointment_id(1))


