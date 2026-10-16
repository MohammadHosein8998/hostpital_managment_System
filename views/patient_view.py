from importlib.metadata import pass_none
from tkinter import ttk

from model.view import View


class PatientView(View):
    attributes = ["name", "family", "national_code", "birth_date", "phone_number"]
    heading_list = ["patient_id" , "name", "family", "national_code", "birth_date", "phone_number"]


    def __init__(self, parent, controller):
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
        self.patient_table = self.draw_table(300 , 60 , len(self.heading_list))

        for i in range(0, len(self.heading_list)):
            self.patient_table.heading(i + 1, text=self.heading_list[i])
            self.patient_table.column(i + 1, width=130)

        self.patient_table.bind("<ButtonRelease>" , self.select_patient)

        ttk.Button(
            self,
            text="Back to Dashboard",
            command=lambda: controller.show_frame("DashboardView")
        ).place(x=10, y=350)


    def select_patient(self,event):
        pass

