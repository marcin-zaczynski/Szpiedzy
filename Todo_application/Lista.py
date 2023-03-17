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

    dodac = tk.StringVar(okno1)
    tk.Entry(okno1, textvariable=dodac).grid(row=1, column=1) # tabelka do wpisania
    tk.Button(okno1, text="        Dodaj do listy        ", command=lambda: dodanieDoListy(dodac)).grid(row=1, column=2) #przycisk
    tk.Button(okno1, bg='pink', text='Wyświetl liste zakupów', command=wyswietlListe).grid(row=2,column=2)
    tk.Button(okno1, text='    Wyświetl kupione      ', bg='red', command=lista_kupione).grid(row=3, column=2)

    okno1.mainloop()

def dodanieDoListy(dodanwane):
    dodane = dodanwane.get()
    doKupienia.append(dodane)
    zapisz_do_kupienia()

def lista_kupione():
    okno3 = tk.Tk()
    okno3.geometry('200x300')
    okno3.config(bg='red')
    okno3.title('Kupione')
    tk.Label(okno3, text='Kupione').grid(row=0, column=0)
    b = 1
    for i in kupione:
        tk.Label(okno3, bg='red', foreground='yellow', text=i).grid(row=b, column=0)
        b += 1

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

program()