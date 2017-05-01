import time 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ClassSection import ClassSection

# use creds to create a cleint to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("pitt-courses_2174").sheet1

if __name__ == "__main__":
    _building = input("Enter a building: ")
    _day = input("Enter a day (Leave blank to use today):  ")
    _time = input("Enter a time( Leave blank to use now): ")

    if _building in ClassSection.BUILDING_CODES_REV:
        _building = ClassSection.BUILDING_CODES_REV[_building]
    else:
        print("Error - building " + _building + " not recognized.")

    if _day == "":
        _day = time.strftime("%A")
        print(_day)
    else:
        print(ClassSection.DAY_DICT[_day])

    if _time == "":
        _time = time.strftime("%H") + ":" + time.strftime("%M")
        print(_time)
    else:
        print(_time)
