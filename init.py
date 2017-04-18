
import psycopg2

# http://initd.org/psycopg/docs/usage.html

# Connect to an existing database
conn = psycopg2.connect("dbname=hospital user=postgres")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
names = ["Ann", "Bob", "Chris", "Diane", "Eric", "Fiona", "Gary", "Niklas"]
nameId = 3000
for name in names:
    cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)",
    (nameId, name)
    )
    nameId += 1

# Query the database and obtain data as Python objects
var = cur.execute("SELECT * FROM test;")
cur.fetchone()
(1, 100, "abc'def")


# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()