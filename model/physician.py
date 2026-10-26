from datetime import date

import jdatetime

from model.user import User


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
        self.__doctor_id = value

    @property
    def license(self):
        return self.__license

    @license.setter
    def license(self, value):
        self.__license = value


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