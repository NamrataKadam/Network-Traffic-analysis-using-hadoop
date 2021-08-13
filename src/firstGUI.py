from Tkinter import *
import Tkinter as tk
import tkFont
import tkMessageBox
import Tkinter,tkFileDialog
import subprocess as sub
import os
win = Tk()


name2 = """IP Analysis"""
wip = Label(win,padx = 10,text=name2,state=DISABLED,font="bold")
wip.grid(row=6, column=0)

Bhostcounttxt = Button(win,text="      Host Count      ",state=DISABLED,command=lambda: sub.call('/home/a/job.sh'))
Bhostcounttxt.grid(row=7, column=0)		
Bflowtxt = Button(win,text=" Flow Statistics ",state=DISABLED)
Bflowtxt.grid(row=7, column=2)		
Bgrpbytxt = Button(win,text="     Count By Grouping     ",state=DISABLED)
Bgrpbytxt.grid(row=7, column=7)	

#application analysis
name3 = """Application Analysis"""
wapp = Label(win,padx = 10,text=name3,state=DISABLED,font="bold")
wapp.grid(row=8, column=0)

Bwebusetxt = Button(win,text="Web Usage Pattern",state=DISABLED)
Bwebusetxt.grid(row=9, column=0)		
Bwebpoptxt = Button(win,text="Web Popularity",state=DISABLED)
Bwebpoptxt.grid(row=9, column=2)		
Bfileextxt = Button(win,text="Analysis By File Extension",state=DISABLED)
Bfileextxt.grid(row=9, column=7)

#flow analysis
name4 = """Flow Analysis"""
wflow = Label(win,padx = 10,text=name4,state=DISABLED,font="bold")
wflow.grid(row=10, column=0)

BAgrflowtxt = Button(win,text="   Aggregate Flow   ",state=DISABLED)
BAgrflowtxt.grid(row=11, column=0)		
Btopntxt = Button(win,text="       TOP N       ",state=DISABLED)
Btopntxt.grid(row=11, column=2)	

#LABLE
name = """Internet Traffic Analysis"""
w1 = Label(win,padx = 10,text=name)
w1.grid(row=0, column=0)
w1.grid(row=0,column=0,columnspan=2,pady=5,padx=5)

#ENTRY 
name1 = """Input"""
w2 = Label(win,padx = 10,text=name1)
w2.grid(row=1, column=0)
w2.grid(row=1,column=0,columnspan=2,pady=5,padx=5)

v = StringVar()
e = Entry(win,textvariable=v)
e.grid(row=2, column=0)
e.grid(row=2,column=0,columnspan=2,pady=5,padx=5)

#File Browser
def file_browser():
	file = tkFileDialog.askopenfile(parent=win,initialdir='/home/	a',title='Choose a file')
    	path=file.name
    	print(path)
	v.set(path)
	e.configure(state='disable')
#BROWZ BUTTON
b3 = Button(win,text="BROWZ",command=file_browser)
b3.grid(row=2, column=2)



	
#Second PART

#DDLIST
#name1 = """ITA"""
#var = tk.StringVar(win)
#var.set('IP')
#lst1 = ['IP','Application','Flow analysis']
#w3 =OptionMenu(win, var, *lst1)
#w3.grid(row=3, column=0)
			

def onselect(evt):
	print lb1.curselection()
	w = evt.widget
    	index = int(w.curselection()[0])
    	value = w.get(index)
    	print 'You selected item %d: "%s"' % (index, value)
        if value == 'IP Analysis':
		Bhostcounttxt['state']='normal'
		Bflowtxt['state']='normal'
		Bgrpbytxt['state']='normal'
		wip['state']='normal'
		
		Bwebusetxt['state']='disabled'
		Bwebpoptxt['state']='disabled'
		Bfileextxt['state']='disabled'
		BAgrflowtxt['state']='disabled'
		Btopntxt['state']='disabled'
		wapp['state']='disabled'
		wflow['state']='disabled'
	
                
	if value == 'Application Analysis':
		Bwebusetxt['state']='normal'
		Bwebpoptxt['state']='normal'
		Bfileextxt['state']='normal'
		wapp['state']='normal'
		
		Bhostcounttxt['state']='disabled'
		Bflowtxt['state']='disabled'
		Bgrpbytxt['state']='disabled'
		BAgrflowtxt['state']='disabled'
		Btopntxt['state']='disabled'
		wflow['state']='disabled'
		wip['state']='disabled'
		

	if value == 'Flow Analysis':
		BAgrflowtxt['state']='normal'
		Btopntxt['state']='normal'
		wflow['state']='normal'

		Bhostcounttxt['state']='disabled'
		Bflowtxt['state']='disabled'
		Bgrpbytxt['state']='disabled'
		Bwebusetxt['state']='disabled'
		Bwebpoptxt['state']='disabled'
		Bfileextxt['state']='disabled'
		wip['state']='disabled'
		wapp['state']='disabled'
		#BAgrflowtx = Button(win,text="Aggregate Flow",state=NORMAL)
		#Btopntxt = Button(win,text="TOP N",state=NORMAL)
                

#lb1= tk.Listbox(height=3)		
lb1=Listbox(win, height=6);
lb1.insert(1,"IP Analysis")
lb1.insert(2,"")
lb1.insert(3,"Application Analysis")
lb1.insert(4,"")
lb1.insert(5,"Flow Analysis")
lb1.insert(6,"")
lb1.grid(row=3, column=0)
lb1.bind('<<ListboxSelect>>', onselect)
#lb1.pack();	



#OK BUTTON
#b3 = Button(win,text="OK")
#b3.grid(row=3, column=1)
	
	
#EXECUTE BUTTON
#b4 = Button(win, text="Execute!",)
#b4.grid(row=0,column=4,rowspan=3,sticky=NSEW)
	
win.mainloop()
