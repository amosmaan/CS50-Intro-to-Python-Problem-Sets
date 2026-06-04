import random

def main():
    y = get_level()
    generate_integer(y)

def get_level():
    while True:
        try:
            x = int(input("Level:"))
            if x in [1, 2, 3]:
                return x
        except ValueError:
            pass

def generate_integer(level):
    score = 0 
    if level == 1:
        for _ in range(10):
            n = random.sample(range(0, 10), 3)
            x1 = n[0]
            x2 = n[1]
            answer = x1 + x2
            for attempt in range(3):
                try:
                    question = int(input(f"{x1} + {x2} = "))
                    if answer == question:
                        score += 1
                        break
                    else:
                        print("EEE")
                except ValueError:
                    print("EEE")
            else:
                print(f"{x1} + {x2} = {answer}")

    if level == 2:
        for _ in range(10):
            n = random.sample(range(10, 20), 3)
            x1 = n[0]
            x2 = n[1]
            answer = x1 + x2
            for attempt in range(3):
                try:
                    question = int(input(f"{x1} + {x2} = "))
                    if answer == question:
                        score += 1
                        break
                    else:
                        print("EEE")
                except ValueError:
                    print("EEE")
            else:
                print(f"{x1} + {x2} = {answer}")
    if level == 3:
        for _ in range(10):
            n = random.sample(range(30, 40), 3)
            x1 = n[0]
            x2 = n[1]
            answer = x1 + x2
            for attempt in range(3):
                try:
                    question = int(input(f"{x1} + {x2} = "))
                    if answer == question:
                        score += 1
                        break
                    else:
                        print("EEE")
                except ValueError:
                    print("EEE")
            else:
                print(f"{x1} + {x2} = {answer}")
    
    print(f"Score: {score}")
    
if __name__ == "__main__":
    main()