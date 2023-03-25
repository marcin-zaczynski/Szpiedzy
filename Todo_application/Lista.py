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
        self.okno_kupione = Tk()
        self.okno_kupione.geometry('200x300')
        self.okno_kupione.config(bg='red')
        self.okno_kupione.title('Kupione')
        nazwa = Label(self.okno_kupione, text='Kupione')
        nazwa.grid(column=0,row=0)
        b = 1
        for produkt in kupione:
            Label(self.okno_kupione, bg='red', foreground='yellow', text= produkt).grid(row=b, column=0)
            b += 1
        Button(self.okno_kupione, text="Wyczyść listę", command=lambda :Lista_kupione.wyczysc(self)).grid(row=100, column=2)
        self.okno_kupione.mainloop()

    def wyczysc(self):
        kupione.clear()
        zapisz_kupione()
        self.okno_kupione.destroy()

class wyswietlListe:
    def __init__(self):
        self.okno_do_kupienia = Tk()
        self.okno_do_kupienia.geometry('200x300')
        self.okno_do_kupienia.config(bg='pink')
        self.okno_do_kupienia.title('Lista zakupów')
        self.nazwa = Label(self.okno_do_kupienia, text='Do kupienia')
        self.nazwa.grid(padx= 0,pady=1)
        lista.wyswietl(self)
    def wyswietl(self):
        wiersz = 1
        for towar in doKupienia:
            self.tabelka_towar = Label(self.okno_do_kupienia,bg='pink', foreground='blue', text=towar)
            self.tabelka_towar.grid(column=0,row=wiersz)
            self.przycisk_kupione = Button(self.okno_do_kupienia, text='Kupione',command=partial(lista.dodajDoKupione, towar))
            self.przycisk_kupione.grid(column=1, row=wiersz)
            wiersz+=1

    def dodajDoKupione(produkt):
        kupione.append(produkt)
        doKupienia.remove(produkt)
        zapisz_kupione()
        zapisz_do_kupienia()

lista = wyswietlListe
def dodanieDoListy(dodawane):
    dodane = dodawane.get()
    doKupienia.append(dodane)
    zapisz_do_kupienia()
    wpisywanie.delete(0, 'end')

okno_glowne = Tk()
okno_glowne.title('Lista zakupów', )
okno_glowne.geometry('280x280')
okno_glowne.config(bg='green')

dodawane = StringVar(okno_glowne)
wpisywanie = Entry(okno_glowne, textvariable=dodawane, font=('Arial',12))
wpisywanie.pack(pady=30, )
przycisk1=Button(okno_glowne, text="        Dodaj do listy        ", command=lambda: dodanieDoListy(dodawane))
przycisk1.pack( pady=10)
przycisk2 =Button(okno_glowne, bg='pink', text='Wyświetl liste zakupów', command= lambda: wyswietlListe())
przycisk2.pack(pady=10)
przycisk3 =Button(okno_glowne, text='    Wyświetl kupione      ', bg='red', command=lambda :Lista_kupione())
przycisk3.pack(pady=10)
okno_glowne.mainloop()