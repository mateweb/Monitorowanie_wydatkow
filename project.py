
import sys

# Variables
expenses = []


# Printing all expenses
def get_expenses(month):
    for expense_value, expense_cat, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_value} - {expense_cat}')


# Adding a new expense
def add_expense(month):
    print()
    expense_value = int(input('Podaj kwote wydatku [euro]: '))
    print()
    expense_cat = input('Podaj kategorie: [Jedzenie, Chemia, Auto, Mieszkanie, Sparkonto] ')
    
    expense = (expense_value, expense_cat, month)
    expenses.append(expense)
    print()
    print('Poprawnie dodano!')
    print()


# Delete expenses
def delete_expenses(month):
    print(expenses)
    print()
    user_delete = int(input('Wybierz pozycje do usuniecia [0,1,2,3 itd.] i nacisnij Enter: '))
    del expenses[user_delete]
    print()
    message = print('Pomyslnie usunieto ')
    print(message)
    print()
    print(expenses)


# Statistics
def show_statistics(month):
    summ_value_month = sum(expense_value for expense_value, _, expense_month in expenses if expense_month == month)
    summ_all_value = sum(expense_value for expense_value, _, _, in expenses)


    print('Laczna suma wydatkow w tym miesiacu wynosi [€]: ', summ_value_month)
    print('Laczna ilosc wydatkow w tym roku [€]: ', summ_all_value)


# New definition: add_income

# New definition: show_income

# New definition: show difference (incomes - expenses)




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
            print()
            get_expenses(month)
        if user_choice == 2:
            print("Dodaj nowy wydatek")
            print("------------------------------")
            print()
            add_expense(month)
        if user_choice == 3:
            print("Usuń istniejący wydatek")
            print("------------------------------")
            print()
            delete_expenses(month)
        if user_choice == 4:
            print("Statystyki")
            print("------------------------------")
            print()
            show_statistics(month)
        if user_choice == 5:
            sys.exit(0)
       
