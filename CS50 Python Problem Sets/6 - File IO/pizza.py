import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") != True:
        sys.exit("Not a CSV file")
    else: 
        food_table(sys.argv[1])


def food_table(x):
    try:
        with open(x, 'r') as file:
            csvFile = csv.DictReader(file)
            print(tabulate(csvFile, headers = "keys"))
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()