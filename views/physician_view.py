from tkinter import ttk, END

from model.view import View
from controller.physician_controller import PhysicianController


class PhysicianView(View):
    attributes = ["name", "family", "national_code", "birth_date", "license"]
    heading_list = ["physician_id", "name", "family", "national_code", "birth_date", "license"]

    def reset_form(self):
        super().reset_form()
        self.show_data_on_the_table()

    def show_data_on_the_table(self):
        success, physician_list = self.physician_c.get_all_physician()

        if success:
            for item in self.physician_table.get_children():
                self.physician_table.delete(item)
            for physician in physician_list:
                self.physician_table.insert("", END, values=physician.values())

    def select_physician(self, event_info):
        row_id = self.physician_table.focus()
        selected_item = list(self.physician_table.item(row_id, "values"))
        selected_item.pop(0)
        self.set_selected_values(selected_item)

    def save_physician(self) -> None:
        physician = self.get_res_dic()
        success, response = self.physician_c.save(physician)
        if success:
            # self.physician_table.insert("", END, values=tuple(physician.values()))
            self.reset_form()
        self.show_message_box(success, response)

    def edit_physician(self) -> None:
        physician = self.get_res_dic()
        success, response = self.physician_c.update(physician)
        if success:
            self.reset_form()
        self.show_message_box(success, response)

    def delete_physician(self) -> None:
        physician = self.get_res_dic()
        success, response = self.physician_c.delete(physician)
        if success:
            self.reset_form()
        self.show_message_box(success, response)

    def __init__(self, parent, controller):

        self.physician_c = PhysicianController()

        super().__init__(parent, controller)

        ttk.Label(
            self,
            text="physician Management",
            font=("Arial", 18, "bold")
        ).place(x=10, y=10)

        #  my Label drawing
        for component in list(enumerate(self.attributes)):
            self.draw_str_input(text=component[1], x=20, y=int((component[0] + 1.5) * 40))

        # my physician table headings
        self.physician_table = self.draw_table(300, 60, len(self.heading_list))

        self.physician_table.bind("<ButtonRelease>", self.select_physician)

        for i in range(0, len(self.heading_list)):
            self.physician_table.heading(i + 1, text=self.heading_list[i])
            self.physician_table.column(i + 1, width=130)

        ttk.Button(
            self,
            text="Back to Dashboard",
            command=lambda: controller.show_frame("DashboardView")
        ).place(x=10, y=350)

        self.draw_button(text="save", x=20, y=280, command=self.save_physician)
        self.draw_button(text="edit", x=100, y=280, command=self.edit_physician)
        self.draw_button(text="delete", x=180, y=280, command=self.delete_physician)

        self.reset_form()
