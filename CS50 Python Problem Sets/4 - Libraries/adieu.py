import inflect
def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            x = input("Name: ")
            names.append(x)
        except EOFError:
            concats = p.join(names)
            print ("Adieu, adieu, to " + concats)
            break

main()
