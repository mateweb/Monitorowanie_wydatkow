import sys
import sqlite3
import datetime
import os

from datetime import date, datetime
from string import ascii_letters

# Variables

expenses = []
incomes = []
id = 0

# PrintingAllExpenses
def get_expenses(month):
    # test comment
    try:
        os.system('clear')

        db = sqlite3.connect('expenses_and_incomes.db')
        cursor = db.cursor()

        sql3 = "SELECT * FROM expenses WHERE strftime('%m', date) = " +"'"+ str(month)+"'"

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
        try:
            expense_cat = input('Podaj kategorie: [Jedzenie, Chemia, Auto, Mieszkanie, Sparkonto, etc.] ')
            print()
            assert all(c in ascii_letters for c in expense_cat)

        except:
            print('Wpisz poprawna kategorie! ')

            
    
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
    os.system('clear')
    print('WYDATKI: ')
    print('---------------------------------------------------------------------------------------------')
    
    db = sqlite3.connect('expenses_and_incomes.db')
    cursor = db.cursor()
    
    sumExpenseMonth = ("SELECT sum(value) FROM expenses WHERE strftime('%m', date) = " +"'"+ str(month)+"'")
    cursor.execute(sumExpenseMonth)
    sumExpenseMonth = cursor.fetchone()[0]
    print('Suma wydatków w tym miesiacu:',sumExpenseMonth,'€')
    print()
    
    avgExpenseMonth = ("SELECT avg(value) FROM expenses WHERE strftime('%m', date) = " +"'"+ str(month)+"'")
    cursor.execute(avgExpenseMonth)
    avgExpenseMonth = cursor.fetchone()[0]
    print('Srednia wydatków w tym miesiacu:',int(avgExpenseMonth),'€')
    print()
    
    sumExpenses = ("SELECT sum(value) FROM expenses")
    cursor.execute(sumExpenses)
    sumExpenses = cursor.fetchone()[0]
    print('Suma wydatków w tym roku:',sumExpenses,'€')
    print()
    
    print()    
    print('PRZYCHODY: ')
    print('---------------------------------------------------------------------------------------------')
    
    sumIncomeMonth = ("SELECT sum(value) FROM incomes WHERE strftime('%m', date) = " +"'"+ str(month)+"'")
    cursor.execute(sumIncomeMonth)
    sumIncomeMonth = cursor.fetchone()[0]
    print('Suma przychodow w tym miesiacu:',sumIncomeMonth,'€')
    print()
    
    avgIncomeMonth = ("SELECT avg(value) FROM incomes WHERE strftime('%m', date) = " +"'"+ str(month)+"'")
    cursor.execute(avgIncomeMonth)
    avgIncomeMonth = cursor.fetchone()[0]
    print('Srednia przychodow w tym miesiacu:',int(avgIncomeMonth),'€')
    print()
    
    sumIncomes = ("SELECT sum(value) FROM incomes")
    cursor.execute(sumIncomes)
    sumIncomes = cursor.fetchone()[0]
    print('Suma przychodow w tym roku:',sumIncomes,'€')
    print()
    print()

    diffExpIncMonth = (sumIncomeMonth - sumExpenseMonth) 
    print('*********************************************************************************************')
    print()
    print('Aktualny balans wynosi:',diffExpIncMonth,'€')
    print()
    
    cursor.close()
    db.close()


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
        os.system('clear')
        db = sqlite3.connect('expenses_and_incomes.db')
        cursor2 = db.cursor()
        sql4 = ("SELECT * FROM incomes WHERE strftime('%m', date) = " +"'"+ str(month)+"'")
            # sumValueMonth = ("SELECT SUM(value) FROM expenses WHERE strftime('%m', date) = " +"'"+ str(currentMonth)+"'")
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


# TestDefinition
def testDefinition():
    pass


# MainWhile
while True:
    try:
        os.system('clear')
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
        print()
        print('9. testDefinition')
        print()
        
        try:
            user_choice = int(input("Wybierz pozycję z menu [0-9] i naciśnij Enter: "))
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

            if user_choice == 9:
                testDefinition()
       
        except ValueError:
            print('Wybierz poprawnie pozycje!')
