def main():
    maths = (input("What is your math question? "))
    print(answer(maths))


def answer(n):
    x, y, z = n.split(" ")
    x = float(x)
    z = float (z)

    if y == '+':
        return x + z
    elif y == '-':
        return x - z
    elif y == '/':
        return x / z
    else:
        return x * z
    







main()