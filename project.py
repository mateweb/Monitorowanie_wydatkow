
import sys
import datetime

from datetime import date


# Variables
expenses = []
today = date.today()
file = open('expense_base.txt', 'w+')


# Printing all expenses
def get_expenses(month):
    for expense_value, expense_cat, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_value} - {expense_cat} - {today} ')


# Adding a new expense
def add_expense(month):
    print()
    try:
        expense_value = int(input('Podaj kwote wydatku [euro]: '))
        print()
        expense_cat = input('Podaj kategorie: [Jedzenie, Chemia, Auto, Mieszkanie, Sparkonto, etc.] ')
        
    
        expense = (expense_value, expense_cat, month)
        expenses.append(expense)
    
    except ValueError:
        print()
        print('Wpisz poprawna kwote! ')
    else:
        print()
        print('Poprawnie dodano!')
    print()


# Delete expenses
def delete_expenses(month):
    print(expenses)
    print()
    try:
        user_delete = int(input('Wybierz pozycje do usuniecia [0,1,2,3 itd.] i nacisnij Enter: '))
        del expenses[user_delete]
        print()
        message = print('Pomyslnie usunieto ')
    except ValueError:
        print()
        print('Wybierz poprawnie numer indeksu [Cyfra 0 oznacza pierwsza pozycje, cyfra 1 druga pozycje itd.]')
    except IndexError:
        print()
        print('Wybierz poprawnie numer indeksu [Cyfra 0 oznacza pierwsza pozycje, cyfra 1 druga pozycje itd.]')
    else:
        print(message)
    print()
    print(expenses)


# Statistics
def show_statistics(month):
    summ_value_month = sum(expense_value for expense_value, _, expense_month in expenses if expense_month == month)
    summ_all_value = sum(expense_value for expense_value, _, _, in expenses)


    print('Laczna suma wydatkow w tym miesiacu wynosi [€]: ', summ_value_month)
    print('Laczna ilosc wydatkow w tym roku [€]: ', summ_all_value)
 # New option: show difference (incomes - expenses)   


 # Save / Open a File
def save_open_file():
    with open('expense_base.txt', 'w') as file:
        file.write(expenses)

    



# New definition: add_income

# New definition: show_income




# Main while
while True:
    print()
    month = int(input("Wybierz miesiac [1-12]: "))

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
        print('5. Zapisz do pliku')
        print("6. Zamknij program")
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
            print("Zapisz do pliku")
            print("------------------------------")
            print()
            save_open_file
        if user_choice == 6:
            sys.exit(0)
       
