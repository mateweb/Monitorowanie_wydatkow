import sys
import os

# while - user should to choice one Month
while True:
    print()
    month = int(input("Wybierz miesiąc [1-12]: "))

    if month == 0:
        break

    while True:
        print()
        print("0. Powrót do wyboru miesiąca")
        print("1. Przeglądaj bieżące wydatki")