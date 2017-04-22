import random
import psycopg2
# http://initd.org/psycopg/docs/usage.html
import tkinter_test as app


# Return list of existing issues from db
def gtIssues(cur):
    cur.execute("SELECT DISTINCT issue FROM Treatments;")
    return [x[0] for x in cur.fetchall()]


# Find teamID's that can treat given issue
def getTeam(cur, issue):
    teamId = cur.execute( "SELECT teamid FROM Team WHERE issue1 = %(issue)s \
                        OR issue2 = %(issue)s OR issue3 = %(issue)s", 
        {'issue': issue})
    return [x[0] for x in cur.fetchall()]


# Return a list of all queues with given id's    
def getQueues(cur, ids):
    q = []
    for i in ids:
        cur.execute("SELECT * FROM Queue WHERE teamID = %(id)s \
            ORDER BY priority DESC;", {'id': i})
        q.append(cur.fetchall())
    return q


def main():
    # Connect to an existing database
    conn = psycopg2.connect("dbname=hospital user=postgres")
    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Collect current issues from db
    issue_list = gtIssues(cur)
    # Create tkinter Nurse's form window
    app1 = app.Application(issue_list)
    app1.mainloop()
    print(app1.data)
    teamIds = getTeam(cur, app1.data[4]) # data[4] is issue of a patient
    queues = getQueues(cur, teamIds)
    app1.showQueues(queues)
    app1.mainloop()
    print '--- EOF ---'
    # Make the changes to the database persistent
    # conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
