import re
import sys


def main():
        print(convert(input("Hours: ")))



def convert(s):
    regex = "(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    matches = re.search(r"^" + regex + " to " + regex + "$", s)
    if matches:
        time1 = standardise(matches.group(1), matches.group(2), matches.group(3)) 
        time2 = standardise(matches.group(4), matches.group(5), matches.group(6))
        return time1 + " to " + time2
    else: 
        sys.exit(ValueError)
def standardise(hr, min, time):
    if hr == "12":
        if time == "AM":
            hour = "00"
        else: 
            hour = "12"
    else:
        if time == "AM":
            hour = f"{int(hr):02}"
        else:
            hour = f"{int(hr)+ 12}"
        if min == None:
            minute = "00"
        else:
            minute = f"{int(min):02}"
        return f"{hour}:{minute}"

            

               
if __name__ == "__main__":
    main()