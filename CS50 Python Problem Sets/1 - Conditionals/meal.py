def main():
    x = input("What time is it? ")

    convert(x)

def convert(time):
    hours, mins = time.split(":")

    time = (float(hours) + (float (mins) / 60))

    if 7<= time < 8:
        print ("breakfast time")

    elif 12<= time < 13:
        print ("lunch time")

    elif 18<= time < 19:
        print ("dinner time")
    
    else: 
        return None
    
if __name__ == "__main__":
    main()