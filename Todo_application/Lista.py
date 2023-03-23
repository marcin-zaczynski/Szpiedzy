import json
from functools import partial
from tkinter import*

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

class Lista_kupione:

    def __init__(self):
        self.okno = Tk()
        self.okno.geometry('200x300')
        self.okno.config(bg='red')
        self.okno.title('Kupione')
        nazwa = Label(self.okno, text='Kupione')
        nazwa.grid(column=0,row=0)
        b = 1
        for produkt in kupione:
            Label(self.okno, bg='red', foreground='yellow', text= produkt).grid(row=b, column=0)
            b += 1
        Button(self.okno, text="Wyczyść listę", command=lambda :Lista_kupione.wyczysc(self)).grid(row=100, column=2)
        self.okno.mainloop()

    def wyczysc(self):
        kupione.clear()
        zapisz_kupione()
        self.okno.destroy()

class wyswietlListe:
    def __init__(self):
        self.okno2 = Tk()
        self.okno2.geometry('200x300')
        self.okno2.config(bg='pink')
        self.okno2.title('Lista zakupów')
        self.nazwa = Label(self.okno2, text='Do kupienia')
        self.nazwa.grid(padx= 0,pady=1)
        lista.wyswietl(self)
    def wyswietl(self):
        b = 1
        c= 1
        a = 0
        for towar in doKupienia:
            self.tabelka_towar = Label(self.okno2,bg='pink', foreground='blue', text=towar)
            self.tabelka_towar.grid(column=0,row=b)
            b+=1

        for produkt in doKupienia:
            self.przycisk_kupione = Button(self.okno2, text='Kupione',command=partial(lista.dodajDoKupione, produkt))
            self.przycisk_kupione.grid(column=1,row=c)
            c+=1
            a+=1

    def dodajDoKupione(produkt):
        kupione.append(produkt)
        doKupienia.remove(produkt)
        zapisz_kupione()
        zapisz_do_kupienia()

lista = wyswietlListe
def dodanieDoListy(dodawane,okno1):
    dodane = dodawane.get()
    doKupienia.append(dodane)
    zapisz_do_kupienia()
    wpisywanie.delete(0, 'end')

okno1 = Tk()
okno1.title('Lista zakupów', )
okno1.geometry('280x280')
okno1.config(bg='green')

dodawane = StringVar(okno1)
wpisywanie = Entry(okno1, textvariable=dodawane, font=('Arial',12))# tabelka do wpisania
wpisywanie.pack(pady=30, )
przycisk1=Button(okno1, text="        Dodaj do listy        ", command=lambda: dodanieDoListy(dodawane,okno1)) #przycisk
przycisk1.pack( pady=10)
przycisk2 =Button(okno1, bg='pink', text='Wyświetl liste zakupów', command= lambda: wyswietlListe())
przycisk2.pack(pady=10)
przycisk3 =Button(okno1, text='    Wyświetl kupione      ', bg='red', command=lambda :Lista_kupione())
przycisk3.pack(pady=10)
okno1.mainloop()