def main():
    x = input("Greeting: ")
    print (value(x))


def value(greeting):
    welcome = ""
    if greeting.startswith("Hello"):
        welcome = "$10"
    elif greeting.startswith("H"):
        welcome = "$20"
    else:
        welcome = "$100"
    return welcome

if __name__ == "__main__":
    main()