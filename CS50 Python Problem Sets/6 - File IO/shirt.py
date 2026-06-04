import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid input")  
    elif not sys.argv[2].endswith((".jpg", ".jpeg", ".png")):
        sys.exit("Invalid output")
    elif not sys.argv[1].rsplit('.')[-1] == sys.argv[2].rsplit('.')[-1]:
        sys.exit("Input and output have different extensions")
    else:
        muppets(sys.argv[1], sys.argv[2])


def muppets(x, y):
    try:
        before = Image.open(x)
        shirt = Image.open("shirt.png")  
    except FileNotFoundError:
        sys.exit("Input does not exist")
    else:
        size = shirt.size
        before = ImageOps.fit(before, size)
        before.paste(shirt, (0, 0), shirt)
        before.save(y)


if __name__ == "__main__":
    main()