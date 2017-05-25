import time, datetime, sqlite3
from ClassSection import ClassSection

sqlite_file = 'courses_2174.sqlite'
table_name = 'courses'
connection = sqlite3.connect(sqlite_file)
cursor = connection.cursor()

def convert_to_24hr(time):
    #format: "hh:MM XX" or "HH:MM" or datetime.time (HH:MM:SS)
    if "PM" in time:
        am_pm = "PM"
    else:
        am_pm = "AM"

    time = time.split(" ")
    time = time[0].split(":")
    hour = int(time[0])
    if(len(time) > 1):
        minute = int(time[1])
    else:
        minute = 0


    if am_pm == "PM" and hour < 12:
        hour += 12

    return datetime.time(hour, minute, 0)

def time_in_range(time_range, x):
    time_range = time_range.split("-")
    start = convert_to_24hr(time_range[0])
    end = convert_to_24hr(time_range[1])

    # if start <= end:
    return start <= x <= end
    # else:
        # return start <= x or x <= end

def clean_input(string):
    return ''.join(char for char in string if char.isalnum())

def remove_leading_zeros(room):
    for char in room:
        if char == "0":
            room.remove(char)
        if char != "0":
            return room

def room_to_floor(room):
    if "G" in room:
        return "G"
    else:
        room = room.lstrip("0") # Remove leading zeros
        room = room[:-2]        # Remove last two characters
        return room

if __name__ == "__main__":

    # INPUT
    _building = input("Enter a building: ")
    _day = input("Enter a day (Leave blank to use today): ")
    _time = input("Enter a time( Leave blank to use now): ")

    # BUILDING
    #   Allows for typed out name ex 'Cathedral of Learning' or abbrev. ex 'CL'
    if _building in ClassSection.BUILDING_CODES_REV:
        _building = ClassSection.BUILDING_CODES_REV[_building]
    elif _building not in ClassSection.BUILDING_CODES:
        print("Error - building " + _building + " not recognized.")
        exit(1)

    _building = clean_input(_building)

    # DAY
    if _day == "":
        # If no input, use current day
        _day = time.strftime("%A")
    if _day + " " not in ClassSection.DAY_CODES:
        for elem in ClassSection.DAY_DICT:
            # Allows for more abbreviations - ex Mo, Mon, Mond, Tue, Tues, etc.
            if _day in elem:
                _day = ClassSection.DAY_DICT[elem]

    # TIME
    if _time == "":
        # If no input, use current time
        _time = datetime.datetime.now().time()
    else:
        # Convert input to 24hr time 
        _time = convert_to_24hr(_time)

    # SQL
    cursor.execute('SELECT * FROM courses WHERE {cn}=?'.\
            format(cn='building'), (_building,))
    while True:
        row = cursor.fetchone()

        if row == None:
            print("End of results")
            break

        # Print classrooms that are busy 
        #   Todo - maybe put in list, run through again and find EMPTY instead
        #   of FULL?
        if _day in row[1] and time_in_range(row[2], _time):
            print("ROOM: " + row[4])
            # print("FLOOR: " + room_to_floor(row[4]))
            # print("")

    cursor.close()
