# Variables
category = ['Jedzenie', 'Chemia', 'Auto', 'Mieszkanie', 'Sparkonto']
expenses = []


# Adding a new expense
def add_expense(month):
    print()
    expense_value = print(int(input('Podaj kwote wydatku [euro]: ')))
    expense_cat = print(input('Podaj kategorie: ', category))
    
    expense = (expense_value, expense_cat, month)
    expenses.append(expense)


# Printing all expenses
def print_expenses():
    print()
    if expenses in month == month:
        print(expenses)
    else:
        print('Sprobuj ponownie.')
    return



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
            print_expenses
        if user_choice == 2:
            add_expense(month)
            print("Dodaj nowy wydatek")
            print("------------------------------")
        if user_choice == 3:
            print("Usuń istniejący wydatek")
            print("------------------------------")
        if user_choice == 4:
            print("Statystyki")
            print("------------------------------")
       
