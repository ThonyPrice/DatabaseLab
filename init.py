import random
import psycopg2
# http://initd.org/psycopg/docs/usage.html
import tkinter_test as app
import tkinter_nurs2 as app2


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
                                        gender char,            \
                                        issue varchar,          \
                                        priority integer);")
    for i in range(1, 11):
        cur.execute("INSERT INTO person (id, name, age, gender, issue, priority) \
                    VALUES (%s, %s, %s, %s, %s, %s)",
                    (i, "Person" + str(i), 30+i, gender(i), i,
                    random.randrange(1,6))
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
        (i, "Head" + str(i), str(issues[random.randrange(10)]),
        str(issues[random.randrange(10)]), str(issues[random.randrange(10)])))
    return

def gender(num):
    if (num%2 == 0):
        return "M"
    return "F"

def mkTreatments(cur):
    cur.execute("CREATE TABLE Treatments(   issue varchar,  \
                                            treatment varchar);")

    treats = ['Rest', 'Surgery', 'Drip', 'Acupunctur', 'Spa tretment',
            'Lobotomize', 'Marijuana', 'Exercise', 'Gastric bypass', 'Insulin treatment',
            'Autopsy', 'Biopsy', 'Blood test', 'CAT-scan', 'X-ray',
            'Teeth brushing', 'Colesterole test', 'Condoms', 'Dialysis', 'EKG',
            'ER-treatment', 'Eye operation', 'Facelift', 'Vaccination', 'Hair removal',
            'Hard surgery', 'Iron lung', 'MRI-scan', 'Nerve operation', 'Nose job']
    for i in range(len(issues)):
        cur.execute("INSERT INTO Treatments (issue, treatment) VALUES (%s, %s)",
        (str(issues[i]), str(treats[i])))
        cur.execute("INSERT INTO Treatments (issue, treatment) VALUES (%s, %s)",
        (str(issues[i]), str(treats[i+10])))
        cur.execute("INSERT INTO Treatments (issue, treatment) VALUES (%s, %s)",
        (str(issues[i]), str(treats[i+20])))
    return

def gtIssues(cur):
    cur.execute("SELECT DISTINCT issue FROM Treatments;")
    res_list = []
    for row in cur.fetchall():
        res_list += [row[0]]
    return res_list

def mkQueue(cur):
    cur.execute("CREATE TABLE Queue(    patientId serial PRIMARY KEY,   \
                                        teamID serial,                  \
                                        tstamp int,                     \
                                        priority int)")
    return


def getTeam(cur, data):
    skill = data[4]
    team = cur.execute("SELECT teamid from Team WHERE skill1 == "+ "'" +skill+ "+"'"+ OR skill2 == "+skill+" OR skill3 == "+skill)
    return team

def getQue(cur, team):
    que = cur.execute("SELECT * from Que WHERE teamid == "+team)
    return que


issues = ['Headace', 'Concussion', 'Cancer', 'Dehydration', 'Broken bone',
        'Allegric', 'Obesity', 'Anorectic', 'Paranoia', 'Snake bite']

def main():
    # Connect to an existing database
    conn = psycopg2.connect("dbname=hospital user=postgres")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    dropTable('person', cur)
    mkPerson(cur)
    dropTable('team', cur)
    mkTeam(cur)
    dropTable('treatments', cur)
    mkTreatments(cur)
    dropTable('Queue', cur)
    mkQueue(cur)
    issue_list = gtIssues(cur)
    # Make the changes to the database persistent
    conn.commit()
    # mkPatient(cur) This might not be necessary
    # Create tkinter Nurse's form window
    app1 = app.Application(issue_list)
    app1.mainloop()
    print(app1.data)
    team = getTeam(cur, app1.data)
    print(team)
    que = getQue(cur, team)
    print(que)




    #app2 = app.Application(queue)
    #app2.mainloop()


    # Close communication with the database
    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
