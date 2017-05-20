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
    minute = int(time[1])

    if am_pm == "PM" and hour < 12:
        hour += 12

    return datetime.time(hour, minute, 0)

def time_in_range(time_range, x):
    time_range = time_range.split("-")
    start = convert_to_24hr(time_range[0])
    end = convert_to_24hr(time_range[1])

    # print("START: " + str(start))
    # print("END:   " + str(end))

    if start <= end:
        # print(start <= x <= end)
        return start <= x <= end
    else:
        # print(start <= x or x <= end)
        return start <= x or x <= end

def clean_input(string):
    return ''.join(char for char in string if char.isalnum())

if __name__ == "__main__":
    _building = input("Enter a building: ")
    _day = input("Enter a day (Leave blank to use today): ")
    _time = input("Enter a time( Leave blank to use now): ")

    if _building in ClassSection.BUILDING_CODES_REV:
        _building = ClassSection.BUILDING_CODES_REV[_building]
    elif _building not in ClassSection.BUILDING_CODES:
        print("Error - building " + _building + " not recognized.")
        exit(1)

    _building = clean_input(_building)

    if _day == "":
        _day = time.strftime("%A")
    if _day + " " not in ClassSection.DAY_CODES:
        _day = ClassSection.DAY_DICT[_day]

    if _time == "":
        _time = datetime.datetime.now().time()
    else:
        _time = convert_to_24hr(_time)

    cursor.execute('SELECT * FROM courses WHERE {cn}=?'.\
            format(cn='building'), (_building,))

    while True:
        row = cursor.fetchone()

        if row == None:
            print("End of results.")
            break

        if _day in row[1] and time_in_range(row[2], _time):
            print(row[4])

    cursor.close()
