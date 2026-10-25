import time
import unittest
from random import sample

from data_access import patient_data_managment
from model import patient
from model.patient import Patient
from datetime import date, datetime

from service.patient_service import PatientService
from data_access.patient_data_managment import PatientDataAccess


############################################
#           patient model test             #
############################################


class TestPatient(unittest.TestCase):

    def setUp(self):
        self.patient = Patient(
            1,
            "mohammad hosein",
            "ghasemi",
            "0022613013",
            datetime(2020, 5, 8),
            "09026464308"
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.patient_id, 1)
        self.assertEqual(self.patient.name, "mohammad hosein", "these two name attributes are not equal")
        self.assertEqual(self.patient.family, "ghasemi")
        self.assertEqual(self.patient.national_code, "0022613013")
        self.assertEqual(self.patient.phone_number, "09026464308")

    def test_patient_birth_date(self):
        self.assertEqual(
            self.patient.birth_date,
            datetime(2020, 5, 8)
        )


############################################
#           patient data access test       #
############################################

class TestPatientDataAccess(unittest.TestCase):
    def setUp(self):
        self.patient_data_access = PatientDataAccess()

        self.sample = Patient.make_sample()

        self.samples = Patient.make_samples()

    def tearDown(self):
        self.patient_data_access.clear_data()

    def test_save_patient(self):
        self.patient_data_access.save_patient_data(self.sample)

        patient = self.patient_data_access.get_patient_by_national_code("0022613013")

        self.assertEqual(self.sample, patient)

    def test_save_and_get_all_patients(self):
        for sample in self.samples:
            self.patient_data_access.save_patient_data(sample)

        patients = self.patient_data_access.get_all_patients()

        self.assertListEqual(self.samples, patients)

    def test_save_and_update_patient(self):
        self.patient_data_access.save_patient_data(self.sample)
        updated_patient = Patient(1, "mohammad hosein", "ghasemi", "0022613013", datetime(2015, 1, 1), "09197267263")
        self.patient_data_access.update_patient_by_national_code("0022613013", updated_patient)

    def test_save_and_delete_patient(self):
        for sample in self.samples:
            self.patient_data_access.save_patient_data(sample)

        patients = self.patient_data_access.get_all_patients()

        self.patient_data_access.delete_patient_by_national_code("0022613013")

        self.assertNotIn(self.sample, patients)


############################################
#           patient service test           #
############################################

class TestPatientService(unittest.TestCase):
    def setUp(self):
        self.patient_service = PatientService()

        self.sample = Patient.make_sample()

        self.samples = Patient.make_samples()

    def tearDown(self) -> None:
        self.patient_data_access = PatientDataAccess()
        self.patient_data_access.clear_data()

    def test_save_patient(self):
        self.patient_service.save_patient_data(self.sample)

    def test_save_and_get_all_patients(self):
        for patient in self.samples:
            self.patient_service.save_patient_data(patient)

        patients = self.patient_service.get_all_patients()

        self.assertListEqual(self.samples, patients)

    def test_save_and_update_patient(self):
        for patient in self.samples:
            self.patient_service.save_patient_data(patient)

        updated_patient = Patient(1, "mohammad hosein", "ghasemi", "0022613013", datetime(2015, 1, 1), "09197267263")

        self.patient_service.update_patient_by_national_code("0022613013" , updated_patient)

    def test_save_and_delete(self):

        self.patient_service.save_patient_data(self.sample)

        patient = self.patient_service.get_patient_by_national_code(self.sample.national_code)

        self.assertEqual(self.sample, patient)


############################################
#           patient controller test        #
############################################


class TestPatientController(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == "__main__":
    unittest.main()
