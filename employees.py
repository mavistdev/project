# спасибо за курс! Хороших вам потоков что ли...

import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('employees.db')

# Создание таблицы
conn.execute('''CREATE TABLE IF NOT EXISTS employees
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 phone TEXT NOT NULL,
                 email TEXT NOT NULL,
                 salary REAL NOT NULL)''')

conn.commit()

#функция добавления сотрудников. На вход - имя, телефон, почта, зп
def add_employee(name, phone, email, salary):
    conn.execute("INSERT INTO employees (name, phone, email, salary) VALUES (?, ?, ?, ?)",
                (name, phone, email, salary))
    conn.commit()
    return 'Сотрудник успешно добавлен.'

#функция обновления сотрудников. На вход - айди, имя, телефон, почта, зп
def update_employee(id, name, phone, email, salary):
    conn.execute("UPDATE employees SET name = ?, phone = ?, email = ?, salary = ? WHERE id = ?",
                (name, phone, email, salary, id))
    conn.commit()
    return "Сотрудник успешно изменен."

#функция добавления сотрудников. На вход - айди
def delete_employee(id):
    conn.execute("DELETE FROM employees WHERE id = ?", (id,))
    conn.commit()
    return "Сотрудник успешно удален."

#функция добавления сотрудников. На вход - ФИО
def search_employee(name):
    cursor = conn.execute("SELECT * FROM employees WHERE name LIKE ?", (f'%{name}%',))
    return cursor.fetchall()

#вывод меню
def main_menu():
    print("1. Добавить сотрудника")
    print("2. Изменить сотрудника")
    print("3. Удалить сотрудника")
    print("4. Поиск по ФИО")
    print("5. Выйти")

#Меню добавления сотрудников
def add_employee_menu():
    name = input("Введите ФИО: ")
    phone = input("Введите номер телефона: ")
    email = input("Введите адрес электронной почты: ")
    salary = float(input("Введите заработную плату: "))
    print(add_employee(name, phone, email, salary))

#
def update_employee_menu():
    id = int(input("Введите ID сотрудника: "))
    name = input("Введите новое ФИО: ")
    phone = input("Введите новый номер телефона: ")
    email = input("Введите новый адрес электронной почты: ")
    salary = float(input("Введите новую заработную плату: "))
    print(update_employee(id, name, phone, email, salary))

def delete_employee_menu():
    id = int(input("Введите ID сотрудника: "))
    print(delete_employee(id))

def search_employee_menu():
    name = input("Введите ФИО сотрудника: ")
    result = search_employee(name)
    if result:
        print("Результаты поиска:")
        for employee in result:
            print(f"ID: {employee[0]}, ФИО: {employee[1]}, Телефон: {employee[2]}, Email: {employee[3]}, Заработная плата: {employee[4]}")
    else:
        print("Сотрудник не найден.")

def data_empty():
    cursor = conn.execute("SELECT * FROM employees ")
    resp = cursor.fetchall()
    if len(resp) != 0:
        return True
    else:
        return False

if __name__ == "__main__":
    if data_empty():
        pass
    else:
        print('Сотрудники не созданы')

while True:
    main_menu()
    choice = input("Введите номер пункта меню: ")
    if choice == "1":
        add_employee_menu()
    elif choice == "2":
        update_employee_menu()
    elif choice == "3":
        delete_employee_menu()
    elif choice == "4":
        search_employee_menu()
    elif choice == "5":
        break
    else:
        print("Неверный ввод. Попробуйте еще раз.")