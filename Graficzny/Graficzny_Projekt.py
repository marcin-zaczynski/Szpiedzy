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

def koniec():
    sys.exit()

def dodajOsobe(x,y):
    #imiee = x.get()
    #nazw = y.get()
    print(x, y)
    #a = len(osoby) + 1
    #osoby[a] = imiee, nazw
    #with open('osoby.json', 'w') as file:
    #    json.dump(osoby, file)

def oknoDodajOsobe():
    okno = tk.Tk()
    tk.Label(okno,)
    imie = tk.StringVar()
    nazwisko = tk.StringVar()
    tk.Label(okno, text='Imię').grid(row=0, column=0)
    tk.Entry(okno, textvariable=imie).grid(row=0, column=1)
    tk.Label(okno, text='Nazwisko').grid(row=1, column=0)
    tk.Entry(okno, textvariable=nazwisko).grid(row=1, column=1)
    tk.Button(okno, text="Zatwierdz", command=lambda a=imie.get(),b=nazwisko.get(),eff=None:dodajOsobe(a, b)).grid(row=2, column=0, padx=2, pady=2)
    #tk.Button(okno, text="Zrezygnuj", command=koniec).grid(row=2, column=1, padx=2, pady=2)
    okno.mainloop()


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

    ok = tk.Button(okno1, text="Zatwierdz", command=listaOsob).grid(row=1, column=1, padx=2, pady=2)
    ok1 = tk.Button(okno1, text="Zatwierdz", command=oknoDodajOsobe ).grid(row=2, column=1, padx=2, pady=2)
    ok2 = tk.Button(okno1, text="Zatwierdz", ).grid(row=3, column=1, padx=2, pady=2)
    ok3 = tk.Button(okno1, text="Zatwierdz", ).grid(row=4, column=1, padx=2, pady=2)
    ok4 = tk.Button(okno1, text="Zatwierdz", ).grid(row=5, column=1, padx=2, pady=2)
    ok5 = tk.Button(okno1, text="Zatwierdz", ).grid(row=6, column=1, padx=2, pady=2)

    okno1.mainloop()
def logowanie():
    __login = 'login'
    __haslo = 'haslo'
    login = log.get()
    haslo = has.get()
    podlogin = login #input('Podaj login:')
    podhaslo = haslo  #input('Podaj hasło:')

    if podlogin == __login and podhaslo == __haslo:
        okno.destroy()
        wyswietlanie()
    else:
        okno_blad = tk.Tk()
        okno_blad.title('Błąd')
        okno_blad.geometry('100x100')

        tk.Label(okno_blad, text="Zły login lub hasło").grid(row=0, column=0, padx=2, pady=2)
        ok = tk.Button(okno_blad, text="spróbuj ponownie",command=okno_blad.destroy ).grid(row=2, column=0, padx=2, pady=2)
        k = tk.Button(okno_blad, text="Zakończ program",command=koniec ).grid(row=3, column=0, padx=2, pady=2)
        okno_blad.mainloop()
        okno.destroy()


while True:
    okno = tk.Tk()
    okno.title('Logowanie')
    okno.geometry('300x100')
    log = tk.StringVar()
    has = tk.StringVar()
    tk.Label(okno, text="Login").grid(row=0, column=0, padx=2, pady=2)
    wpis_log = tk.Entry(okno,textvariable=log).grid(row=0, column=1)

    tk.Label(okno, text="Haslo").grid(row=1, column=0, padx=2, pady=2)
    wpis_haslo = tk.Entry(okno, textvariable=has).grid(row=1, column=1)

    tk.Button(okno, text="Zatwierdz", command=logowanie).grid(row=2, column=0, padx=2, pady=2)
    tk.Button(okno, text="Zrezygnuj", command=koniec).grid(row=2, column=1, padx=2, pady=2)
    okno.mainloop()
