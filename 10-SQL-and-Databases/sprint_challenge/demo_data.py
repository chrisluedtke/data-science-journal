import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

curs = conn.cursor()

curs.execute("""
CREATE TABLE IF NOT EXISTS data (
    s text,
    x int,
    y int
)
""")

data = [['g', 3, 9],
        ['v', 5, 7],
        ['f', 8, 7]]

for row in data:  
    curs.execute(f"""
    INSERT INTO data
    VALUES ({str(row)[1:-1]})
    """)

conn.commit()

"""Count how many rows you have - it should be 3!"""
n_rows = curs.execute("SELECT COUNT(*) FROM data").fetchall()

"""How many rows are there where both x and y are at least 5?"""
n_rows_ge5 = curs.execute("""
SELECT COUNT(*) 
FROM data
WHERE x>=5
AND y>=5
""").fetchall()

"""How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?"""
n_dist_y = curs.execute("""
SELECT COUNT(DISTINCT(y))
FROM data 
""").fetchall()