from tkinter import ttk

from model.view import View
from service import patient_service


class PatientDashboardView(View):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.welcome_label = ttk.Label(self, text="", font=("Arial", 12, "bold"))

        self.welcome_label.place(x=100, y=100)

        self.welcome_label.pack(pady=30)

        ttk.Button(
            self,
            text="Make an appointment",
            command=self.make_appointment,
        ).pack(pady=30)

        ttk.Button(
            self,
            text="patient info",
            command=self.patient_info,
        ).pack(pady=30)

        ttk.Button(
            self,
            text="log out",
            command= lambda : self.controller.show_frame("PatientLoginView"),
        ).pack(pady=30)

    def make_appointment(self):
        self.controller.show_frame("PatientMakeAppointmentView")

    def patient_info(self):
        self.controller.show_frame("PatientInfoView")
