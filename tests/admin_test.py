
from model.admission import Admission
from model.medicine import Medicine
from model.patient import Patient
from model.prescription import Prescription
from model.transaction import Transaction
from model.physician import Physician

patient_1 = Patient("eye" ,"123654" , "ali" , 15 , "ali998" , "sdf445")
patient_2 = Patient("bones","3435435" , "mohammd" , 15 , "moh8998" , "sff2342")
patient_3 = Patient("ears","4796557" , "hassan" , 15 , "hassan324" , "sdfsf53")
patient_4 = Patient("skin","2424532" , "hosein" , 15 , "hosein346" , "sdfs434")

doctor_1 = Physician("00224654", "mohmmad hosein", "25", "mo85", "moh12346" , "MIT")


transaction_1 = Transaction(1,"this is transaction","1405-6-1")

transaction_1.update(doctor_1 , patient_1)

drug_1 = Medicine("13322" , "neotadin" , "good for alergi" , "$5" , "1407-6-12")

drug_1_admission = Admission( "123546" , "1405-7-8" , "ali" , "drink it with water 2 hours after lunch everyday")

prescription = Prescription("134188" , drug_1 , drug_1_admission , "1407-6-12")

print(prescription)
