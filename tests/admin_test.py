from datetime import date, datetime

from data_access.admin_data_managment import AdminDataManager
from model.admin import Admin
import re

from service.admin_service import AdminService

############################################
#             Admin model test             #
############################################


birth_date = datetime(2002, 8, 12)
birth_date_2 = datetime(2014, 10, 20)

admin_1 = Admin(1, "mohammad hosein", "ghasemi", "0022613013"
                , birth_date, "Admin", "123456")

admin_2 = Admin(1, "ali", "asghare", "0022613013", birth_date_2, "hassan@sabzali.com", "aliHassan1234")

print(admin_1)

print(admin_2)

############################################
#         Admin Data Access test           #
############################################

admin_data_access = AdminDataManager()

admin_data_access.save_admin_data(admin_1)
admin_data_access.save_admin_data(admin_2)

print(admin_data_access.get_all_admins())

print(admin_data_access.get_admin_by_national_code("0022613013"))

admin_data_access.clear_data()

admin_data_access.save_admin_data(admin_1)

print(admin_data_access.update_admin_by_national_code("0022613013", admin_2))

print(admin_data_access.get_admin_by_national_code("0022613013"))

############################################
#             Admin service test           #
############################################

admin_data_access.clear_data()

admin_service = AdminService()
admin_service.save_admin_data(admin_1)

admin_service.get_admin_by_national_code("0022613013")


print(admin_service.get_all_admins())


admin_data_access.clear_data()
admin_service.save_admin_data(admin_1)