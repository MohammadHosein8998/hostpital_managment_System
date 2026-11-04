import tkinter as tk
import tkinter.ttk as ttk

from views.admin_login_view import AdminLoginView
from views.patient_login_view import PatientLoginView
from views.admin_dashboard_view import AdminDashboardView
from views.patient_view import PatientView
from views.physician_view import PhysicianView
from views.appointment_view import AppointmentView
from views.login_view import LoginView
from views.sign_up_view import SignUpView
from views.admin_info_view import AdminInfoView
from views.patient_dashboard_view import PatientDashboardView
from views.patient_Info_View import PatientInfoView

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Hospital Management System")
        self.geometry("1300x650")
        self.minsize(800, 600)

        # متغیری برای نگهداری اطلاعات کاربر لاگین‌شده
        self.current_user = None

        # محل نگهداری صفحات
        self.frame = {}

        # ظرف مشترک تمام صفحات هست
        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        for PageClass in (LoginView, AdminLoginView, PatientLoginView, SignUpView, AdminDashboardView, PatientView,
                          PhysicianView, AppointmentView, AdminInfoView, PatientDashboardView , PatientInfoView):
            page = PageClass(container, self)

            self.frame[PageClass.__name__] = page

            page.grid(row=0, column=0, sticky="nsew")

        container.rowconfigure(0, weight=1)

        container.columnconfigure(0, weight=1)

        self.show_frame("LoginView")

    def show_frame(self, page_name):
        """نمایش صفحه موردنظر"""
        frame = self.frame[page_name]
        # اگر صفحه متدی برای به‌روزرسانی داده‌ها داشت، آن را صدا می‌زنیم
        if hasattr(frame, "on_show"):
            frame.on_show()

        frame.tkraise()
