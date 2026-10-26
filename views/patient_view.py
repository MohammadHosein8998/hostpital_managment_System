from tkinter import ttk
from tkinter import END

from controller import patient_controller
from controller.patient_controller import PatientController
from model.view import View


class PatientView(View):
    attributes = ["name", "family", "national_code", "birth_date", "phone_number"]
    heading_list = ["patient_id", "name", "family", "national_code", "birth_date", "phone_number"]

    def reset_form(self):
        super().reset_form()
        self.show_data_on_the_table()

    def show_data_on_the_table(self):
        success, patient_list = self.patient_c.find_all()

        if success:
            for item in self.patient_table.get_children():
                self.patient_table.delete(item)
            for patient in patient_list:
                self.patient_table.insert("", END, values=patient.values())

    def select_patient(self, event_info):
        row_id = self.patient_table.focus()
        selected_item = list(self.patient_table.item(row_id, "values"))
        selected_item.pop(0)
        self.set_selected_values(selected_item)

    def save_patient(self) -> None:
        patient = self.get_res_dic()
        success, response = self.patient_c.save(patient)
        if success:
            # self.patient_table.insert("", END, values=tuple(patient.values()))
            self.reset_form()
        self.show_message_box(success, response)

    def edit_patient(self) -> None:
        patient = self.get_res_dic()
        success, response = self.patient_c.update(patient)
        if success:
            self.reset_form()
        self.show_message_box(success, response)

    def delete_patient(self) -> None:
        patient = self.get_res_dic()
        success, response = self.patient_c.delete(patient)
        if success:
            self.reset_form()
        self.show_message_box(success, response)

    def __init__(self, parent, controller):
        # patient controller
        self.patient_c = PatientController()

        super().__init__(parent, controller)

        ttk.Label(
            self,
            text="Patient Management",
            font=("Arial", 18, "bold")
        ).place(x=10, y=10)

        #  my Label drawing
        for component in list(enumerate(self.attributes)):
            self.draw_str_input(text=component[1], x=20, y=int((component[0] + 1.5) * 40))

        # my patient table headings
        self.patient_table = self.draw_table(300, 60, len(self.heading_list))

        self.patient_table.bind("<ButtonRelease>", self.select_patient)

        for i in range(0, len(self.heading_list)):
            self.patient_table.heading(i + 1, text=self.heading_list[i])
            self.patient_table.column(i + 1, width=130)

        ttk.Button(
            self,
            text="Back to Dashboard",
            command=lambda: controller.show_frame("DashboardView")
        ).place(x=10, y=350)

        self.draw_button(text="save", x=20, y=280, command=self.save_patient)
        self.draw_button(text="edit", x=100, y=280, command=self.edit_patient)
        self.draw_button(text="delete", x=180, y=280, command=self.delete_patient)

        self.reset_form()
