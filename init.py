import psycopg2
# http://initd.org/psycopg/docs/usage.html


# Drop table person
def dropTable(name, cur):
    string = 'DROP TABLE ' + name + ";"
    cur.execute(string)  
    return

# Execute a command: this creates a new table
def mkPerson(cur):
    cur.execute("CREATE TABLE Person (  id serial PRIMARY KEY,  \
                                        name varchar,           \
                                        age integer,            \
                                        gender char);")
    i = 1
    while i < 11:
        cur.execute("INSERT INTO person (id, name, age, gender) VALUES (%s, %s, %s, %s)",
        (i, "Person" + str(i), 30+i, gender(i))
        )
        i += 1
    return

def mkPatient(cur):
    cur.execute("SELECT * FROM person;")
    data = cur.fetchall()
    print data
    return

def gender(num):
    if (num%2 == 0):
        return "M"
    return "F" 


def main():
    # Connect to an existing database
    conn = psycopg2.connect("dbname=hospital user=postgres")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    dropTable('person', cur)
    mkPerson(cur)
    mkPatient(cur)
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()
    
if __name__ == '__main__':
    main()
