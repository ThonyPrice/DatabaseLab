import random
import psycopg2
# http://initd.org/psycopg/docs/usage.html
import tkinter_test as app
import doctor_form as doctor


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

def getPatient(cur, teamid):
    cur.execute("SELECT * FROM Queue WHERE teamID = %(teamid)s \
    AND priority = (SELECT MAX(Priority) FROM Queue WHERE teamID = %(teamid)s) \
    AND Timestmp = (SELECT MIN(timestmp) FROM Queue WHERE teamID = %(teamid)s\
    AND priority = (SELECT MAX(Priority) FROM Queue WHERE teamID = %(teamid)s))", {'teamid': teamid})
    return [x for x in cur.fetchall()]

def getTreatments(cur, issue):
    cur.execute("SELECT treatment FROM Treatments WHERE issue = %(issue)s", 
        {'issue': issue})
    return [x[0] for x in cur.fetchall()]

def getDrugs(cur):
    cur.execute("SELECT drug FROM Drugs")
    return [x[0] for x in cur.fetchall()]


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
    app1.destroy()
    # Insert patient into queue
    time = '15:30' # This is the time our patients is logged in the system
    insertPatient(cur, teamq, pdata, time)
    # Open doctors form
    app2 = doctor.Application()
    app2.mainloop()
    teamid = app2.team # Get choosen teamId
    # Collect patient first in given teamId's queue
    patient = getPatient(cur, teamid) 
    # Put patient information in a tuple
    patient_tup = patient[0]
    print "Issue", patient_tup[4]
    # Show patient info in doc_form
    app2.showPatientInfo(patient_tup)
    # Get treatments for patients issue
    treats = getTreatments(cur, patient_tup[4])
    app2.showTreatments(treats)
    app2.mainloop()
    # Get the ordinated treats
    prescribed_treats = app2.treatments
    drugs = getDrugs(cur)
    print "Drugs", drugs

    print '--- EOF ---'
    # Make the changes to the database persistent
    conn.commit()
    # Close communication with the database
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
