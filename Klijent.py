from tkinter import *
import tkinter
import random
import threading
import time
from tkinter import ttk


def naruci():
    print("poz")


padding=5
okvir = tkinter.Tk()

okvir.option_add("*Font", "arial 14")

#Naslovi
naslov = tkinter.Label(okvir,text= "Poupunite porudžbinu:",bg="#8FC93A",width=50,height=3)
naslov.grid(column=0,row =0,rowspan=3,columnspan=5,pady=(0,20),sticky=NW)

naslov = tkinter.Label(okvir,text= "Odgovor servera:",bg="#E4CC37",width=30,height=3)
naslov.grid(column=5,row =0,rowspan=3,columnspan=5,pady=(0,20),sticky=NW)

#Combobox-ovi
textVelicina = tkinter.Label(okvir,text= "Veličina:")
textVelicina.grid(column=0,row=3,pady=padding,sticky=E)

dropVelicina = ttk.Combobox(okvir, values=[ 25,32, 50],width=23)
dropVelicina.grid(column = 1,columnspan=4,row = 3,pady=padding,sticky=W)

textVrsta = tkinter.Label(okvir,text= "Vrsta:")
textVrsta.grid(column=0,row=4,pady=padding,sticky=E)

dropVrsta = ttk.Combobox(okvir, values=[ "Margarita","Funghi", "Quatro Stagione", "Vegeterian"],width=23)
dropVrsta.grid(column = 1,columnspan=4,row = 4,pady=padding,sticky=W)

textDodatak = tkinter.Label(okvir,text= "Dodatak:")
textDodatak.grid(column=0,row=5,pady=padding,sticky=E)

#Checkbox-evi
kecapVar = IntVar()
majonezVar = IntVar()
ciliVar = IntVar()
origanoVar = IntVar()
govedjaVar = IntVar()
pilecaVar = IntVar()
comboKecap = tkinter.Checkbutton(text="Kečap",variable = kecapVar)
comboMajonez = tkinter.Checkbutton(text="Majonez",variable = majonezVar)
comboCili = tkinter.Checkbutton(text="Čili",variable = ciliVar)
comboOrigano = tkinter.Checkbutton(text="Origano",variable = origanoVar)
comboGovedja = tkinter.Checkbutton(text="Govedja salata",variable = govedjaVar)
comboPileca = tkinter.Checkbutton(text="Pileća salata",variable = pilecaVar)
comboKecap.grid(column=1,row=5,sticky=W)
comboMajonez.grid(column=1,row=6,sticky=W)
comboCili.grid(column=2,row=5,sticky=W)
comboOrigano.grid(column=2,row=6,sticky=W)
comboGovedja.grid(column=3,row=5,sticky=W)
comboPileca.grid(column=3,row=6,sticky=W)

#Radiobuttons
textNacinPlacanja = tkinter.Label(okvir,text= "Način plaćanja:")
textNacinPlacanja.grid(column=0,row=7,pady=padding,sticky=E)

nacinPlacanjaVar = IntVar()
radioKes = tkinter.Radiobutton(okvir, text="Keš",variable=nacinPlacanjaVar,value=1)
radioKartica = tkinter.Radiobutton(okvir, text="Kartica",variable=nacinPlacanjaVar,value=2)
radioKes.grid(column=1,row = 7)
radioKartica.grid(column=2,row = 7)

#Text input-i
textAdresa = tkinter.Label(okvir,text= "Adresa naručioca:")
textAdresa.grid(column=0,row=8,pady=padding,sticky=E)

adresaVar= StringVar()
entryAdresa= tkinter.Entry(okvir,textvariable=adresaVar,width=25)
entryAdresa.grid(column=1,row=8,columnspan=3,sticky=W)

textBrojTelefona = tkinter.Label(okvir,text= "Broj telefona:")
textBrojTelefona.grid(column=0,row=9,pady=padding,sticky=E)

brojTelefonaVar= StringVar()
entryBrojTelefona= tkinter.Entry(okvir,textvariable=brojTelefonaVar,width=25)
entryBrojTelefona.grid(column=1,row=9,columnspan=3,sticky=W)

#Textarea
textNapomena = tkinter.Label(okvir,text= "Napomena:")
textNapomena.grid(column=0,row=10,pady=padding,sticky=E)

unosNapomena = tkinter.Text(okvir, height=4,width=25)
unosNapomena.grid(column=1,row=10,columnspan=3,sticky=W)

unosOdgovorServera = tkinter.Text(okvir,width=30)
unosOdgovorServera.grid(column=5,row=3,rowspan=9,pady=padding)

#dugme
dugmeNaruci= tkinter.Button(okvir,text="Naruci",width=15,bg="#8FC93A",command=naruci)
dugmeNaruci.grid(column=0,row=11,columnspan=5,pady=30)



okvir.mainloop()