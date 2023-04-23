import time
import tkinter as tk
from tkinter import *
from tkinter.ttk import Progressbar
frame = tk.Tk()
frame.title("TextBox Input")
frame.geometry('400x400')
global chek
def printInput():
    inp = float(inputtxt.get(1.0, "end-1c"))
    # lbl.config(text = inp)
    inp1=float(inputtxt1.get(1.0, "end-1c"))
    inp2 =float(inputtxt2.get(1.0, "end-1c"))
    inp3 =float(inputtxt3.get(1.0, "end-1c"))
    inp4 =float(inputtxt4.get(1.0, "end-1c"))
    print(inp)
    print(inp1)
    print(inp2)
    print(inp3) 
    print(inp4)
    che=(inp+inp1+inp2+inp3+inp4)/(5.0)
    print(che*9.5)
    chek=int(che*9.5)
    list.append(chek)
    print(list)
    # incr(percen)
    # task=1#Here we were checking the limit up to where the task bar is needed to fill
    # x=0
    # GB=100
    # speed=1
    # while(x<GB):
    #     # bar['value']+=10
    #     if x==percen:
    #         return
    #     time.sleep(0.05)
    #     bar['value']+=(speed/GB)*100
    #     x=x+speed
    #     # percent.set()
    #     tx=str((x/task)*100)+"%"
        # percent.set(text=tx)
        # percent.set("hello")
        # txt.set(str(x)+"/"+str(GB)+"Tasks completed")
        # print(x)
        # perc.set(str((int((x/GB)*100)))+"%")
        # frame.update_idletasks()
   # bar['value']+=10#increases the progress bar
    # TextBox Creation
# def incr():
#     task=10#Here we were checking the limit up to where the task bar is needed to fill
#     x=0
#     GB=100
#     print("incr")
#     speed=1
#     while(x<GB):
#         # bar['value']+=10
#         if x== list[0]:
#             break
#         time.sleep(0.05)
#         bar['value']=bar['value']+(speed/GB)*100
#         x=x+speed
#         # percent.set()
#         tx=str((x/task)*100)+"%"
#         # percent.set(text=tx)
#         # percent.set("hello")
#         # txt.set(str(x)+"/"+str(GB)+"Tasks completed")
#         # print(x)
#         # perc.set(str((int((x/GB)*100)))+"%")
#         frame.update_idletasks()
#    # bar['value']+=10#increases the progress bar
def incr():
    window=Tk()
    chek=25
    def incr():
        task=10#Here we were checking the limit up to where the task bar is needed to fill
        x=0
        GB=100
        speed=1
        while(x<GB):
        # bar['value']+=10
           if x== chek:
             break
           time.sleep(0.05)
           bar['value']+=(speed/GB)*100
           x=x+speed
        # percent.set()
           tx=str((x/task)*100)+"%"
        # percent.set(text=tx)
        # percent.set("hello")
           txt.set(str(x)+"/"+str(GB)+"Tasks completed")
        # print(x)
           perc.set(str((int((x/GB)*100)))+"%")
        window.update_idletasks()
   # bar['value']+=10#increases the progress bar
    percent=StringVar()
    txt=StringVar()
    perc=StringVar()
    window.title("Progress bar")
# percent=Label(window,textvariable=percent).pack()
    bar=Progressbar(window,orient=HORIZONTAL,length=300)
    bar.pack(pady=10)
    per=Label(window,textvariable=perc)
    per.pack(padx=10)
    text=Label(window,textvariable=txt)
    text.pack(padx=10)
    but=Button(text="SUBMIT",command=incr)
    but.pack(padx=10)
    window.mainloop()


lsub1=tk.Label(frame,text="Enter the cgpa of first subject:").place(x=55,y=100)
lsub2=tk.Label(frame,text="Enter the cgpa of second subject:").place(x=40,y=130)
lsub3=tk.Label(frame,text="Enter the cgpa of third subject:").place(x=45,y=160)
lsub4=tk.Label(frame,text="Enter the cgpa of fourth subject:").place(x=40,y=190)
lsub5=tk.Label(frame,text="Enter the cgpa of fifth subject:").place(x=50,y=220)
bar=Progressbar(frame,orient=tk.HORIZONTAL,length=300).pack()
list=[20]
prog=tk.Button(frame,text="PROGRESS",command=incr).pack()
inputtxt = tk.Text(frame,
                   height = 1,
                   width = 15)
inputtxt1 = tk.Text(frame,
                   height = 1,
                   width = 15)
inputtxt2 = tk.Text(frame,
                   height = 1,
                   width = 15)
inputtxt3 = tk.Text(frame,
                   height = 1,
                   width = 15)
inputtxt4 = tk.Text(frame,
                   height = 1,
                   width = 15)
inputtxt.place(x=230,y=100)
inputtxt1.place(x=230,y=130)
inputtxt2.place(x=230,y=160)
inputtxt3.place(x=230,y=190)
inputtxt4.place(x=230,y=220) 
# Button Creation
printButton = tk.Button(frame,
                        text = "SUBMIT", 
                        command = printInput)
printButton.place(x=200,y=250)
  
# Label Creation
lbl = tk.Label(frame, text = "")
lbl.pack()
frame.mainloop()