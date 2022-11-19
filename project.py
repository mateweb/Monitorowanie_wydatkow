import sys
import sqlite3
import datetime

from datetime import date, datetime

# Variables

expenses = []
incomes = []
id = 0
id2 = 0

# PrintingAllExpenses
def get_expenses(month):
    
    try:

        db = sqlite3.connect('expenses_and_incomes.db')
        cursor = db.cursor()

        sql3 = "SELECT * FROM expenses"

        cursor.execute(sql3)
        
        rows = cursor.fetchall() 

        for x in rows:
            print('ID: ', x[0])
            print('Wartosc [€]: ', x[1])
            print('Kategoria: ', x[2])
            print('Data: ', x[3])
            print('-' * 80)
            print()

        cursor.close()

    except sqlite3.Error as e:
        print('Blad, sprobuj ponownie. ', e)

    finally:
        if (db):
            db.close()
            print('Lista wydatkow zostala pomyslnie wczytana. ')


# AddingANewExpense
def add_expense(month):
    print()
    id = 0
    try:
        expense_value = int(input('Podaj kwote wydatku [euro]: '))
        print()
        expense_cat = input('Podaj kategorie: [Jedzenie, Chemia, Auto, Mieszkanie, Sparkonto, etc.] ')
        print()
        
        expense = (expense_value, expense_cat, month)
        expenses.append(expense)

        db = sqlite3.connect('expenses_and_incomes.db')

        sql = """INSERT INTO expenses
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
        print()
    else:
        print()
        print('Poprawnie dodano!')
        print()

        db.commit()
        db.close()

       
# DeleteExpenses
def delete_expenses(month):
    
    try:
         
        db = sqlite3.connect('expenses_and_incomes.db') 
        userInput = int(input("Wpisz ID do usuniecia: "))
        print()
        cursor = db.cursor()

        cursor.execute(f'DELETE FROM expenses WHERE id= {userInput}')
        cursor.close()
        db.commit()
        db.close()
        

    except sqlite3.Error as e:
        print('Blad, sprobuj ponownie. ', e)
        print()

    finally:
        if (db):
            db.close()
            print('Pomyslnie usunieto. ') 


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


# AddIncome
def add_income(month):

    id = 0
    try:
        income_value = int(input('Wpisz wartosc przychodu [€]: '))
        print()
        income_cat = input('Wpisz zrodlo przychodu: ')

        income = (income_value, income_cat, month)
        incomes.append(income)
    
        db = sqlite3.connect('expenses_and_incomes.db')

        sql2 = """INSERT INTO incomes
            (value, category, date) 
            VALUES ('{}', '{}', '{}');""".format(
                income_value, income_cat, d)

        cursor2 = db.cursor()
        cursor2.execute(sql2)
        db.commit()
        print()
        print('Zapisano w bazie!')
        id+= 1
        cursor2.close()

    except ValueError:
        print()
        print('Wpisz poprawna kwote! ')
    else:
        print()
        print('Poprawnie dodano!')
        print()


# ShowIncomes
def get_incomes(month):
   
    try:
        db = sqlite3.connect('expenses_and_incomes.db')
        cursor2 = db.cursor()

        sql4 = "SELECT * FROM incomes"

        cursor2.execute(sql4)
        
        rows2 = cursor2.fetchall() 

        for x in rows2:
            print('ID: ', x[0])
            print('Wartosc [€]: ', x[1])
            print('Kategoria: ', x[2])
            print('Date: ', x[3])
            print('-' * 80)
            print()

        cursor2.close()

    except sqlite3.Error as e:
        print('Blad, sprobuj ponownie. ', e)

    finally:
        if (db):
            db.close()
            print('Lista przychodow zostala pomyslnie wczytana. ')

# DeleteIncomes
def deleteIncomes(month):

    try:
         
        db = sqlite3.connect('expenses_and_incomes.db') 
        userInput2 = int(input("Wpisz ID do usuniecia: "))
        print()
        cursor2 = db.cursor()

        cursor2.execute(f'DELETE FROM incomes WHERE id= {userInput2}')
        cursor2.close()
        db.commit()
        db.close()
        

    except sqlite3.Error as e:
        print('Blad, sprobuj ponownie. ', e)
        print()

    finally:
        if (db):
            db.close()
            print('Pomyslnie usunieto. ') 


# MainWhile
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
            print()
            print('Wybrano bledny miesiac! Powroc do wyboru miesiaca.')
            print()
            continue
            
        
# Secondary while
    while True:
        print()
        print("0. Powrót do wyboru daty")
        print("1. Przeglądaj wydatki")
        print("2. Dodaj wydatek")
        print("3. Usuń wydatek")
        print("4. Przegladaj przychody")
        print("5. Dodaj przychod")
        print("6. Usun przychod")
        print("7. Statystyki")
        print("8. Zamknij program")
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
                print('Usun przychod')
                print('------------------------------')
                print()
                deleteIncomes(month)
        
            if user_choice == 7:
                print("Statystyki")
                print("------------------------------")
                print()
                show_statistics(month)
        
            if user_choice == 8:
                sys.exit(0)
       
        except ValueError:
            print('Wybierz poprawnie pozycje!')
