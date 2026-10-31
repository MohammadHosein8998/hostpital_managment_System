from datetime import date , datetime  ,time
# from datetime import time
from model.appointment import Appointment

############################################
#       appointment model test             #
############################################


meeting_date = datetime(2020 , 8 , 9)

meeting_time = time(10 , 30 , 45)

appointment_1 = Appointment(1 , 1 ,1 , meeting_date , meeting_time)

