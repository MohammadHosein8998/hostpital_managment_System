


from tkinter import ttk

from model.view import View


class DashboardView(View):
    def __init__(self, parent, controller):
        super().__init__(parent , controller)


        ttk.Label(
            self,
            text="Hospital Dashboard",
            font=("Arial", 20, "bold")
        ).pack(pady=30)

        ttk.Button(
            self,
            text="Manage Patients",
            command=lambda: controller.show_frame("PatientView")
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Manage Physicians",
            command=lambda: controller.show_frame("PhysicianView")
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Appointments",
            command=lambda: controller.show_frame("AppointmentView")
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Visits and Reports",
            command=lambda: controller.show_frame("VisitView")
        ).pack(pady=10)

        ttk.Button(
            self,
            text="Logout",
            command=lambda: controller.show_frame("LoginView")
        ).pack(pady=30)