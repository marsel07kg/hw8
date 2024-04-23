import sqlite3

with sqlite3.connect('students.db') as conn:
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    hobbi TEXT,
    year_of_birth DATE,
    point_for_hw INTEGER
    )""")

    cur.execute('''UPDATE student SET name = 'genius' WHERE point_for_hw = 10''')

    cur.execute("""DELETE FROM student WHERE id % 2 = 0 """)

    cur.execute('''SELECT * FROM student WHERE length(surname) >= 10''')

    # cur.execute('''SELECT * FROM student''')
    for i in cur:
        print(i)


