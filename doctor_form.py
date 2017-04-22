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
        self.team = None
        self.slctTeam()
    
    def slctTeam(self):
        tk.Label(self, text='Which MedTeam:').grid(row=0)
        for i in range(5):
            tk.Button(self, text=str(i+1),
                command= lambda val = str(i+1): self.setTeam(str(val))).grid(row=0, column=1+i)
        self.quitButton = tk.Button(self, text='Enter',
            command=self.quit)
        self.quitButton.grid(row=20, column=0)
        return

    def setTeam(self, val):
        self.team = val
    
    def showPatientInfo(self):
        tk.Label(self, text='MEDICAL TEAM:').grid(row=2)
        tk.Label(self, text='%s' % str(self.team)).grid(row=2, column=1)
        tk.Label(self, text='Patient\'s name:').grid(row=3)
        tk.Label(self, text='Patient\'s age:').grid(row=4)
        tk.Label(self, text='Patient\'s gender:').grid(row=5)
        tk.Label(self, text='Patient\'s issue:').grid(row=6)
    
    def showTreatments(self, treats):
        tk.Label(self, text='CHOOSE TREATMENT(S):').grid(row=7)
        tk.Label(self, text='%s' % str(treat[0])).grid(row=8, column=1)
        tk.Label(self, text='%s' % str(treat[1)).grid(row=9, column=1)
        tk.Label(self, text='%s' % str(treat[2)).grid(row=10, column=1)
    
    def showDrugs(self, drugs):
        tk.Label(self, text='CHOOSE DRUG(S):').grid(row=11)
        tk.Label(self, text='%s' % str(drugs[0])).grid(row=12, column=1)
        tk.Label(self, text='%s' % str(drugs[1)).grid(row=13, column=1)
        tk.Label(self, text='%s' % str(drugs[2)).grid(row=14, column=1)
    
    def sndBtns(self):
        # TODO
    
# This snippet should be used to initiate this class from init.py
    
# app2 = doctor.Application()
# app2.mainloop()
# team = app2.team
# print "Selected team:", team
# app2.showPatientInfo()
# app2.mainloop()
# print '--- NOT_EOF ----'    
