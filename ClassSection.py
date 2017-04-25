class ClassSection:

    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.days = []
        self.time = ""

    def set_timeslot(self, days, time):
        self.days = days
        self.time = time

    def display(self):
        # print(self.title + " " + self.days + " " + self.time)
        print(self.title)
