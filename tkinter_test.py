#!/usr/bin/env python
import Tkinter as tk
import datetime


class Application(tk.Frame):
    def __init__(self, list_of_issues, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.prio = None
        self.issue = None
        self.issues = list_of_issues
        self.createWidgets()
        self.timestamp = None
        self.data = None
        self.into_team = None
        self.time = None

    def createWidgets(self):
        pId     = tk.StringVar()
        name    = tk.StringVar()
        age     = tk.StringVar()
        gender  = tk.StringVar()
        self.name_field     = tk.Label(self, text='Enter patient\'s ID:').grid(row=0)
        self.name_field     = tk.Label(self, text='Enter patient\'s name:').grid(row=1)
        self.age_field      = tk.Label(self, text='Enter patient\'s age:').grid(row=2)
        self.gender_field   = tk.Label(self, text='Enter patient\'s gender:').grid(row=3)
        self.priotity_field = tk.Label(self, text='Select patient\'s priority:').grid(row=4)
        self.issue_field    = tk.Label(self, text='Select patient\'s issue:').grid(row=9)
        self.name_entry     = tk.Entry(self, textvariable=pId).grid(row=0, column=1)
        self.name_entry     = tk.Entry(self, textvariable=name).grid(row=1, column=1)
        self.age_entry      = tk.Entry(self, textvariable=age).grid(row=2, column=1)
        self.gender_entry   = tk.Entry(self, textvariable=gender).grid(row=3, column=1)
        for i in range(5):
            tk.Button(self, text=str(i+1),
                command= lambda val = str(i+1): self.setPrio(str(val))).grid(row=4+i, column=1)
        i = 0
        for issue in self.issues:
            tk.Button(self, text=str(issue),
                command= lambda val = str(issue): self.setIssue(val)).grid(row=9+i, column=1)
            i += 1

        self.insertButton = tk.Button(self, text='Insert',
            command=lambda: self.getData(name, age, gender, pId)).grid(row=20, column=0)
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid(row=21, column=0)

    def setPrio(self, value):
        self.prio = value

    def setIssue(self, value):
        self.issue = value

    def getData(self, name, age, gender, pId):
        self.timestamp = datetime.datetime.now().time()
        pId = pId.get()
        name = name.get()
        age = age.get()
        gender = gender.get()
        self.data = [name, age, gender, self.prio, self.issue, pId] # Removed timestamp for now

    def showQueues(self, queues):
        q_prios = []
        for i in range(len(queues)):
            prio_data = []
            t = tk.Text(self, width=80, height=10)
            for tupl in queues[i]:
                prio_data.append((tupl[1], tupl[6]))
                t.insert('end', str(tupl) + '\n')
            t.grid(row=23, column=1+i)
            q_prios.append(prio_data)
        return q_prios

    def showTimeBtns(self, q_prios, p_prio):
        i = 0
        for queue_priorities in q_prios:
            total = 0
            for priority in queue_priorities:
                if int(priority[1]) >= int(p_prio):
                    total += priority[1] * 10
            tk.Button(self, text=str(total),
                command=lambda val = priority[0], time = total: self.setTeam(val, time)).grid(row=25, column=1+i)
            i += 1

        return

    def setTeam(self, val, time):
        self.to_team = val
        self.time = time
