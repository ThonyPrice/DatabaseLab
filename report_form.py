# This class should be called with a patients hospital data
# and shows is as an report.

#!/usr/bin/env python
import Tkinter as tk




class Application(tk.Frame):
    def __init__(self, info, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.displayLabels()
        self.displayInfo(info)

    def displayLabels(self):
        tk.Label(self, text='PATIENT REPORT:').grid(row=0)
        tk.Label(self, text='Name:').grid(row=1)
        tk.Label(self, text='Age:').grid(row=2)
        tk.Label(self, text='Issue:').grid(row=3)
        tk.Label(self, text='Treatments:').grid(row=4)
        tk.Label(self, text='Drugs:').grid(row=5)
        tk.Label(self, text='Waiting time (minutes):').grid(row=6)
        tk.Label(self, text='Sent home or not (y/n):').grid(row=7)
        tk.Label(self, text='Total cost:').grid(row=8)
        tk.Button(self, text='Quit', command=self.quit).grid(row=10, column=1)

    def displayInfo(self, info):
        for i in range(len(info)):
            tk.Label(self, text=str(info[i])).grid(row=1+i, column=1)
