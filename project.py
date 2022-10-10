import sys

# while - user have to choice one Month
while True:
    print()
    month = int(input("Wybierz miesiac [1-12]: "))

    if month == 0:
        break

    while True :
        if month == 1:
            print("Styczen")
        if month == 2:
            print("Luty")
        if month == 3:
            print("Marzec ")
        if month == 4:
            print("Kwiecien")
        if month == 5:
            print("Maj")
        if month == 6:
            print("Czerwiec")
        if month == 7:
            print("Lipiec")
        if month == 8:
            print("Sierpien")
        if month == 9:

