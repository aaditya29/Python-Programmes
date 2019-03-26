Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 20:42:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> #!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter
top=tkinter.Tk()#calling of the module
res = 0#Result
tfprb = ""#Texts from previous radio button
def and1(a,b):
    global res#using global keyword to using global variable inside a function.
    res = int(a and b)
def or1(a,b):
    global res
    res  = int(a | b)
def not1(a):
    global res
    res = int(not a)
def xor1(a,b):
    global res
    res = int((a and not b) or (not a and b))
def result(event=None):
    global top,res,E3
    text = StringVar()
    E3=Entry(top,textvariable=text,bd=5)#The entry widget is used to accept a single line text strings grom the user.
    E3.grid(row=4,column=1)
    text.set(str(res))
def exit1(top):
    top.destroy()#destroy() destroys a widget i.e closing a tkinter window
def exit2(top):
    top.destroy()
def selected():
    global tfprb
    tfprb = var.get()
def expl(a,b):
    global top,tfprb,res
    binary1 = StringVar()
    binary2 = StringVar()#Used for getting the string value in the radio button
    top1=tkinter.Toplevel(top)#Toplevel widgets do not have a parent wiget on top of them. Toplevel widgets worork as windows that are directly managed byy the window manager.
    value1 = IntVar()#Used for getting int value and used in radio button
    l1=Label(top1,text="Number 1").grid(row=0,column=0)
    e1=Entry(top1,textvariable = value1,bd=5)
    value1.set(a)
    e1.grid(row=0,column=1)
    e3=Entry(top1,textvariable = binary1,bd=5)
    l3=Label(top1,text="Binary Number 1").grid(row=0,column=2)
    binary1.set(format(a,'b'))
    e3.grid(row=0,column=3)#It is a gemoretry organizer which organizes widgets in a table like structure in the parent widget.
    value2 = IntVar()
    l2=Label(top1,text="Number 2").grid(row=1,column=0)
    e2=Entry(top1,textvariable = value2,bd=5)
    value2.set(b)
    e2.grid(row=1,column=1)
    l4=Label(top1,text="Binary Number 2").grid(row=1,column=2)
    e4=Entry(top1,textvariable = binary2,bd=5)
    binary2.set(format(b,'b'))
    e4.grid(row=1,column=3)
    l5=Label(top1,text="t.f.p.r.b").grid(row=2,column=2) #says text from previous radiobutton selection
    operator = StringVar()#Operators are used to carry out arithmetic or logical computation.
    e5=Entry(top1,textvariable = operator,bd=5)
    operator.set(tfprb)
    operator.set(tfprb)
    e5.grid(row=2,column=3)
    dres = IntVar()
    l6=Label(top1,text="Decimal Result").grid(row=3,column=1)
    e6=Entry(top1,textvariable = dres ,bd=5)
    dres.set(res)
    e6.grid(row=3,column=2)
    b1=Tkinter.Button(top1,bd=5,text="Exit",command=lambda top=top1:exit2(top1)).grid(row=4,column=0)#Anonymous functions are defined using the lambda keyword.
    #We use lambda functions when we require a nameless function for a short period of time.
    top.mainloop()#Mainloop is used when we are ready for the application to run.
    #mainloop is an infinte loop used to run the application, wait for an event to occur and process the event till the window is not closed.
def dotwo(a,b):
    selected()
    expl(a,b)

num1 = IntVar()
L1=Label(top,text="Number 1").grid(row=0,column=0)
E1=Entry(top,textvariable = num1,bd=5)
num1.set(1)
E1.grid(row=0,column=1)
num2 = IntVar()
L2=Label(top,text="Number 2").grid(row=0,column=2)
E2=Entry(top,textvariable =num2,bd=5)
num2.set(1)
E2.grid(row=0,column=3)
var=StringVar()

R1=Radiobutton(top,text="AND",variable=var,value="AND",command=lambda: and1(int(E1.get()),int(E2.get())))
R1.grid(row=1,column=0)
R2=Radiobutton(top,text="OR",variable=var,value="OR",command=lambda: or1(int(E1.get()),int(E2.get())))
R2.grid(row=1,column=1)
R3=Radiobutton(top,text="NOT",variable=var,value="NOT",command=lambda: not1(int(E1.get())))
R3.grid(row=2,column=0)
R4=Radiobutton(top,text="XOR",variable=var,value="XOR",command=lambda: xor1(int(E1.get()),int(E2.get())))
R4.grid(row=2,column=1)
label=Label(top)
label.grid()

B1=tkinter.Button(top,text="Result is:",command=result,bd=5)
B1.grid(row=3,column=0)
B2=tkinter.Button(top,text="Explanation",command=lambda:dotwo(int(E1.get()),int(E2.get())),bd=5)
B2.grid(row=3,column=1)
B3=tkinter.Button(top,bd=5,text="Exit",command=lambda top=top:exit1(top)).grid(row=3,column=2)
L3=Label(top,text="Result is:").grid(row=4,column=0)
E3=Entry(top,bd=5)
E3.grid(row=4,column=1)
top.mainloop()

