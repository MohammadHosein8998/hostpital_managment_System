from tkinter import ttk

from controller.patient_controller import PatientController
from model.view import View
from views import patient_view


class PatientInfoView(View):
    attributes = ["name", "family", "national_code", "birth_date", "phone_number", "password"]


    def reset_form(self):
        super().reset_form()



    def select_patient(self , patient):
        patient_list = list(patient.values())
        patient_list.pop(0)
        self.set_selected_values(patient_list)

    def edit_patient(self) -> None:
        patient = self.get_res_dic()
        success, response = self.patient_c.update(patient)
        self.show_message_box(success, response)
        success , patient = self.patient_c.find_by_national_code(patient["national_code"])
        if success:
            self.controller.current_user = patient

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.patient_c = PatientController()

        ttk.Label(
            self,
            text="patient profile",
            font=("Arial", 18, "bold")
        ).place(x=10, y=10)

        #  my Label drawing
        for component in list(enumerate(self.attributes)):
            self.draw_str_input(text=component[1], x=20, y=int((component[0] + 1.5) * 40))

        ttk.Button(
            self,
            text="Back to Dashboard",
            command=lambda: controller.show_frame("PatientDashboardView")
        ).place(x=10, y=350)

        self.draw_button(text="edit", x=20, y=300, command=self.edit_patient)

    def on_show(self):
        patient = self.controller.current_user
        if patient:
            self.select_patient(patient)