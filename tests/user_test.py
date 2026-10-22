from datetime import date, datetime

from persian_tools import national_id

from model.user import User

########################################
#           user model test            #
########################################

date_time_1 = datetime(2020, 5, 8)

date_time_2 = datetime(2030, 5, 8)

national_code_1 = national_id.generate_random()

national_code_2 = national_id.generate_random()

user_1 = User("moahammad hosein", "Ghasemi", national_code_1, date_time_1)

user_2 = User("ali", "hassani", national_code_2, date_time_1)

print(user_1)
print(user_1.national_code)

print(user_2)

########################################
#           user database test         #
########################################


########################################
#           user service test          #
########################################


########################################
#           user controller test       #
########################################
