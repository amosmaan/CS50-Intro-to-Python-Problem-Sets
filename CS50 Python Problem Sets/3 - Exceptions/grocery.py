grocery_list = {}
while True:
    try:
        x = input("").upper()
        if x in grocery_list:
            grocery_list[x] = grocery_list[x] + 1
        else:
            grocery_list [x] = 1 
    except EOFError:
        for _ in grocery_list:
            print(grocery_list[_], _)
        break