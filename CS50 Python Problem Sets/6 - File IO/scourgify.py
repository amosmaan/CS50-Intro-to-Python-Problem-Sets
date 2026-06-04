import csv
import sys


def main():
    if len(sys.argv) < 3:  # check for input on command line
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv") != True:
        sys.exit("Not a CSV file")
    else:
        tonks(sys.argv[1], sys.argv[2])


def tonks(x, y):  # harry potter list sorting
    listofdict = []  # list to store original csv file
    try:
        with open(x, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                listofdict.append({"first": first, "last": last, "house": row["house"]})

        with open(y, "w", newline="") as file1:
            writer = csv.DictWriter(file1, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for i in range(len(listofdict)):
                writer.writerow(
                    {
                        "first": listofdict[i]["first"],
                        "last": listofdict[i]["last"],
                        "house": listofdict[i]["house"],
                    }
                )
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
