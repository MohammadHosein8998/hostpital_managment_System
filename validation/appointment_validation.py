import re
from datetime import date, time


class AppointmentValidation:

    @staticmethod
    def appointment_id(value):
        if not isinstance(value, int) :
            raise ValueError("appointment id must be a integer")

    @staticmethod
    def physician_id(value):
        if not isinstance(value, int) :
            raise ValueError("physician id must be a integer")

    @staticmethod
    def patient_id(value):
        if not isinstance(value, int) :
            raise ValueError("patient id must be a integer")

    @staticmethod
    def appointment_date(value):
        if not isinstance(value, date):
            raise ValueError("appointment date must be a date")

    @staticmethod
    def appointment_time(value):
        if not isinstance(value, time):
            raise ValueError("appointment time must be a time")
