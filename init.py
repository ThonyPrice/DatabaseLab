import random
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
    for i in range(1, 11):
        cur.execute("INSERT INTO person (id, name, age, gender) VALUES (%s, %s, %s, %s)",
        (i, "Person" + str(i), 30+i, gender(i))
        )
    return

def mkPatient(cur):
    cur.execute("SELECT * FROM person;")
    data = cur.fetchall()
    return
    
def mkTeam(cur):
    cur.execute("CREATE TABLE Team (    teamId serial PRIMARY KEY,  \
                                        head varchar,               \
                                        skill1 varchar,             \
                                        skill2 varchar,             \
                                        skill3 varchar);")

    for i in range(1, 6):
        cur.execute("INSERT INTO Team (teamId, head, skill1, skill2, skill3) VALUES (%s, %s, %s, %s, %s)",
        (i, "Head" + str(i), str(random.randrange(1, 11)), 
        str(random.randrange(1, 11)), str(random.randrange(1, 11))))
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
    dropTable('team', cur)
    mkTeam(cur)
    mkPatient(cur)
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()
    
if __name__ == '__main__':
    main()
