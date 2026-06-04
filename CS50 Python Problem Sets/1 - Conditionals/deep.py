def main(): 
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer(x)

def answer(q):
    if q == "42":
        print("Yes")
    elif q == "Forty Two":
        print("Yes")
    elif q == ("forty-two"):
        print ("Yes")
    else:
        print ("No")

main()