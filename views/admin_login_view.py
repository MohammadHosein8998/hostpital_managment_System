import tkinter as tk
from idlelib.colorizer import color_config
from tkinter import ttk

from controller.admin_controller import AdminController
from model.view import View



class AdminLoginView(View):
    def __init__(self, parent, controller):
        super().__init__(parent , controller)

        self.__admin_c = AdminController()
        ttk.Label(
            self,
            text="Hospital Management System For Admin",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        ttk.Label(self, text="Username", font=("Arial", 14, "bold")).pack()

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
            text="back",
            command=self.back
        ).place(x=150, y=120)

        self.error_label = ttk.Label(self, text="")
        self.error_label.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        success , response = self.__admin_c.login(username, password)
        if success:
            success , self.controller.current_user = self.__admin_c.find_admin_by_user_name(username)
            self.controller.show_frame("AdminDashboardView")
        else:
            self.error_label.config(
                text=response,
                background="red",
                font=("Arial", 10)
            )


    def back(self):
        self.controller.show_frame("LoginView")