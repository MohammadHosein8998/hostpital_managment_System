from tkinter import ttk

from model.view import View
from views.login_view import LoginView


class TestView(View):

    def __init__(self , parent , controller):
        super().__init__(parent , controller)

        self.controller = controller

        ttk.Label(
            self,
            text="Hospital Management System _ test",
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
        self.error_label = ttk.Label(self, text="")
        self.error_label.pack()
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # صرفاً برای تست؛ بعداً با دیتابیس جایگزین شود
        if username == "admin" and password == "1234":
            self.controller.show_frame("DashboardView")
        else:
            self.error_label.config(
                text="Invalid username or password!",
                background="red",
                font=("Arial", 10)
            )