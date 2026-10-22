from datetime import date
from persian_tools import phone_number , national_id

from model.user import User
from validation.patient_validation import PatientValidation


class Patient(User):
    samples = [
        {
            "patient_id": 1,
            "name": "mohammad hosein",
            "family": "ghasemi",
            "national_code": "0022613013",
            "birth_date": date(2000, 10, 8),
            "phone_number": "09026464308"
        },
        {
            "patient_id": 2,
            "name": "ali",
            "family": "ahmadi",
            "national_code": national_id.generate_random(),
            "birth_date": date(1998, 5, 12),
            "phone_number": "09126008947"
        },
        {
            "patient_id": 3,
            "name": "reza",
            "family": "karimi",
            "national_code": national_id.generate_random(),
            "birth_date": date(1995, 3, 21),
            "phone_number": "09123456782"
        },
        {
            "patient_id": 4,
            "name": "sara",
            "family": "mohammadi",
            "national_code": national_id.generate_random(),
            "birth_date": date(2002, 7, 15),
            "phone_number": "09123456783"
        },
        {
            "patient_id": 5,
            "name": "amir",
            "family": "hosseini",
            "national_code": national_id.generate_random(),
            "birth_date": date(1999, 1, 30),
            "phone_number": "09123456784"
        },
        {
            "patient_id": 6,
            "name": "fatemeh",
            "family": "rezaei",
            "national_code": national_id.generate_random(),
            "birth_date": date(2001, 11, 4),
            "phone_number": "09123456785"
        },
        {
            "patient_id": 7,
            "name": "hossein",
            "family": "moradi",
            "national_code":national_id.generate_random(),
            "birth_date": date(1997, 9, 18),
            "phone_number": "09123456786"
        },
        {
            "patient_id": 8,
            "name": "maryam",
            "family": "jafari",
            "national_code": national_id.generate_random(),
            "birth_date": date(2003, 2, 25),
            "phone_number": "09123456787"
        },
        {
            "patient_id": 9,
            "name": "mohsen",
            "family": "kazemi",
            "national_code": national_id.generate_random(),
            "birth_date": date(1996, 6, 9),
            "phone_number": "09123456788"
        },
        {
            "patient_id": 10,
            "name": "zahra",
            "family": "akbari",
            "national_code": national_id.generate_random(),
            "birth_date": date(2000, 12, 17),
            "phone_number": "09123456789"
        }
    ]

    def __init__(self, patient_id, name, family, national_code, birth_date, phone_number):
        super().__init__(name, family, national_code, birth_date)
        self.patient_id = patient_id
        self.phone_number = phone_number

    @property
    def patient_id(self):
        return self.__patient_id

    @patient_id.setter
    def patient_id(self, value):
        self.__patient_id = value

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        PatientValidation.validate_phone_number(value)
        self.__phone_number = value

    def __repr__(self) -> str:
        return f"Patient( patient_id : {self.patient_id} , phone_number : {self.phone_number} , name : {self.name}, family : {self.family}, national_code : {self.national_code} , birth_date : {self.birth_date} )"

    def enableUser(self):
        print(f"user {self.name} enabled")

    def disableUser(self):
        print(f"user {self.name} disabled")

    def __eq__(self, other: Patient) -> bool:
        if not isinstance(other, Patient):
            return NotImplemented

        return (
                self.patient_id == other.patient_id
                and self.name == other.name
                and self.family == other.family
                and self.national_code == other.national_code
                and self.birth_date == other.birth_date
                and self.phone_number == other.phone_number
        )

    @classmethod
    def make_sample(cls , dic_sample = None):
        if dic_sample is None:
            return cls(1, "mohammad hosein", "ghasemi", "0022613013", date(2020, 5, 8), "09026464308")
        else:
            return cls(dic_sample["patient_id"] , dic_sample["name"] , dic_sample["family"] , dic_sample["national_code"] , dic_sample["birth_date"] , dic_sample["phone_number"])

    @classmethod
    def make_samples(cls):
        cls_samples = list(map( cls.make_sample, cls.samples))
        return cls_samples
