import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
   sys.exit("Too many command-line arguments")

boom = sys.argv[1]
if not boom.endswith(".py"):
        sys.exit("Not a Python file")    
try:
    with open(boom, "r") as file:
        lines = file.readlines()
        print (len(lines))
except FileNotFoundError:
    sys.exit("File does not exist")