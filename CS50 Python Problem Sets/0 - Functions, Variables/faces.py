def main():
    x = input ("What do you feel? ")
    convert (x)

def convert(to):
    print(to.replace(":)", "happy").replace(":(","sad"))

main()