import random
import datetime
import psycopg2
# http://initd.org/psycopg/docs/usage.html
import tkinter_test as app
import doctor_form as doctor
import report_form as report

# Return list of existing issues from db
def gtIssues(cur):
    cur.execute("SELECT DISTINCT issue FROM Treatments;")
    return [issue[0] for issue in cur.fetchall()]

# Find teamID's that can treat given issue
def getTeam(cur, issue):
    teamId = cur.execute( "SELECT teamid FROM Team WHERE issue1 = %(issue)s \
                        OR issue2 = %(issue)s OR issue3 = %(issue)s",
        {'issue': issue})
    return [teamID[0] for teamID in cur.fetchall()]

# Return a list of all queues with given id's
def getQueues(cur, ids):
    q = []
    for i in ids:
        cur.execute("SELECT * FROM Queue WHERE teamID = %(id)s \
            ORDER BY priority DESC;", {'id': i})
        q.append(cur.fetchall())
    return q

# Insert patient into relation Queue
def insertPatient(cur, teamId, pdata, time):
    cur.execute("INSERT INTO Queue \
        (personid, teamID, name, age, gender, issue, priority, timestmp) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
        (pdata[5], teamId, pdata[0], int(pdata[1]), pdata[2], pdata[4], int(pdata[3]), time)
    )
    return

# Remove patient from queue
def rmPatient(cur, pId):
    cur.execute("DELETE FROM Queue WHERE personid = %(pId)s;", {'pId': pId})
    return

# Get a treatments for a given issue
def getTreatments(cur, issue):
    cur.execute("SELECT treatment FROM Treatments WHERE issue = %(issue)s",
        {'issue': issue})
    return [treatment[0] for treatment in cur.fetchall()]

# Get a list of all drugs
def getDrugs(cur):
    cur.execute("SELECT drug FROM Drugs")
    return [drug[0] for drug in cur.fetchall()]

# Insert all data necessary into the relation patientLog
def fillLog(cur, pid, name, age, issue, treat, drugs, 
            waittime, home, timestmp, totCost):
    cur.execute("INSERT INTO patientLOG \
        (personid, name, age, issue, treat, drugs, waittime, home, timee, totCost) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (str(pid), name, age, issue, treat, drugs, waittime, home, timestmp, totCost))
    return

# Return the total cost of pills and treatments
def getCost(cur, ListOfPills, treatments):
    cost = 0
    for i in ListOfPills:
        cur.execute("SELECT cost FROM Drugs WHERE drug = %(i)s",
            {'i': i})
        cost += int(cur.fetchall()[0][0])
    for j in treatments:
        cur.execute("SELECT cost FROM Treatments WHERE treatment = %(j)s",
            {'j': j})
        cost += int(cur.fetchall()[0][0])
    return cost

# Run file from here
def main():
    
    # Connect to an existing database and open a cursor
    conn = psycopg2.connect("dbname=hospital user=postgres")
    cur = conn.cursor()
    # Collect current issues from db
    issue_list = gtIssues(cur)
    
    # Create tkinter Nurse's form window
    app1 = app.Application(issue_list)
    app1.mainloop()
    # Get patient information that was filled in
    pdata = app1.data
    # Check which teams are able to treat a patients issue
    # pdata[4] is issue of a patient
    teamIds = getTeam(cur, pdata[4]) 
    # Get queues of those teams
    queues = getQueues(cur, teamIds)
    # Prompt nurse to select a queue
    q_data = app1.showQueues(queues)
    # pdata[3] is priority of a patient
    app1.showTimeBtns(q_data, pdata[3]) 
    app1.mainloop()
    # Get the teamID that the nurse selected
    teamq = app1.to_team
    app1.destroy()
    
    # Insert patient into queue and record which time that occurs
    time = str(datetime.datetime.now().time())[:5] 
    insertPatient(cur, teamq, pdata, time)
    conn.commit()
    
    # Open doctors form
    app2 = doctor.Application()
    # Put patient information in a tuple
    patient_tup = (teamq, pdata[0], pdata[1], pdata[2], pdata[4], pdata[3], time)
    # Show patient info in doc_form
    app2.showPatientInfo(patient_tup)
    # Get treatments for patients issue
    treats = getTreatments(cur, patient_tup[4])
    app2.showTreatments(treats)
    drugs = getDrugs(cur)
    app2.showDrugs(drugs)
    app2.mainloop()
    app2.destroy()
    
    # remove patient from queue
    rmPatient(cur, pdata[5])
    conn.commit()
    
    # Get the data froc doctors form
    prescribed_treats = app2.treatments
    prescribed_drugs = app2.drugs
    cost = getCost(cur, prescribed_drugs, prescribed_treats)

    fillLog(cur, pdata[5], pdata[0], pdata[1], pdata[4],', '.join(prescribed_treats), 
        ', '.join(prescribed_drugs), app1.time, app2.home ,time, cost)
    rep = report.Application([pdata[5], pdata[0], pdata[1], pdata[4],
        ', '.join(prescribed_treats), ', '.join(prescribed_drugs), app1.time, 
        app2.home , time, cost])
    rep.mainloop()
    
    # Make the changes to the database persistent and close communication
    conn.commit()
    cur.close()
    conn.close()
    print '--- EOF ---'

# Run file from main module
if __name__ == '__main__':
    main()
