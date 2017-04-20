#!/usr/bin/env python   
import Tkinter as tk    

list_of_issues = [1,2,3,4,5,6,7,8,9,10]

class Application(tk.Frame):           
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.prio = None
        self.issue = None
        self.createWidgets()
    
    def createWidgets(self):
        name    = tk.StringVar()
        age     = tk.StringVar()
        gender  = tk.StringVar()
        self.name_field     = tk.Label(self, text='Enter patient\'s name:').grid(row=0)
        self.age_field      = tk.Label(self, text='Enter patient\'s age:').grid(row=1)
        self.gender_field   = tk.Label(self, text='Enter patient\'s gender:').grid(row=2)
        self.priotity_field = tk.Label(self, text='Select patient\'s priority:').grid(row=3)
        self.issue_field    = tk.Label(self, text='Select patient\'s issue:').grid(row=8)
        self.name_entry     = tk.Entry(self, textvariable=name).grid(row=0, column=1)
        self.age_entry      = tk.Entry(self, textvariable=age).grid(row=1, column=1)
        self.gender_entry   = tk.Entry(self, textvariable=gender).grid(row=2, column=1)
        for i in range(5):
            tk.Button(self, text=str(i+1), 
                command=lambda: self.setPrio(self.text)).grid(row=3+i, column=1)
        i = 0
        for issue in list_of_issues:
            self.insertButton = tk.Button(self, text=str(issue), 
                command=lambda: self.setIssue(str(issue))).grid(row=8+i, column=1)
            i += 1
        self.insertButton = tk.Button(self, text='Insert',
            command=lambda: self.getData(name, age, gender)).grid(row=19, column=0)
        
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)
        self.quitButton.grid(row=20, column=0)
    
    def setPrio(self, value):
        self.prio = value
    
    def setIssue(self, value):
        self.issue = value
    
    def getData(self, name, age, gender):
        name = name.get()
        age = age.get()
        gender = gender.get()
        print name, age, gender, self.prio, self.issue
        

app = Application()
app.master.title('Nurse\'s form') 
app.mainloop()