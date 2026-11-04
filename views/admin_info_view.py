from tkinter import ttk, END

from controller.admin_controller import AdminController
from model.admin import Admin
from model.view import View


class AdminInfoView(View):
    attributes = ["name", "family", "national_code", "birth_date", "user_name", "password"]

    def reset_form(self):
        super().reset_form()



    def select_admin(self , admin):
        admin_list = list(admin.values())
        admin_list.pop(0)
        self.set_selected_values(admin_list)

    def edit_patient(self) -> None:
        patient = self.get_res_dic()
        success, response = self.admin_c.update(patient)
        self.show_message_box(success, response)

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.admin_c = AdminController()

        ttk.Label(
            self,
            text="Admin profile",
            font=("Arial", 18, "bold")
        ).place(x=10, y=10)

        #  my Label drawing
        for component in list(enumerate(self.attributes)):
            self.draw_str_input(text=component[1], x=20, y=int((component[0] + 1.5) * 40))


        ttk.Button(
            self,
            text="Back to Dashboard",
            command=lambda: controller.show_frame("AdminDashboardView")
        ).place(x=10, y=350)

        self.draw_button(text="edit", x=20, y=300, command=self.edit_patient)



    def on_show(self):
        admin = self.controller.current_user
        if admin :
            self.select_admin(admin)
