import tkinter as tk
import json
from functools import partial

try:
    with open('doKupienia.json','r') as file:
        doKupienia = json.load(file)

except FileNotFoundError:
    doKupienia = []
    with open('doKupienia.json', 'w') as file:
        json.dump(doKupienia, file)

try:
    with open('Kupione.json','r') as file:
        Kupione = json.load(file)

except FileNotFoundError:
    Kupione = []
    with open('Kupione.json','w') as file:
        json.dump(Kupione, file)


class Zadanie:
    def __init__(self, index):
        self.index = index

    def get_index(self):
        return self.index

def program():
    okno1 = tk.Tk()
    okno1.title('Lista zakupów', )
    okno1.geometry('280x280')
    okno1.config(bg='green')

    dodac = tk.StringVar(okno1)
    tk.Entry(okno1, textvariable=dodac).grid(row=1, column=1) # tabelka do wpisania
    tk.Button(okno1, text="Dodaj do listy", command=lambda: dodanieDoListy(dodac)).grid(row=1, column=2) #przycisk
    tk.Button(okno1, text='Wyświetl liste zakupów', command=wyswietlListe).grid(row=2,column=2)

    okno1.mainloop()

def dodanieDoListy(dodanwane):
    dodane = dodanwane.get()
    doKupienia.append(dodane)
    with open('doKupienia.json','w') as file:
        json.dump(doKupienia, file)


def wyswietlListe():
    okno2 = tk.Tk()
    okno2.geometry('200x300')
    okno2.config(bg='pink')
    tk.Label(okno2, text='Do kupienia').grid(row=0,column=0)
    b = 1
    c= 1
    a = 0
    for i in doKupienia:
        tk.Label(okno2,bg='pink', foreground='blue', text=i).grid(row=b, column=0)
        b+=1

    for i in doKupienia:
        zadanie = Zadanie(i)
        tk.Button(okno2, text='Kupione',command=partial(dodajDoKupione, zadanie)).grid(row=c,column=1)
        c+=1
        a+=1


def dodajDoKupione(x):
    print(x.get_index())

program()