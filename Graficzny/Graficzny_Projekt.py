import sys
import tkinter as tk
import json

try:
    with open('osoby.json','r') as file:
        osoby = json.load(file)

except FileNotFoundError:
    osoby = {}
    with open('osoby.json', 'w') as file:
        json.dump(osoby, file)

try:
    with open('kontakty.json','r') as file:
        kontakty = json.load(file)

except FileNotFoundError:
    kontakty = {}
    with open('kontakty.json','w') as file:
        json.dump(kontakty, file)

def listaOsob():

    oknoW = tk.Tk()
    oknoW.title('Wyświetlanie')
    a = 1
    for i in osoby.values():
        cb = tk.Label(oknoW, text=str(a) + ':' + str(i) + '\n')
        cb.pack()
        a += 1

    oknoW.mainloop()

def zamknijOkno(okno):
    okno.destroy()

def koniec():
    sys.exit()

def dodajOsobe(x,y):
    name = x.get()
    surname = y.get()
    print('wpisano:', name, surname)
    a = len(osoby) + 1
    osoby[a] = name, surname
    with open('osoby.json', 'w') as file:
        json.dump(osoby, file)

def oknoDodajOsobe():
    oknoD = tk.Tk()
    tk.Label(oknoD,)
    oknoD.title('Dodaj osobę')
    oknoD.geometry('300x100')
    imie = tk.StringVar(oknoD)
    nazwisko = tk.StringVar(oknoD)
    tk.Label(oknoD, text='Imię').grid(row=0, column=0)
    tk.Entry(oknoD, textvariable=imie).grid(row=0, column=1)
    tk.Label(oknoD, text='Nazwisko').grid(row=1, column=0)
    tk.Entry(oknoD, textvariable=nazwisko).grid(row=1, column=1)
    tk.Button(oknoD, text="Zatwierdz", command=lambda: dodajOsobe(imie, nazwisko)).grid(row=2, column=0, padx=2, pady=2)
    tk.Button(oknoD, text="Zrezygnuj", command=lambda: zamknijOkno(oknoD)).grid(row=2, column=1, padx=2, pady=2)
    oknoD.mainloop()


def wyswietlanie():

    okno1 = tk.Tk()
    okno1.title = 'Wyświetlanie'
    okno1.geometry('480x480')

    tk.Label(okno1, text="1 - wyświetl sieć kontaktów").grid(row=1, column=0, padx=2, pady=2)
    tk.Label(okno1, text="2 - dodaj osobę").grid(row=2, column=0, padx=2, pady=2)
    tk.Label(okno1, text="3 - dodaj powiązanie pomiędzy kontaktami").grid(row=3, column=0, padx=2, pady=2)
    tk.Label(okno1, text="4 - wyświetl powiązane osoby z kontaktem").grid(row=4, column=0, padx=2, pady=2)
    tk.Label(okno1, text="5 - usuń osobę").grid(row=5, column=0, padx=2, pady=2)
    tk.Label(okno1, text="9 - zamknij").grid(row=6, column=0, padx=2, pady=2)

    tk.Button(okno1, text="Zatwierdz", command=listaOsob).grid(row=1, column=1, padx=2, pady=2)
    tk.Button(okno1, text="Zatwierdz", command=oknoDodajOsobe ).grid(row=2, column=1, padx=2, pady=2)
    tk.Button(okno1, text="Zatwierdz", ).grid(row=3, column=1, padx=2, pady=2)
    tk.Button(okno1, text="Zatwierdz", ).grid(row=4, column=1, padx=2, pady=2)
    tk.Button(okno1, text="Zatwierdz", ).grid(row=5, column=1, padx=2, pady=2)
    tk.Button(okno1, text="Zatwierdz", ).grid(row=6, column=1, padx=2, pady=2)

    okno1.mainloop()
def logowanie():
    __login = 'login'
    __haslo = 'haslo'
    login = log.get()
    haslo = has.get()
    podlogin = login
    podhaslo = haslo

    if podlogin == __login and podhaslo == __haslo:
        okno.destroy()
        wyswietlanie()
    else:
        okno_blad = tk.Tk()
        okno_blad.title('Błąd')
        okno_blad.geometry('100x100')

        tk.Label(okno_blad, text="Zły login lub hasło").grid(row=0, column=0, padx=2, pady=2)
        tk.Button(okno_blad, text="spróbuj ponownie",command=okno_blad.destroy ).grid(row=2, column=0, padx=2, pady=2)
        tk.Button(okno_blad, text="Zakończ program",command=koniec ).grid(row=3, column=0, padx=2, pady=2)
        okno_blad.mainloop()
        okno.destroy()


while True:
    okno = tk.Tk()
    okno.title('Logowanie')
    okno.geometry('300x100')
    log = tk.StringVar()
    has = tk.StringVar()
    tk.Label(okno, text="Login").grid(row=0, column=0, padx=2, pady=2)
    tk.Entry(okno,textvariable=log).grid(row=0, column=1)

    tk.Label(okno, text="Haslo").grid(row=1, column=0, padx=2, pady=2)
    tk.Entry(okno, textvariable=has).grid(row=1, column=1)

    tk.Button(okno, text="Zatwierdz", command=logowanie).grid(row=2, column=0, padx=2, pady=2)
    tk.Button(okno, text="Zrezygnuj", command=koniec).grid(row=2, column=1, padx=2, pady=2)
    okno.mainloop()
