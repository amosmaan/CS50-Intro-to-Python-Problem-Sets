import random
import sys
def main():
    while True:
        try:
            x = int(input("Level:"))
            if x > 0:
                break
        except ValueError:
            pass
    y = random.randrange(1, x)
    
    while True:
        try:
            z = int(input("Guess:"))
            if z < 0:
                break
            elif z == y:
                print ("Just right!")
                sys.exit()
            elif z > y:
                print("Too large!")
            else:
                print("Too small!")
        except ValueError:
            pass
main()