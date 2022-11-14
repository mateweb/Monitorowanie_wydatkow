import sys
import sqlite3
import datetime

from datetime import date, datetime


# Variables

expenses = []
incomes = []
id = 0


# Printing all expenses
def get_expenses(month):
    #for expense_value, expense_cat, expense_month in expenses:
    #    if expense_month == month:
    #        print(f'{expense_value}€ - {expense_cat} - {d} ')
    
    try:

        db = sqlite3.connect('expenses3.db')
        cursor = db.cursor()

        sql3 = "SELECT * FROM expenses3"

        cursor.execute(sql3)
        
        rows = cursor.fetchall() 

        for x in rows:
            print('Wartosc [€]: ', x[0])
            print('Kategoria: ', x[1])
            print('Data: ', x[2])
            print('-' * 80)
            print()

        cursor.close()

    except sqlite3.Error as e:
        print('Blad, sprobuj ponownie. ', e)

    finally:
        if (db):
            db.close()
            print('Lista wydatkow zostala pomyslnie wczytana. ')


# Adding a new expense
def add_expense(month):
    print()
    id = 0
    try:
        expense_value = int(input('Podaj kwote wydatku [euro]: '))
        print()
        expense_cat = input('Podaj kategorie: [Jedzenie, Chemia, Auto, Mieszkanie, Sparkonto, etc.] ')
        
        expense = (expense_value, expense_cat, month)
        expenses.append(expense)

        db = sqlite3.connect('expenses3.db')

        sql = """INSERT INTO expenses3
            (value, category, date) 
            VALUES ('{}', '{}', '{}');""".format(
                expense_value, expense_cat, d)

        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        print('Zapisano w bazie!')
        id+= 1
        cursor.close()
    
    except ValueError:
        print()
        print('Wpisz poprawna kwote! ')
    else:
        print()
        print('Poprawnie dodano!')
        print()

        db.commit()
        db.close()

       
# Delete expenses
def delete_expenses(month):
    print(expenses)
    print()
    
    #try:
    #    user_delete = int(input('Wybierz pozycje do usuniecia [0,1,2,3 itd.] i nacisnij Enter: '))
    #    del expenses[user_delete]
    #    print()
    #    message = print('Pomyslnie usunieto ')
    #except ValueError:
    #    print()
    #    print('Wybierz poprawnie numer indeksu [Cyfra 0 oznacza pierwsza pozycje, cyfra 1 druga pozycje itd.]')
    #except IndexError:
    #    print()
    #    print('Wybierz poprawnie numer indeksu [Cyfra 0 oznacza pierwsza pozycje, cyfra 1 druga pozycje itd.]')
    #else:
    #    print(message)
    #    print()
    #    print(expenses)
    
    try:

        db = sqlite3.connect('expenses3.db')
        cursor = db.cursor()
    
        sql3 = '''DELETE FROM expenses3 WHERE rowid = ?;''', (id,)

        cursor.execute(sql3)
        rows = cursor.fetchall() 

        for x in rows:
            print('ID: ', x[1])
            print('Wartosc [€]: ', x[2])
            print('Kategoria: ', x[3])
            print('Data: ', x[4])
            print('-' * 80)
            print()

        cursor.close()

    except sqlite3.Error as e:
        print()
        print('Blad, sprobuj ponownie. ', e)
        print()

    finally:
        if (db):
            db.close()
            print('Lista wydatkow zostala pomyslnie wczytana. ')


# Statistics
def show_statistics(month):
   
    summ_value_month = sum(expense_value for expense_value, _, expense_month in expenses if expense_month == month)
    summ_all_expense = sum(expense_value for expense_value, _, _, in expenses)
    summ_all_income = sum(income_value for income_value, _, _, in incomes) 
    diff = summ_all_income - summ_all_expense

    print('Aktualny balans [€]: ', diff)
    print('Najdrozszy wydatek dotychczas [€]: ', max(expenses))
    print('Najwyzszy przychod dotychczas [€]: ', max(incomes))
    print('Laczna suma wydatkow w tym miesiacu wynosi [€]: ', summ_value_month)
    print('Laczna ilosc wydatkow w tym roku [€]: ', summ_all_expense)


# Add Income
def add_income(month):

    id2 = 0

    try:
        income_value = int(input('Wpisz wartosc przychodu [€]: '))
        print()
        income_cat = input('Wpisz zrodlo przychodu: ')

        income = (income_value, income_cat, month)
        incomes.append(income)
    
        db2 = sqlite3.connect('incomes.db')

        sql2 = """INSERT INTO incomes
            (value, category, date) 
            VALUES ('{}', '{}', '{}');""".format(
                income_value, income_cat, d)

        cursor2 = db2.cursor()
        cursor2.execute(sql2)
        db2.commit()
        print()
        print('Zapisano w bazie!')
        id2+= 1
        cursor2.close()

    except ValueError:
        print()
        print('Wpisz poprawna kwote! ')
    else:
        print()
        print('Poprawnie dodano!')
        print()


# Show Incomes
def get_incomes(month):
    #for income_value, income_cat, income_month in incomes:
    #    if income_month == month:
    #        print(f'{income_value }€ - {income_cat} - {d}')

    try:
        db2 = sqlite3.connect('incomes.db')
        cursor = db2.cursor()

        sql4 = "SELECT * FROM incomes"

        cursor.execute(sql4)
        
        rows = cursor.fetchall() 

        for x in rows:
            print('Wartosc [€]: ', x[0])
            print('Kategoria: ', x[1])
            print('Data: ', x[2])
            print('-' * 80)
            print()

        cursor.close()

    except sqlite3.Error as e:
        print('Blad, sprobuj ponownie. ', e)

    finally:
        if (db2):
            db2.close()
            print('Lista przychodow zostala pomyslnie wczytana. ')


# Main while
#TASK - by user_input '123231313' does not returning to beginning
while True:
    try:
        year = int(input('Podaj rok: '))
        print()
        month = int(input("Podaj miesiac [1-12]: "))
        print()
        day = int(input('Podaj dzien: '))
        print()

        d = date(year, month, day)
        print(d)

        if month == 0:
            break
    except ValueError: 
            print('Wybrano bledny miesiac!')
        
        
# Secondary while
    while True:
        print()
        print("0. Powrót do wyboru daty")
        print("1. Przeglądaj wydatki")
        print("2. Dodaj wydatek")
        print("3. Usuń wydatek")
        print("4. Przegladaj przychody")
        print("5. Dodaj przychod")
        print("6. Statystyki")
        print("7. Zamknij program")
        print()
        
        try:
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
                print('Przeglad aktualnych przychodow')
                print('------------------------------')
                print()
                get_incomes(month)

            if user_choice == 5:
                print('Dodaj nowy przychod')
                print('------------------------------')
                print()
                add_income(month)
        
            if user_choice == 6:
                print("Statystyki")
                print("------------------------------")
                print()
                show_statistics(month)
        
            if user_choice == 7:
                sys.exit(0)
       
        except ValueError:
            print('Wybierz poprawnie pozycje!')
