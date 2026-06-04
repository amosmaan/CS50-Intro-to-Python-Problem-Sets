def main():
    x = input("What is your file name? ").strip().lower()
    filetype(x)


def filetype(q):
    if q.endswith((".jpg", ".gif", "jpeg", ".png", "pdf", "txt", ".zip")):
        print(q.replace(".", "/"))
    else:
        print("application/octet-stream")


main()
