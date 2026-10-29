from datetime import date

import jdatetime

from model.user import User
from validation import physician_validation
from validation.physician_validation import PhysicianValidation


class Physician(User):

    def __init__(self, doctor_id, name, family, national_code, birth_date: date, license: str):
        super().__init__(name, family, national_code, birth_date)
        self.doctor_id = doctor_id
        self.license = license

    @property
    def doctor_id(self):
        return self.__doctor_id

    @doctor_id.setter
    def doctor_id(self, value):
        PhysicianValidation.doctor_id(value)
        self.__doctor_id = value

    @property
    def license(self):
        return self.__license

    @license.setter
    def license(self, value):
        PhysicianValidation.license_number(value)
        self.__license = value


    def __repr__(self) -> str:
        return f"Physician({self.doctor_id} , {self.name} , {self.family} , {self.national_code} , {self.birth_date} , {self.license})"

    def values(self):

        persian_birth_date = jdatetime.datetime.fromgregorian(date=self.birth_date)

        string_date_persian = jdatetime.datetime.strftime(persian_birth_date , "%Y-%m-%d")


        return (
            self.doctor_id,
            self.name,
            self.family,
            self.national_code,
            string_date_persian,
            self.license
        )