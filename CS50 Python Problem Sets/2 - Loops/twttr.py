def main():
    word = input("")
    print (shorten(word))

def shorten(word):
    result = ""
    for c in word:
        if c not in ["A","E","O","I","U","a","e","i","o","u"]:
            result += c 
    return result

if __name__ == "__main__":
    main()
