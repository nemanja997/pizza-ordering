from tkinter import *
import tkinter
import random
import threading
import time
from tkinter import ttk
import socket

redIsporucenih = 3

def odbrojavaj(vremeIsporuke,narudbinaLabela,vremeLabela,vreme):
    global redIsporucenih
    brojac = vremeIsporuke
    while brojac > 0:
        vreme.set(brojac)
        time.sleep(1)
        brojac -=1
    narudbinaLabela.grid_forget()
    vremeLabela.grid_forget()

    narudbinaLabela.grid(column=5, row=redIsporucenih, rowspan=1, pady=padding)
    redIsporucenih +=1



def formatirajNarudzbinuZaIspis(narudzbina):
    prilozi = narudzbina['prilozi'].split(",")
    ispis = f"{narudzbina['vrstaPizze']}, {narudzbina['velicinaPizze']} \n Prilozi:"
    for prilog in prilozi:
        if prilog != "":
            ispis += prilog + " "
    ispis += f"\n Adresa: {narudzbina['adresa']} \n Broj: {narudzbina['brojTelefona']} \n Napomena: \n {narudzbina['napomena']}"
    return ispis


def generisiOdgovorServera(narudzbina):

    return "Hvala na porudzbini \n Vreme za isporuku vase pizze " +narudzbina["vrstaPizze"]+ " je: " + str(narudzbina["vreme"]) + "min"

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)

def rasclaniPoruku(poruka):
    recnikNarudzbina = {}
    privremena = poruka.split(";")
    recnikNarudzbina["velicinaPizze"] = privremena[0]
    recnikNarudzbina["vrstaPizze"] = privremena[1]
    recnikNarudzbina["prilozi"] = privremena[2]
    recnikNarudzbina["nacinPlacanja"] = privremena[3]
    recnikNarudzbina["adresa"] = privremena[4]
    recnikNarudzbina["brojTelefona"] = privremena[5]
    recnikNarudzbina["napomena"] = privremena[6]
    recnikNarudzbina["vreme"] = random.randrange(10,50)

    return recnikNarudzbina

def konektujSeSaKlijentom(conn):
    brojac = 3
    print('Imam konekciju od klijenta')
    while True:
        porukaKlijenta= conn.recv(1024).decode()
        narudzbina = rasclaniPoruku(porukaKlijenta)
        conn.send(generisiOdgovorServera(narudzbina).encode())

        narudzbinaLabele = []
        vremeLabele = []
        narudzbinaLabele.append(tkinter.Label(okvir,text=formatirajNarudzbinuZaIspis(narudzbina),wraplength=200))
        narudzbinaLabele[-1].grid(column=0,row=brojac,rowspan=1,pady=padding)

        vremeLabele.append(tkinter.Label(okvir, textvariable=vremeVarijable[brojac-3]))
        vremeLabele[-1].grid(column=1, row=brojac, rowspan=1, pady=padding)

        threading.Thread(target=odbrojavaj,args=(narudzbina['vreme'],narudzbinaLabele[-1],vremeLabele[-1],vremeVarijable[brojac-3])).start()

        brojac+=1
    conn.close()
def cekajNaKlijenta():
    while True:
        conn,addr = s.accept()
        threading.Thread(target=konektujSeSaKlijentom,args=(conn,)).start()

threading.Thread(target=cekajNaKlijenta).start()



# --- Graficki interfejs ---
padding=5
okvir = tkinter.Tk()
okvir.title("Server")
okvir.geometry("700x600")

okvir.option_add("*Font", "arial 14")
vremeVarijable = []
for broj in range(100):
    vremeVarijable.append(StringVar())
#Naslovi
naslov = tkinter.Label(okvir,text= "Neisporučene porudžbine:",bg="#7F92B7",width=30,height=3)
naslov.grid(column=0,row =0,rowspan=3,columnspan=5,pady=(0,20),sticky=NW)

naslov = tkinter.Label(okvir,text= "Isporučene porudžbine:",bg="#7BE0AD",width=30,height=3)
naslov.grid(column=5,row =0,rowspan=3,columnspan=5,pady=(0,20),sticky=NW)

#Labele



#TextArea
# unosNeisporuceno = tkinter.Text(okvir,width=30)
# unosNeisporuceno.grid(column=0,row=3,rowspan=9,pady=padding)
#
# unosIsporuceno = tkinter.Text(okvir,width=30)
# unosIsporuceno.grid(column=5,row=3,rowspan=9,pady=padding)


okvir.mainloop()
# --- Graficki interfejs ---