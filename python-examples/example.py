import psycopg2
import psycopg2.extras

conn_string = "host='localhost' dbname='example' user='example' password='example'"

conn = psycopg2.connect(conn_string)
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM course WHERE capacity<=%(cap)s", {'cap': 25})

capacity = 25
semester = 'F18'


cursor.execute("SELECT * FROM course WHERE capacity<=%s AND semester=%s", [capacity, semester])
# cursor.execute("SELECT * FROM course")

records = cursor.fetchall()


for t in records:
    print(t['location'])

cursor.execute("INSERT INTO student VALUES('dave@example.com', 'Dave', 'MATH')")
conn.commit()