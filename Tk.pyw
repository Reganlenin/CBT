from tkinter import *
import ttk
win=Tk()
win["background"] = '#123'
home=ttk.Frame(win)
fresh=ttk.Frame(win)
home.grid(row=0, column=0)
fresh.grid(row=1, column=0)

win.mainloop()