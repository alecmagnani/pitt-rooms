class ClassSection:

    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.date_time = ""

    def set_timeslot(self, date_time):
        self.date_time = date_time

    def display(self):
        print(self.title + " " + self.date_time)
