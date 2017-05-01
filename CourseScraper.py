import requests, re
import webbrowser
from ClassSection import ClassSection
from bs4 import BeautifulSoup, SoupStrainer

OFFSET_VAL = 15

def generate(sections, TERM_NUMBER):
    for PAGE_NUM in range(0, 646):
        URL = "http://www.courses.as.pitt.edu/results-title.asp?TITL=+%2F&TERM=" + TERM_NUMBER + "&offset=" + str(OFFSET_VAL * PAGE_NUM)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'lxml')
        elems = (soup.find_all('tr', {'class':['even', 'odd']}))

        for elem in elems:
            title = elem.find_all('td', width="31%")
            strtitle = str(title).strip("[<td width=\"31%\">")
            strtitle = str(strtitle).strip("</td>]")
            strtitle = strtitle.replace("&amp;", "&")
            strtitle = "\"" + strtitle + "\""

            link = (elem.find_all('a'))
            link = str(re.findall('"([^"]*)"', str(link)))
            link = str(link).strip("['")
            link = str(link).strip("']")
            link = str(link).replace("&amp;", "&")
            link = "http://www.courses.as.pitt.edu/" + link

            if(strtitle not in ClassSection.TITLE_IGNORE_LIST):
                sections.append(ClassSection(strtitle, link))

    for sec in sections:
        url = sec.link
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'lxml')

        text = soup.find_all("td", class_="style1")
        for t in text:
            if any(day in str(t) for day in ClassSection.DAY_CODES) and any(building in str(t)for building in ClassSection.BUILDING_CODES):
                timeslot = (t.get_text().split(" / "))
                sec.set_day(timeslot[0])
                sec.set_time(timeslot[1])
                sec.set_room(timeslot[2])
                break

    return sections
