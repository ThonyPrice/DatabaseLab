# This class represents a interface for doctors where a user can select
#   which medical team he/she belong to, see a patients information,
#   select treatments and drugs then send patient home or to further care.

#!/usr/bin/env python
import Tkinter as tk
import datetime

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.treatments = []
        self.drugs = []
        self.home = None
        self.quitButton = tk.Button(self, text='Enter',
            command=self.quit).grid(row=26, column=2)

    def slctTeam(self):
        tk.Label(self, text='Which MedTeam:').grid(row=0)
        for i in range(5):
            tk.Button(self, text=str(i+1),
                command= lambda val = str(i+1): self.setTeam(str(val))).grid(row=0, column=1+i)
        self.quitButton = tk.Button(self, text='Enter',
            command=self.quit)
        self.quitButton.grid(row=26, column=2)

    def setTeam(self, val):
        self.team = val

    def showPatientInfo(self, data):
        tk.Label(self, text='DOCTORS FORM:').grid(row=2)
        tk.Label(self, text='Patient\'s name:').grid(row=3)
        tk.Label(self, text='%s' % str(data[1])).grid(row=3, column=1)
        tk.Label(self, text='Patient\'s age:').grid(row=4)
        tk.Label(self, text='%s' % str(data[2])).grid(row=4, column=1)
        tk.Label(self, text='Patient\'s gender:').grid(row=5)
        tk.Label(self, text='%s' % str(data[3])).grid(row=5, column=1)
        tk.Label(self, text='Patient\'s issue:').grid(row=6)
        tk.Label(self, text='%s' % str(data[4])).grid(row=6, column=1)

    def showTreatments(self, treats):
        tk.Label(self, text='CHOOSE TREATMENT(S):').grid(row=7)
        for i in range(len(treats)):
            tk.Button(self, text=treats[i],
                command= lambda val = treats[i]: self.addTreat(val)).grid(row=8+i, column=1)

    def showDrugs(self, drugs):
        tk.Label(self, text='CHOOSE DRUG(S):').grid(row=11)
        for i in range(len(drugs)):
            tk.Button(self, text=drugs[i],
                command= lambda val = drugs[i]: self.addDrug(val)).grid(row=12+i, column=1)
        self.sndBtns()

    def addTreat(self, treatment):
        self.treatments.append(treatment)

    def addDrug(self, drug):
        self.drugs.append(drug)

    def sndBtns(self):
        tk.Label(self, text='SEND PATIENT:').grid(row=23)
        tk.Button(self, text='Home',
            command= lambda val = 'y': self.setSend(val)).grid(row=24, column=1)
        tk.Button(self, text='Ordinate further care',
            command= lambda val = 'n': self.setSend(val)).grid(row=25, column=1)

    def setSend(self, val):
        self.home = val
