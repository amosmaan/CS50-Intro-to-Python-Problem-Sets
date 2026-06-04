def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(x):
    unwanted = [".", "?", ",", "/", ";", ":", "()", "---"]
    if any(char in x for char in unwanted):
        return False
    elif len(x)< 2 or len(x)> 6:
        return False
    elif len (x) <= 5 and x[1].isdigit() or len(x) == 6 and x[2].isdigit() or x[0].isdigit():
        return False
    else:
        return True


main()