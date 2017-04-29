class ClassSection:

    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.day = ""
        self.time = ""
        self.room = ""

    def set_day(self, day):
        self.day = "\"" + day + "\"" 
    def set_time(self, time):
        self.time = "\"" + time + "\""
    def set_room(self, room):
        self.room = "\"" + room + "\""

    def is_valid(self):
        return (self.day != "" and self.time != "" and self.room != "")

    def csv_format(self):
        return self.title + "," + self.day + "," + self.time + "," + self.room + "\n"
