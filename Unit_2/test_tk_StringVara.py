from tkinter import *

import _thread
import time


def changeItems():
    global cnames
    time.sleep(2)
    cnames.set("changed")
    print("change")
    

root = Tk() 
root.geometry('+400+200') 
root.minsize(400,200) 
root.title("test")

tnames = 'python','TCL','ruby'

cnames = StringVar()

cnames.set(tnames)

l = Listbox(root, listvariable = cnames,height = 10).grid() 

ttk.Button(root,text = "submit",command = changeItems).grid() 

root.mainloop()

# cnames.set("changed")
#_thread.start_new_thread( changeItems, ("Thread-1", 2, ) )
