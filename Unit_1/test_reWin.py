from tkinter import *

import _thread
import time

root = Tk() 
cnames = StringVar()
isChecked = 0

def changeItems(cna,css):
    while True:
        global cnames,isChecked
        time.sleep(1)
        isChecked += 1
        #cnames.set("changed")
        print("change")
    
def getWin():
    global root,cnames,i
    root.geometry('+400+200') 
    root.minsize(400,200) 
    root.title("test")

    tnames = 'python','TCL','ruby'


    cnames.set(tnames)

    l = Listbox(root, listvariable = cnames,height = 10).grid() 

    ttk.Button(root,text = "submit",command = changeItems).grid()
    
    if i==1:
        print("i = 1")
    
    #root.mainloop()
    while True:
        global isChecked
        if isChecked%2==0:
            cnames.set("123")
        else:
            cnames.set("456")
            print("456")
        root.update()
        
        
# cnames.set("changed")
_thread.start_new_thread( changeItems, ("Thread-1", 2, ) )
getWin()


