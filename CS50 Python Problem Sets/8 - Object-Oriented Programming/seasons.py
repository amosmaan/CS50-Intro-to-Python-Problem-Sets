import datetime
import inflect
import re
import sys

def main():
    y = date_diff()
    mins = y * 24 * 60
    p = inflect.engine()
    print (p.number_to_words(mins) + " minutes")
def date_diff():
    current_date = str(datetime.date.today())
    x = input ("What is your date of birth? ")
    regexdate = re.search(r"^(19|20)\d\d([- /.])(0[1-9]|1[012])\2(0[1-9]|[12][0-9]|3[01])$", x)
    if regexdate is None:
        sys.exit("You need to enter a valid date in the format YYYY-MM-DD")
    else:
        d1 =  datetime.datetime.strptime(x, "%Y-%m-%d")
        d2 =  datetime.datetime.strptime(current_date, "%Y-%m-%d")
        return abs((d2 - d1).days)


if __name__ == "__main__":
    main()