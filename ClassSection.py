class ClassSection:

    BUILDING_CODES = { 'ALLEN':'Allen Hall', 'ALUM':'Alumni Hall', 'BELLH':'Bellefield Hall',
            'BENDM':'Benedum Hall','BSTWR':'Biomedical Science Tower',
            'CHVRN':'Chevron Science Center', 'CL':'Cathedral of Learning',
            'CLAPP':'Clapp Hall', 'CRAWF':'Crawford Hall', 'EBERL':'Eberly Hall',
            'FALKS':'Falk School', 'FILM':'Pittsburgh Filmmakers',
            'FKART':'Frick Fine Arts Building', 'LANGY':'Langley Hall',
            'LAWRN':'Lawrence Hall', 'MERVS':'Mervis Hall', 'MUSIC':'Music Building',
            'OEH':'Old Engineering Hall', 'EH':'Old Engineering Hall',
            'PUBHL':'Public Health', 'SENSQ':'Sennott Square',
            'THACK':'Thackeray Hall', 'THAW':'Thaw Hall', 'TREES':'Trees Hall',
            'WWPH':'Wesley W. Posvar Hall' }

    BUILDING_CODES_REV = { 'Allen Hall':'ALLEN', 'Alumni Hall':'ALUM', 'Bellefield Hall':'BELLH',
            'Benedum Hall':'BENDM', 'Biomedical Science Tower':'BSTWR',
            'Chevron Science Center':'CHVRN', 'Cathedral of Learning':'CL',
            'Clapp Hall':'CLAPP', 'Crawford Hall':'CRAWF', 'Eberly Hall':'EBERL',
            'Falk School':'FALKS', 'Pittsburgh Filmmakers':'FILM', 'Frick Fine Arts Building':'FKART',
            'Langley Hall':'LANGY', 'Lawrence Hall':'LAWRN','Mervis Hall':'MERVS',
            'Music Building':'MUSIC', 'Public Health':'PUBHL', 'Sennot Square':'SENSQ',
            'Thackeray Hall':'THACK', 'Thaw Hall':'THAW', 'Trees Hall':'TREES',
            'Wesley W. Posvar Hall':'WWPH' }

    DAY_CODES = [ "Mo ", "Tu ", "We ", "Th ", "Fr ", "Sa ", "Su "]
    DAY_DICT = { "Monday":"Mo", "Tuesday":"Tu", "Wednesday":"We",
            "Thursday":"Th", "Friday":"Fr", "Saturday":"Sa", "Sunday":"Su" }

    TITLE_IGNORE_LIST = ["M.S. Thesis", "Directed Study", "Higher Education Internship", 
            "Supervised Research", "Guidanc in the Doctoral Degree", "Internship",
            "Independent Study", "Directed Research-Readings","Research And Thesis Ma Degree",
            "Readings In Selected Fields", "Research And Dissertation Phd",
            "Graduate Projects", "Research, Phd", "Ph.D. Dissertation"]
    
    BLACKLIST = ["Web", "WEB", "web", "WWW", "TBA"]

    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.day = ""
        self.time = ""
        self.building = ""
        self.room = ""

    def set_day(self, day):
        self.day = "\"" + day + "\"" 
    def set_time(self, time):
        self.time = "\"" + time + "\""
    def set_room(self, room):
        split = room.split("\xa0") # I don't know why this works, it just does
        self.room = "\"" + split[0] + "\""
        self.building = "\"" + split[1] + "\""

    def is_valid(self):
        return (self.day != "" and self.time != "" and self.building != "" and self.room != "")

    def csv_format(self):
        return self.title + "," + self.day + "," + self.time + "," + self.building + "," + self.room + "\n"
