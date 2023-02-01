from tkinter import *

master = Tk()
master.geometry('800x120')
master.title('Input Test')
master.resizable(0, 0) #

def UserName():
    global usrE
    global usrN
    global lbl

    usrE1 = usrE.get()
    usrN2 = usrN.get()
    InputExcept = str(usrN2) +"\\" +str(usrE1)
    print( InputExcept )
    #lbl.config(text=' Complete path: \n'+str(InputExcept))

label_1 = Label(master,text ="Name of the video file: ")
label_1.grid(row=1, column=1,sticky=N)
usrE = Entry(master, relief=SUNKEN)
usrE.grid(row=1, column=2,sticky=N,padx=0, pady=0,ipadx=200,ipady=0)
usrE.configure(background='red')

label_2 = Label(master,text ="Path of the video file: ")
label_2.grid(row=2, column=1,sticky=N)
usrN = Entry(master, relief=SUNKEN)
usrN.grid(row=2, column=2,padx=0, pady=0,ipadx=200,ipady=0)
Btn1 = Button(master, text="Input", command=UserName)
Btn1.grid(row=4, column=2,sticky=N,padx=0, pady=0,ipadx=60,ipady=0) 

lbl = Label(master)
lbl.grid(row=8, column=2)

#master.columnconfigure(1, weight=1)
#master.rowconfigure(1, weight=1)
'''
lbl = Label(master)
lbl.grid(row=6, column=2) 
'''
#master.grid_columnconfigure(22, weight=9)
#master.grid_rowconfigure(2, weight=1)
master.mainloop()