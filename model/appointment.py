from datetime import date, time

import jdatetime

from validation.appointment_validation import AppointmentValidation


class Appointment:
    def __init__(self, appointment_id: int, physician_id: int, patient_id: int, appointment_date: date,
                 appointment_time: time):
        self.appointment_id = appointment_id
        self.physician_id = physician_id
        self.patient_id = patient_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time

    @property
    def appointment_id(self):
        return self.__appointment_id

    @appointment_id.setter
    def appointment_id(self, value):
        AppointmentValidation.appointment_id(value)
        self.__appointment_id = value

    @property
    def physician_id(self):
        return self.__physician_id

    @physician_id.setter
    def physician_id(self, value):
        AppointmentValidation.physician_id(value)
        self.__physician_id = value

    @property
    def patient_id(self):
        return self.__patient_id

    @patient_id.setter
    def patient_id(self, value):
        AppointmentValidation.patient_id(value)
        self.__patient_id = value

    @property
    def appointment_date(self):
        return self.__appointment_date

    @appointment_date.setter
    def appointment_date(self, value):
        AppointmentValidation.appointment_date(value)
        self.__appointment_date = value

    @property
    def appointment_time(self):
        return self.__appointment_time

    @appointment_time.setter
    def appointment_time(self, value):
        AppointmentValidation.appointment_time(value)
        self.__appointment_time = value


    def __repr__(self) -> str:
        return f"Appointment( appointment_id: {self.appointment_id} , physician_id: {self.physician_id}, patient_id: {self.patient_id}, appointment_date: {self.appointment_date} , appointment_time: {self.appointment_time})"




    def values(self):

        persian_appointment_date = jdatetime.datetime.fromgregorian(date=self.appointment_date)

        string_appointment_date = jdatetime.datetime.strftime(persian_appointment_date , "%Y-%m-%d")

        string_appointment_time = jdatetime.time.strftime(self.appointment_time , "%H:%M:%S")

        return (
            self.appointment_id,
            self.physician_id,
            self.patient_id,
             string_appointment_date,
            string_appointment_time
        )