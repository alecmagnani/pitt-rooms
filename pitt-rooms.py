import time, datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ClassSection import ClassSection

# use creds to create a cleint to interact with the Google Drive API
# scope = ['https://spreadsheets.google.com/feeds']
# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# client = gspread.authorize(creds)

# sheet = client.open("pitt-courses_2174").sheet1

def convert_to_24hr(time):
    #format: "HH:MM XX"
    time = time.split(" ")
    am_pm = "AM"

    if len(time) > 1:
        am_pm = time[1]

    time = time[0].split(":")

    if am_pm == "PM":
        time[0] = int(time[0]) + 12

    return datetime.time( int(time[0]), int(time[1]), 0)


def time_in_range(start, end, x):
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

if __name__ == "__main__":
    _building = input("Enter a building: ")
    _day = input("Enter a day (Leave blank to use today):  ")
    _time = input("Enter a time( Leave blank to use now): ")

    if _building in ClassSection.BUILDING_CODES_REV:
        _building = ClassSection.BUILDING_CODES_REV[_building]
    elif _building not in ClassSection.BUILDING_CODES:
        print("Error - building " + _building + " not recognized.")

    print(_building)

    if _day == "":
        _day = time.strftime("%A")
        print(_day)
    else:
        print(ClassSection.DAY_DICT[_day])

    if _time == "":
        _time = datetime.datetime.now().time()
    else:
        _time = convert_to_24hr(_time)

    start = convert_to_24hr("2:30 PM")
    end = convert_to_24hr("3:45 PM")
    print(time_in_range(start, end, _time))
