import tkinter as tk
import json
from functools import partial

def zapisz_do_kupienia():
    with open('doKupienia.json', 'w') as file:
        json.dump(doKupienia, file)

def zapisz_kupione():
    with open('kupione.json','w') as file:
        json.dump(kupione, file)

try:
    with open('doKupienia.json','r') as file:
        doKupienia = json.load(file)

except FileNotFoundError:
    doKupienia = []
    zapisz_do_kupienia()

try:
    with open('kupione.json','r') as file:
        kupione = json.load(file)

except FileNotFoundError:
    kupione = []
    zapisz_kupione()

def program():
    okno1 = tk.Tk()
    okno1.title('Lista zakupów', )
    okno1.geometry('280x280')
    okno1.config(bg='green')

    dodawane = tk.StringVar(okno1)
    tk.Entry(okno1, textvariable=dodawane).grid(row=1, column=1) # tabelka do wpisania
    tk.Button(okno1, text="        Dodaj do listy        ", command=lambda: dodanieDoListy(dodawane,okno1)).grid(row=1, column=2) #przycisk
    tk.Button(okno1, bg='pink', text='Wyświetl liste zakupów', command=wyswietlListe).grid(row=2,column=2)
    tk.Button(okno1, text='    Wyświetl kupione      ', bg='red', command=lambda :zakup.lista()).grid(row=3, column=2)
    zakup = Lista_kupione('okno3','przyciski','czyszcik','tabele')
    okno1.mainloop()

def dodanieDoListy(dodawane,okno1):
    okno1.destroy()
    dodane = dodawane.get()
    doKupienia.append(dodane)
    zapisz_do_kupienia()
    program()

class Lista_kupione:

    def __init__(self,okno,przycisk,czyszczenie,tabelka):
        self.okno = okno
        self.przycisk = przycisk
        self.czyszczenie = czyszczenie
        self.tabelka = tabelka

    def lista(self):
        self.okno = tk.Tk()
        self.okno.geometry('200x300')
        self.okno.config(bg='red')
        self.okno.title('Kupione')

        nazwa = tk.Label(self.okno, text='Kupione').grid(row=0, column=0)
        b = 1
        for i in kupione:
            self.tabelka = tk.Label(self.okno, bg='red', foreground='yellow', text=i).grid(row=b, column=0)
            b += 1
        self.przycisk = tk.Button(self.okno, text="Wyczyść listę", command=lambda :zakup.wyczysc(self.okno)).grid(row=100, column=2)
        self.okno.mainloop()
        self.okno.destroy()

    def wyczysc(self,okno):
        okno.destroy()
        kupione.clear()
        zapisz_kupione()
        zakup.lista()

def wyswietlListe():
    okno2 = tk.Tk()
    okno2.geometry('200x300')
    okno2.config(bg='pink')
    okno2.title('Lista zakupów')
    tk.Label(okno2, text='Do kupienia').grid(row=0,column=0)
    b = 1
    c= 1
    a = 0
    for i in doKupienia:
        tk.Label(okno2,bg='pink', foreground='blue', text=i).grid(row=b, column=0)
        b+=1

    for i in doKupienia:
        tk.Button(okno2, text='Kupione',command=partial(dodajDoKupione, i)).grid(row=c,column=1)
        c+=1
        a+=1

def dodajDoKupione(i):
    kupione.append(i)
    doKupienia.remove(i)
    zapisz_kupione()
    zapisz_do_kupienia()
zakup = Lista_kupione('okienko','przyciski','czyszczenia','tabelki')
program()