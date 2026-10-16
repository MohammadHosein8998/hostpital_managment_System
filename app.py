import tkinter as tk
import tkinter.ttk as ttk

from views.login_view import LoginView
from views.dashboard_view import DashboardView
from views.patient_view import PatientView
from views.physician_view import PhysicianView
from views.test import TestView


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Hospital Management System")
        self.geometry("1100x650")
        self.minsize(800, 600)

        # محل نگهداری صفحات
        self.frame = {}

        # ظرف مشترک تمام صفحات هست
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        for PageClass in (LoginView, DashboardView, PatientView , PhysicianView):
            page = PageClass(container, self)
            self.frame[PageClass.__name__] = page

            page.grid(row=0, column=0, sticky="nsew")

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.show_frame("DashboardView")

    def show_frame(self, page_name):
        """نمایش صفحه موردنظر"""
        frame = self.frame[page_name]
        frame.tkraise()
