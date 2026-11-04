from tkinter import ttk

from model.view import View



class LoginView(View):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        ttk.Label(
            self,
            text="Hospital Management System _ test",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        ttk.Button(
            self,
            text="Login as admin",
            command= self.__show_admin_login
        ).pack(ipadx=50, padx=120, pady=20)

        ttk.Button(
            self,
            text="Login as patient",
            command= self.__show_patient_login
        ).pack(ipadx=50, padx=200, pady=20)

    def __show_admin_login(self):
        self.controller.show_frame("AdminLoginView")

    def __show_patient_login(self):
        self.controller.show_frame("PatientLoginView")