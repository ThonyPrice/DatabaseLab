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

def insertPatient(cur, teamId, pdata, time):
    cur.execute("INSERT INTO Queue \
        (teamID, name, age, gender, issue, priority, timestmp) \
        VALUES (%s, %s, %s, %s, %s, %s, %s)", 
        (teamId, pdata[0], int(pdata[1]), pdata[2], pdata[4], int(pdata[3]), time)
    )
    return

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
    # Get patient information that was filled in
    pdata = app1.data
    # Check which teams are able to treat a patients issue
    teamIds = getTeam(cur, pdata[4]) # pdata[4] is issue of a patient
    # Get queues of those teams
    queues = getQueues(cur, teamIds)
    # Prompt nurse to select a queue
    q_data = app1.showQueues(queues)
    app1.showTimeBtns(q_data, pdata[3]) # pdata[3] is priority of a patient
    app1.mainloop()
    teamq = app1.to_team
    # Insert patient into queue
    time = '15:30' # This is the time our patients is logged in the system
    insertPatient(cur, teamq, pdata, time)
    print '--- EOF ---'
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
