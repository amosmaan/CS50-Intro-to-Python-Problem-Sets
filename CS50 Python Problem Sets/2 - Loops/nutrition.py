def main():
    food = input("What food should we check? ")
    hungry(food)

def hungry(x):
    nutrition = [
        {"fruit": "Apple", "calories":"130"},
        {"fruit": "Avocado", "calories" : "50"},
        {"fruit": "Banana", "calories" : "110"},
        {"fruit": "Cantaloupe", "calories" : "50"},
        {"fruit": "Grapefruit", "calories" : "60"},
        {"fruit": "Grapes", "calories" : "90"},
        {"fruit": "Sweet Cherries", "calories" : "100"}
        
    ]

    for i in nutrition:
        if x == i["fruit"]:
            print ("Calories: "+ i["calories"])
        else:
            continue

        return None
        
main()