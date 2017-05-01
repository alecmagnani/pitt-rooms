import sys
import os.path
from CourseScraper import generate
from ClassSection import ClassSection

def make_csv(term_number):
    sections = []
    generate(sections, term_number)
    filename = "courses_" + term_number + ".csv"

    with open(filename, 'w') as file:
        file.write("Course Title,Day,Time,Building,Room\n")
        for sec in sections:
            if sec.is_valid():
                file.write(sec.csv_format())
            else:
                sections.remove(sec)

    return

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please provide a term number code")
        exit(0)
    else:
        filename = "courses_" + sys.argv[1] + ".csv"

    if os.path.isfile(filename):
        print("This csv already exists!")
    else:
        make_csv(sys.argv[1])
        print("csv generated successfully")
