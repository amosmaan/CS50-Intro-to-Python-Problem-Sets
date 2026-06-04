import emoji 
def main():
    x = input("Input: ")
    emojized(x)

def emojized(android):
        print (emoji.emojize("Output: " + android, language='alias'))

main()