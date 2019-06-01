from tkinter import *
import tkinter
import random
import threading
import time
from tkinter import ttk

padding=5
okvir = tkinter.Tk()
okvir.title("Server")

okvir.option_add("*Font", "arial 14")

#Naslovi
naslov = tkinter.Label(okvir,text= "Neisporučene porudžbine:",bg="#7F92B7",width=30,height=3)
naslov.grid(column=0,row =0,rowspan=3,columnspan=5,pady=(0,20),sticky=NW)

naslov = tkinter.Label(okvir,text= "Isporučene porudžbine:",bg="#7BE0AD",width=30,height=3)
naslov.grid(column=5,row =0,rowspan=3,columnspan=5,pady=(0,20),sticky=NW)

#TextArea
unosNeisporuceno = tkinter.Text(okvir,width=30)
unosNeisporuceno.grid(column=0,row=3,rowspan=9,pady=padding)

unosIsporuceno = tkinter.Text(okvir,width=30)
unosIsporuceno.grid(column=5,row=3,rowspan=9,pady=padding)


okvir.mainloop()