while True:
    n = input("Fraction: ")
    try: 
        x,y = n.split("/")
        x = int(x) * 100
        y = int(y)
        p = round(x / y, 2)
        if 100 >= p >= 99:
            print ("F")
            break
        elif p <= 1:
            print ("E")
            break
        elif p > 100:
            pass
        else:
            print (f"{p}%")
            break
    except (ValueError, ZeroDivisionError):
        pass

