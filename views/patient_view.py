


from tkinter import ttk


class PatientView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        ttk.Label(
            self,
            text="Patient Management",
            font=("Arial", 18, "bold")
        ).pack(pady=30)

        ttk.Button(
            self,
            text="Back to Dashboard",
            command=lambda: controller.show_frame("DashboardView")
        ).pack()