


class Report:
    def __init__(self , visit_id , date , details):
        self.visit_id = visit_id
        self.date = date
        self.details = details


    @property
    def visit_id(self):
        return self.__visit_id

    @visit_id.setter
    def set_visit_id(self, visit_id):
        self.__visit_id = visit_id