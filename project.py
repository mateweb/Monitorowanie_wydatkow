import sys

# while - user should to choice one Month
while True:
    print()
    month = int(input("Wybierz miesiąc [1-12]: "))

    if month == 0:
        break

    while True :
        if month == 1:
            print("Styczeń")
        if month == 2:
            print("Luty")
        if month == 3:
            print("Marzec ")
        if month == 4:
            print("Kwiecień")
        if month == 5:
            print("Maj")
        if month == 6:
            print("Czerwiec")
        if month == 7:
            print("Lipiec")
        if month == 8:
            print("Sierpień")
        if month == 9:
            print("Wrzesień")
        if month == 10:
            print("Październik")
        if month == 11:
            print("Listopad")
        if month == 12:
            print("Grudzień")
        else:
            print("Wybierz poprawnie miesiąc!")