import sqlite3
import os
import tabulate

def show_menu():
    print('''
    1 - Add product.
    2 - Show products.
    3 - Close program.
    ''')

conn = sqlite3.connect("products.sqlite")
cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE products (id INT, name TEXT, price INT)")
    print("Procts table created. Welcome to the system.")
except sqlite3.OperationalError:
    print("Welcome again.")

while True:
    show_menu()
    option = input("Enter an option: ")

    if option == '1':
        while True:
            try:
                id = int(input("Insert product id: "))
            except ValueError:
                print("Product ID can only be an INT value.")
            else:
                break
        name = input("Insert product name: ")
        price = input("Insert product price: ")
        cursor.execute("INSERT INTO products VALUES (?, ?, ?)", (id, name, price))
        os.system("cls")
        conn.commit()
    
    if option == '2':
        cursor.execute("SELECT * FROM products")
        data = cursor.fetchall()
        print(tabulate.tabulate(data))
        input("Press enter to continue.")
        os.system("cls")
    if option == '3':
        break

print("Program finished.")

conn.close()