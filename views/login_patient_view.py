from tkinter import ttk

from controller.patient_controller import PatientController
from model.user import User
from model.view import View


class LoginPatientView(View):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.patient_c = PatientController()

        ttk.Label(
            self,
            text="Patient Login",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        ttk.Label(self, text="Username (national code)", font=("Arial", 14, "bold")).pack()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure('TButton', width=20, borderwidth=1, focusthickness=3, focuscolor='none')

        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(pady=5)

        ttk.Label(self, text="Password", font=("Arial", 14, "bold")).pack()

        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        ttk.Button(
            self,
            text="Login",
            command=self.login
        ).pack(pady=20)

        ttk.Button(
            self,
            text="sign up",
            command=self.sign_up
        ).place(x=1000 , y=120)

        ttk.Button(
            self,
            text="back",
            command= self.__back
        ).place(x=150 , y=120)

        self.error_label = ttk.Label(self, text="")
        self.error_label.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        success , respond = self.patient_c.login(username , password)
        if success:
            self.controller.show_frame("DashboardView")
            self.show_message_box(success , respond)
        else:
            self.error_label.config(
                text=respond,
                background="red",
                font=("Arial", 10)
            )


    def __back(self):
        self.controller.show_frame("LoginView")

    def sign_up(self):
        self.controller.show_frame("SignUpView")