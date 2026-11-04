from tkinter import ttk

from controller.patient_controller import PatientController
from model.patient import Patient
from model.view import View


class SignUpView(View):
    attributes = ["name", "family", "national_code", "birth_date", "phone_number" , "password"]

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.patient_c = PatientController()

        ttk.Label(self,
                  text="Patient Sign Up",
                  font=("Arial", 18, "bold")
                  ).place(x=10, y=20)

        #  my Label drawing
        for component in list(enumerate(self.attributes)):
            self.draw_str_input(text=component[1], x=20, y=int((component[0] + 1.5) * 40))


        self.draw_button(text="sign up", x=20, y=300, command=self.__sign_up)

        self.draw_button(text="back", x=90, y=300, command=self.__back)

        self.reset_form()

    def __sign_up(self):
        patient = self.get_res_dic()
        success , message = self.patient_c.save(patient)
        if success:
            self.reset_form()
            self.controller.show_frame("PatientLoginView")
        self.show_message_box(success , message)

    def __back(self):
        self.controller.show_frame("PatientLoginView")