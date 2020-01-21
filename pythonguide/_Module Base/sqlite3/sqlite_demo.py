import sqlite3
from pathlib import Path
from employee import Employee

# In memory Database
"""
conn = sqlite3.connect(':memory:') 
"""
path = Path.cwd() / Path("employees.db")
print(path)
conn = sqlite3.connect(path)

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#             first text,
#             last text,
#             pay integer
#             ) """)


def insert_emp(emp):
    with conn:  # commit auto
        c.execute(
            "INSERT INTO employees VALUES (:first, :last, :pay)",
            {"first": emp.first, "last": emp.last, "pay": emp.pay},
        )


def get_emps_by_name(lastname):
    c.execute(
        "SELECT * FROM employees WHERE last=:last", {"last": lastname}
    )  # no need to commit
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute(
            """UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
            {"first": emp.first, "last": emp.last, "pay": pay},
        )


def remove_emp(emp):
    with conn:
        c.execute(
            "DELETE from employees WHERE first = :first AND last = :last",
            {"first": emp.first, "last": emp.last},
        )


emp_1 = Employee("John", "Doe", 80000)
emp_2 = Employee("Jane", "Doe", 80000)

# insert_emp(emp_1)
# insert_emp(emp_2)

update_pay(emp_2, 95000)
# remove_emp(emp_2)
emps = get_emps_by_name("Doe")
print(emps)

# c.execute("INSERT INTO employees VALUES ('Corey', 'Schafer', 500000)")
# c.execute("INSERT INTO employees VALUES ('Mary', 'Schafer', 500000)")
# c.execute("INSERT INTO employees VALUES ('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay)) # <-- NE PAS FAIRE CA !
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay)) # <-- Ok ! Tuple

# conn.commit()

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay}) # <-- Ok ! Dictionnary

# conn.commit()

# c.execute("SELECT * FROM employees WHERE last='Schafer'")
# c.execute("SELECT * FROM employees WHERE last=?", ('Schafer',))

# print(c.fetchall())

# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})

# print(c.fetchall())
# print(c.fetchmany(5))
# print(c.fetchone())

# conn.commit()

conn.close()
