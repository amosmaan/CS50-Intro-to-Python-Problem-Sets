total = 0 
while True:
    felipe = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
    try:
        x = input("What do you want to order? ").lower()
        if x in felipe:
            total += felipe[x]
            print(f"Total: ${total:.2f}")
            continue
        else:
            continue
    except EOFError:
        break