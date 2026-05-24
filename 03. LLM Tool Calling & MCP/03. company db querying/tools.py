import sqlite3


def get_all_employees():
    connection = sqlite3.connect("company.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")

    data = cursor.fetchall()

    connection.close()

    return data


def get_employees_by_department(department):
    connection = sqlite3.connect("company.db")
    cursor = connection.cursor()

    query = f"SELECT * FROM employees WHERE department LIKE '%{department}%'"
    cursor.execute(query)

    data = cursor.fetchall()

    connection.close()

    return data


def get_high_salary_employees(min_salary):
    connection = sqlite3.connect("company.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees WHERE salary >= ?", (min_salary,))

    data = cursor.fetchall()

    connection.close()

    return data
