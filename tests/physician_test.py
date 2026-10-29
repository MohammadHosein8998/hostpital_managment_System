from datetime import date
from persian_tools import national_id
from controller.physician_controller import PhysicianController
from data_access.physician_data_managment import PhysicianDatAccess
from model.physician import Physician
from service.physician_service import PhysicianService

#####################################
#       physician model             #
#####################################

doctor_1 = Physician(1, "mohammad hosein", "ghasemi", "0022613013"
                     , date(2025, 5, 14), "123")

doctor_2 = Physician(2, "ali", "mahdavi", "0022613013"
                     , date(2025, 5, 14), "45684")

print(doctor_1)

print(doctor_2)

#####################################
#       physician data access       #
#####################################

physician_da = PhysicianDatAccess()

physician_da.save_physician_data(doctor_1)
physician_da.save_physician_data(doctor_2)

print(physician_da.get_all_physicians())

doctor_1_updated = Physician(100, "ali", "hassani", "0022613013", date(2011, 6, 10), "356846")
physician_da.update_physician_by_national_code(doctor_1.national_code, doctor_1_updated)

print("ff", physician_da.get_physician_by_national_code(doctor_1.national_code))
print("ddd", physician_da.get_all_physicians())

#####################################
#       physician services          #
#####################################

physician_da.clear_data()
print("physician database is cleared")

physician_ser = PhysicianService()

physician_ser.save(doctor_1)
# physician_ser.save(doctor_2)

print(physician_ser.get_all_physicians())

doctor_1_updated = Physician(201, "naghi", "alavi", "0022613013", date(2011, 6, 10), "356846")
physician_ser.update_physician_by_national_code(doctor_1.national_code, doctor_1_updated)

print("services get one", physician_ser.get_physician_by_national_code(doctor_1.national_code))
print("services get all", physician_ser.get_all_physicians())

#####################################
#       physician controller        #
#####################################

physician_da.clear_data()

physician_controller = PhysicianController()

doctor_data_1 = { "name": "mohammad hosein", "family": "ghasemi", "national_code": national_id.generate_random()
    , "birth_date": "1378-8-5", "license": "123"}

print(physician_controller.save(doctor_data_1))

print(physician_controller.get_all_physician())


doctor_data_1["name"] = "hassan"

print(physician_controller.update(doctor_data_1))

print(physician_controller.get_all_physician())
