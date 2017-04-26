import requests, re
import webbrowser
from ClassSection import ClassSection
from bs4 import BeautifulSoup, SoupStrainer

BULDING_CODES = { 'ALLEN':'Allen Hall', 'ALUM':'Alumni Hall', 'BELLH':'Bellefield Hall',
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

DAY_CODES = [ "Mo ", "Tu ", "We ", "Th ", "Fr ", "Sa ", "Su "]

TITLE_IGNORE_LIST = ["M.S. Thesis", "Directed Study", "Higher Education Internship", 
                    "Supervised Research", "Guidanc in the Doctoral Degree", "Internship",
                    "Independent Study", "Directed Research-Readings","Research And Thesis Ma Degree",
                    "Readings In Selected Fields", "Research And Dissertation Phd",
                    "Graduate Projects", "Research, Phd", "Ph.D. Dissertation"]
BLACKLIST = ["Web", "WEB", "web", "WWW", "TBA"]

CURRENT_TERM = "2174"
OFFSET_VAL = 15
sections = []

for PAGE_NUM in range(0, 1):
    URL = "http://www.courses.as.pitt.edu/results-title.asp?TITL=+%2F&TERM=" + CURRENT_TERM + "&offset=" + str(OFFSET_VAL * PAGE_NUM)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    elems = (soup.find_all('tr', {'class':['even', 'odd']}))

    for elem in elems:
        title = elem.find_all('td', width="31%")
        strtitle = str(title).strip("[<td width=\"31%\">")
        strtitle = str(strtitle).strip("</td>]")

        link = (elem.find_all('a'))
        link = str(re.findall('"([^"]*)"', str(link)))
        link = str(link).strip("['")
        link = str(link).strip("']")
        link = str(link).replace("&amp;", "&")
        link = "http://www.courses.as.pitt.edu/" + link

        if(strtitle not in TITLE_IGNORE_LIST):
            sections.append(ClassSection(strtitle, link))

for sec in sections:
    url = sec.link
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')

    text = soup.find_all("td", class_="style1")
    for t in text:
        if any(day in str(t) for day in DAY_CODES) and any(building in str(t)for building in BULDING_CODES):
            sec.set_timeslot(t.get_text())
            break

for sec in sections:
    sec.display()
