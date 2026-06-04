month_list =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]

while True:
    date = input("Date: ").strip()
    try:
        if "/" in date and date[0].isnumeric():
            m, d, y = map(lambda x: int(x), date.split("/"))
        else:
            raise ValueError

        if 1 < m > 12 or 1 < d > 31:
            continue
        else:
            print(f"{y}-{m:02}-{d:02}")

    except ValueError:
        if "," in date and not date[0].isnumeric():
            m, d, y = date.split(" ")
            m = month_list.index(m) + 1
            d = int(d.replace(",", ""))
        else:
            continue

        if 1 < m > 12 or 1 < d > 31:
            continue
        else:
            print(f"{y}-{m:02}-{d:02}")

        

