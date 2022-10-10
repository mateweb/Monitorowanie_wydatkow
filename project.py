# Main while
while True:
    print()
    month = int(input("Wybierz miesiąc [1-12]: "))

    if month == 0:
        break

# Secondary while
    while True:
        print()
        print("0. Powrót do wyboru miesiąca")
        print("1. Przeglądaj bieżące wydatki")
        print("2. Dodaj wydatek")
        print("3. Usuń wydatek")
        print("4. Statystyki")
        print("5. Zamknij program")
        print()
        user_choice = int(input("Wybierz pozycję z menu [0-5] i naciśnij Enter: "))
        print()

        if user_choice == 0:
            break
        if user_choice == 1:
            print("Przegląd aktualnych kosztów")
            print("------------------------------")
        if user_choice == 2:
            print("Dodaj nowy wydatek")
            print("------------------------------")
        if user_choice == 3:
            print("Usuń istniejący wydatek")
            print("------------------------------")
        if user_choice == 4:
            print("Statystyki")
            print("------------------------------")
       
