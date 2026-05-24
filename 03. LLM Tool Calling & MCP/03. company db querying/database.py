import sqlite3

connection = sqlite3.connect("company.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    salary INTEGER
)
""")

cursor.execute("DELETE FROM employees")

employees = [
    ("John", "Engineering", 90000),
    ("Alice", "HR", 60000),
    ("Bob", "Engineering", 95000),
    ("Emma", "Marketing", 70000),
]

cursor.executemany(
    """
INSERT INTO employees(name, department, salary)
VALUES (?, ?, ?)
""",
    employees,
)

connection.commit()
connection.close()

print("Database Ready")
