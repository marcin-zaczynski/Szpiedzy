import json
import tkinter
from functools import partial
from tkinter import*

def zapisz(gdzie_zapisac, co_zapisac ):
    with open(gdzie_zapisac+'.json','w') as file:
        json.dump(co_zapisac, file)
try:
    with open('kategorie.json','r') as file:
        kategorie = json.load(file)
except FileNotFoundError:
    kategorie = []
    zapisz('kategorie', kategorie)

def odswiez_liste_kategorii():
    for widget in okno_glowne.winfo_children():
        widget.destroy()
    for nazwa in kategorie:
        przycisk_kategori = Button(okno_glowne, text=nazwa,
                                        command=partial(Wyswietl_kategorii, nazwa), width=15)
        przycisk_kategori.pack()
    przycisk_wyswietlania = Button(okno_glowne, text="Kategorie", command=Kategorie, width=15)
    przycisk_wyswietlania.pack(pady=10)

class Program():
    def __init__(self,okno_glowne):
        self.okno_glowne = okno_glowne
        for nazwa in kategorie:
            self.przycisk_kategori = Button(okno_glowne, text=nazwa,command=partial(Wyswietl_kategorii, nazwa), width=20)
            self.przycisk_kategori.pack()
        self.przycisk_wyswietlania = Button(okno_glowne, text="Kategorie", command=Kategorie, width=15)
        self.przycisk_wyswietlania.pack(pady=10)

class Kategorie():
    def __init__(self):
        self.okno_kategorii = Tk()
        self.okno_kategorii.title('Dodaj kategorie')
        self.dodawane = tkinter.StringVar(self.okno_kategorii)
        self.nazwa_kategorii = Entry(self.okno_kategorii, textvariable=self.dodawane, font=('Arial', 12))
        self.nazwa_kategorii.pack(pady=10)
        self.przycisk_dodaj = Button(self.okno_kategorii, text="Dodaj kategorie        ",
                                command=lambda: Kategorie.dodac_kategorie(self),width=20)
        self.przycisk_dodaj.pack(pady=10)
        self.przycisk_usun = Button(self.okno_kategorii, text="Usuń kategorie",
                                command=lambda: Kategorie.usun_kategorie(self),width=20)
        self.przycisk_usun.pack(pady=10)
        self.okno_kategorii.mainloop()

    def dodac_kategorie(self):
        dodac = self.dodawane.get()
        kategorie.append(dodac)
        zapisz('kategorie',kategorie)
        with open(str(dodac)+ '.json', 'w') as file:
            dodac = []
            json.dump(dodac, file)
        odswiez_liste_kategorii()
        self.okno_kategorii.destroy()

    def usun_kategorie(self):
        usun = self.dodawane.get()
        kategorie.remove(usun)
        zapisz('kategorie',kategorie)
        self.okno_kategorii.destroy()
        odswiez_liste_kategorii()

class Wyswietl_kategorii():
    def __init__(self, okno):
        self.okno = okno
        okno = Tk()
        okno.geometry('200x300')
        Wyswietl_kategorii.kategorie(self, okno)

    def kategorie(self,okno):
        with open(self.okno +'.json', 'r') as file:
            lista = json.load(file)
        listbox = Listbox(okno)
        listbox.pack()
        for item in lista:
            listbox.insert(END, item)
        self.dodawane = tkinter.StringVar(okno)
        self.nazwa_kategorii = Entry(okno, textvariable=self.dodawane, font=('Arial', 12))
        self.nazwa_kategorii.pack(pady=10)
        self.przycisk_dodaj = Button(okno, text=" Dodaj",
                                     command=lambda: Wyswietl_kategorii.akcja(self,1,okno), width=20)
        self.przycisk_dodaj.pack(pady=10)
        delete_button = Button(okno, text='Usuń zaznaczone',
                               command=lambda: Wyswietl_kategorii.akcja(self,listbox,okno))
        delete_button.pack()
        okno.mainloop()

    def akcja(self,x,okno):
        if x == 1:
            dodac = self.dodawane.get()
            with open(self.okno +'.json', 'r') as file:
                lista = json.load(file)
            lista.append(dodac)
            zapisz(self.okno,lista)
            self.nazwa_kategorii.delete(0, 'end')
        else:
            selected_indices = x.curselection()
            for index in selected_indices[::-1]:
                with open(self.okno +'.json', 'r') as file:
                    lista = json.load(file)
                lista.pop(index)
                zapisz(self.okno,lista)
        Wyswietl_kategorii.odswiez(self,okno)

    def odswiez(self,okno):
        for widget in okno.winfo_children():
            widget.destroy()
        Wyswietl_kategorii.kategorie(self,okno)

okno_glowne = Tk()
okno_glowne.title('Lista', )
okno_glowne.geometry('280x280')
app = Program(okno_glowne)
okno_glowne.mainloop()