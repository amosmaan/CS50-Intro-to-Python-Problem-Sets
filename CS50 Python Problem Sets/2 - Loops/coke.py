def main():
    coke = int(input("Insert Coin: ")) 
    payment(coke)

def payment(money):
    amount_due = 50
    while amount_due > 0:
        if money in [25, 10, 5]: 
            amount_due = amount_due - money
            print(f"Amount Due: {amount_due}")  
        else:
            print(f"Amount Due: {amount_due}")
        money = int(input("Insert Coin: "))  
    
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")  

main()
        

