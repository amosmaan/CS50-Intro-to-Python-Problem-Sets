def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    x = float (d)
    x = round (x , 1)
    return x

def percent_to_float(p):
    y = float(p)/100
    y = round (y,2)
    return y

main()