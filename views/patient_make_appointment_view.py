from datetime import datetime
from tkinter import ttk , END
# محاسبه فاصله روز انتخاب شده تا امروز در هفته جاری
import datetime as dt

import jdatetime

from controller.appointment_controller import AppointmentController
from controller.physician_controller import PhysicianController
from model.view import View
from service import patient_service


class PatientMakeAppointmentView(View):
    attributes = ["physician_id", "patient_id", "date", "time"]
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
        physician_id = selected_item.pop(0)
        self.set_selected_value("physician_id" , physician_id)

    def save_appointment(self):
        appointment = self.get_res_dic()
        success, response = self.appointment_c.save(appointment)
        if success:
            self.reset_form()
            self.set_selected_value("patient_id" , self.controller.current_user.patient_id)
        self.show_message_box(success, response)

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # appointment controller
        self.appointment_c = AppointmentController()

        # physician controller
        self.physician_c = PhysicianController()

        # selected day that has been chosen by patient
        self.selected_day = None

        ttk.Label(
            self,
            text="making appointment",
            font=("Arial", 18, "bold")
        ).place(x=10, y=10)

        # my physician table headings
        self.physician_table = self.draw_table(300, 60, len(self.heading_list))

        self.physician_table.bind("<ButtonRelease>", self.select_physician)

        for i in range(0, len(self.heading_list)):
            self.physician_table.heading(i + 1, text=self.heading_list[i])
            self.physician_table.column(i + 1, width=130)

        #  my Label drawing
        for component in list(enumerate(self.attributes)):
            self.draw_locked_input(text=component[1], x=20, y=250 + int((component[0] + 2.5) * 40))



        ttk.Label(
            self,
            text="days for appointment",
            font=("Arial", 10, "bold")
        ).place(x=20, y=60)

        self.draw_button(text="Sa", x=20, y=100, command=lambda: self.add_day("Sat"))
        self.draw_button(text="Su", x=100, y=100, command=lambda: self.add_day("Sun"))
        self.draw_button(text="Mo", x=20, y=140, command=lambda: self.add_day("Mon"))
        self.draw_button(text="Tu", x=100, y=140, command=lambda: self.add_day("Tue"))
        self.draw_button(text="We", x=20, y=180, command=lambda: self.add_day("Wed"))
        self.draw_button(text="Thu", x=100, y=180, command=lambda: self.add_day("Thu"))
        self.draw_button(text="Fri", x=20, y=220, command=lambda: self.add_day("Fri"))

        ttk.Label(
            self,
            text="days for appointment",
            font=("Arial", 10, "bold")
        ).place(x=300, y=340)

        self.draw_button(text="Record", x=20, y=540, command=self.save_appointment)

        ttk.Button(
            self,
            text="Back to Dashboard",
            command=lambda: controller.show_frame("PatientDashboardView")
        ).place(x=100, y=540)

        self.time_plan_scheme(8, 20)

        self.reset_form()

    def on_show(self):
        patient_id = self.controller.current_user.patient_id
        self.set_selected_value("patient_id", patient_id)

    def add_day(self, day: str):
        self.selected_day = day
        print(f"Selected day: {day}")

    def add_time(self, time: str):
        if not self.selected_day:
            self.show_message_box(False, "please chose one day on the week first!")
            return

        day_mapping = {
            "Sat": 5,
            "Sun": 6,
            "Mon": 0,
            "Tue": 1,
            "Wed": 2,
            "Thu": 3,
            "Fri": 4
        }

        today = datetime.today()
        current_weekday = today.weekday()

        target_weekday = day_mapping.get(self.selected_day)


        # پیدا کردن تاریخ روز مورد نظر در هفته جاری
        days_diff = target_weekday - current_weekday
        target_date = today + dt.timedelta(days=days_diff)
        shamsi_date = jdatetime.datetime.fromgregorian(date=target_date)
        formatted_date = shamsi_date.strftime("%Y-%m-%d")

        self.set_selected_value("date", formatted_date)
        self.set_selected_value("time", time)

        # print(f"Selected Day: {self.selected_day}")
        # print(f"Calculated Date: {formatted_date}")
        # print(f"Selected Time: {time}")

    def time_plan_scheme(self, start_time_hour: int, count: int):
        column = 8
        meeting_time = 20
        meeting_duration = ["00", "20", "40"]
        meeting_duration_counter = 0
        rows = count // column
        remains = count % column
        for row in range(1, rows + 1):
            for meeting_number in range(1, column + 1):
                button_text = f"{start_time_hour}:{meeting_duration[meeting_duration_counter]}:00"
                self.draw_button(text=button_text,
                                 x=220 + (meeting_number * 80), y=300 + (row * 80),
                                 command=lambda: self.add_time(button_text))
                if meeting_duration[meeting_duration_counter] == meeting_duration[-1]:
                    start_time_hour += 1
                meeting_duration_counter = (meeting_duration_counter + 1) % len(meeting_duration)


        else:
            for meeting_number in range(1, remains + 1):
                button_text = f"{start_time_hour}:{meeting_duration[meeting_duration_counter]}:00"
                self.draw_button(text=button_text,
                                 x=220 + (meeting_number * 80),
                                 y=300 + ((rows + 1) * 80),
                                 command=lambda: self.add_time(button_text))
                if meeting_duration[meeting_duration_counter] == meeting_duration[-1]:
                    start_time_hour += 1
                meeting_duration_counter = (meeting_duration_counter + 1) % len(meeting_duration)
