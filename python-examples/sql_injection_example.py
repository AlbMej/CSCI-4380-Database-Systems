import psycopg2
import psycopg2.extras

conn_string = "host='localhost' dbname='example' user='example' password='example'"

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

capacity = '25; SELECT * FROM information_schema.tables'

cursor.execute("SELECT * FROM course WHERE capacity=" + capacity)
records = cursor.fetchall()

for t in records:
    print(t)

# cursor.execute("INSERT INTO student VALUES('dave@example.com', 'Dave', 'MATH')")
# conn.commit()