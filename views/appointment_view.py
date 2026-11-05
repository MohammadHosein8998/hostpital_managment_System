from tkinter import ttk, StringVar
from tkinter import END

from controller import appointment_controller
from controller.appointment_controller import AppointmentController
from model.view import View


class AppointmentView(View):
    attributes = ["physician_id", "patient_id", "date", "time"]
    heading_list = ["appointment_id", "physician_id", "patient_id", "appointment_date", "appointment_time"]

    def reset_form(self):
        super().reset_form()
        self.show_data_on_the_table()

    def show_data_on_the_table(self):
        success, appointment_list = self.appointment_c.find_all()

        if success:
            for item in self.appointment_table.get_children():
                self.appointment_table.delete(item)
            for appointment in appointment_list:
                self.appointment_table.insert("", END, values=appointment.values())

    def select_appointment(self, event_info):
        row_id = self.appointment_table.focus()
        selected_item = list(self.appointment_table.item(row_id, "values"))
        if selected_item:
            self.appointment_id.set(selected_item[0])
            selected_item.pop(0)
        self.set_selected_values(selected_item)

    def save_appointment(self) -> None:
        appointment = self.get_res_dic()
        success, response = self.appointment_c.save(appointment)
        if success:
            self.appointment_id.set("")
            self.reset_form()
        self.show_message_box(success, response)

    def edit_appointment(self) -> None:
        appointment = self.get_res_dic()
        success, response = self.appointment_c.update(self.appointment_id.get(),appointment)
        if success:
            self.appointment_id.set("")
            self.reset_form()
        self.show_message_box(success, response)

    def delete_appointment(self) -> None:
        appointment = self.get_res_dic()
        success, response = self.appointment_c.delete(self.appointment_id.get())
        if success:
            self.appointment_id.set("")
            self.reset_form()
        self.show_message_box(success, response)

    def __init__(self, parent, controller):
        self.appointment_id = StringVar()
        # appointment controller
        self.appointment_c = AppointmentController()

        super().__init__(parent, controller)

        ttk.Label(
            self,
            text="appointment Management",
            font=("Arial", 18, "bold")
        ).place(x=10, y=10)

        ttk.Label(self , text="appointment_id").place(x=20, y=70)
        ttk.Label(self , textvariable=self.appointment_id).place(x=120, y=70)
        #  my Label drawing
        for component in list(enumerate(self.attributes)):
            self.draw_str_input(text=component[1], x=20, y=int((component[0] + 2.5) * 40))

        # my appointment table headings
        self.appointment_table = self.draw_table(300, 60, len(self.heading_list))

        self.appointment_table.bind("<ButtonRelease>", self.select_appointment)

        for i in range(0, len(self.heading_list)):
            self.appointment_table.heading(i + 1, text=self.heading_list[i])
            self.appointment_table.column(i + 1, width=130)

        ttk.Button(
            self,
            text="Back to Dashboard",
            command=lambda: controller.show_frame("AdminDashboardView")
        ).place(x=10, y=350)

        self.draw_button(text="save", x=20, y=280, command=self.save_appointment)
        self.draw_button(text="edit", x=100, y=280, command=self.edit_appointment)
        self.draw_button(text="delete", x=180, y=280, command=self.delete_appointment)

        self.reset_form()
