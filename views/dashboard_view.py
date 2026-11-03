from tkinter import ttk

from model import admin
from model.user import User
from model.view import View


class DashboardView(View):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.welcome_label = ttk.Label(self, text="", font=("Arial", 8 , "bold"))

        self.welcome_label.place(x=100, y=30)
        self.welcome_label.pack(pady=30)
        ttk.Label(
            self,
            text="Hospital Dashboard",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        ttk.Button(
            self,
            text="Manage Patients",
            command=self.patients
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Manage Physicians",
            command=self.physicians
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Appointments",
            command=self.appointments
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Visits and Reports",
            command=lambda: controller.show_frame("VisitView")
        ).pack(pady=10)

        ttk.Button(
            self,
            text="admin info",
            command=lambda: controller.show_frame("AdminInfoView")
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Logout",
            command=lambda: controller.show_frame("LoginView")
        ).pack(pady=30)

    def patients(self):
        self.controller.show_frame("PatientView")
        self.controller.frame["PatientView"].reset_form()

    def physicians(self):
        self.controller.show_frame("PhysicianView")
        self.controller.frame["PhysicianView"].reset_form()

    def appointments(self):
        self.controller.show_frame("AppointmentView")
        self.controller.frame["AppointmentView"].reset_form()

    def visits(self):
        self.controller.show_frame("VisitView")
        self.controller.frame["VisitView"].reset_form()

    def on_show(self):
        admin = self.controller.current_user
        if admin :
            text = f"welcome dear {admin.name} {admin.family} . you are admin"
            self.welcome_label.config(text=text)