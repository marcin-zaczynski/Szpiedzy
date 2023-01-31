import sys
import tkinter as tk

def koniec():
    sys.exit()



def wyswietlanie():
    import tkinter as tk

    okno1 = tk.Tk()
    okno1.title = 'Wyświetlanie'
    okno1.geometry('480x480')

    c = tk.Label(okno1, text='ddafafd')
    c.grid(row=0, column=0)
    c.config(background='yellow')

    tk.Label(okno1, text="1 - wyświetl sieć kontaktów").grid(row=1, column=0, padx=2, pady=2)
    tk.Label(okno1, text="2 - dodaj osobę").grid(row=2, column=0, padx=2, pady=2)
    tk.Label(okno1, text="3 - dodaj powiązanie pomiędzy kontaktami").grid(row=3, column=0, padx=2, pady=2)
    tk.Label(okno1, text="4 - wyświetl powiązane osoby z kontaktem").grid(row=4, column=0, padx=2, pady=2)
    tk.Label(okno1, text="5 - usuń osobę").grid(row=5, column=0, padx=2, pady=2)
    tk.Label(okno1, text="9 - zamknij").grid(row=6, column=0, padx=2, pady=2)

    ok = tk.Button(okno1, text="Zatwierdz", ).grid(row=1, column=1, padx=2, pady=2)
    ok1 = tk.Button(okno1, text="Zatwierdz", ).grid(row=2, column=1, padx=2, pady=2)
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
        print('Dostęp uznany')
        okno.destroy()
        wyswietlanie()
    else:
        okno_blad = tk.Tk()
        okno_blad.title = 'Błąd'
        okno_blad.geometry('100x100')

        tk.Label(okno_blad, text="Zły login lub hasło").grid(row=0, column=0, padx=2, pady=2)
        ok = tk.Button(okno_blad, text="spróbuj ponownie",command=okno_blad.destroy ).grid(row=2, column=0, padx=2, pady=2)
        k = tk.Button(okno_blad, text="Zakończ program",command=koniec ).grid(row=3, column=0, padx=2, pady=2)
        okno_blad.mainloop()
        okno.destroy()


while True:
    okno = tk.Tk()
    okno.title = 'Logowanie'
    #okno.geometry('300x170')
    log = tk.StringVar()
    has = tk.StringVar()
    tk.Label(okno, text="Login").grid(row=0, column=0, padx=2, pady=2)
    wpis_log = tk.Entry(okno,textvariable=log).grid(row=0, column=1)

    tk.Label(okno, text="Haslo").grid(row=1, column=0, padx=2, pady=2)
    wpis_haslo = tk.Entry(okno, textvariable=has).grid(row=1, column=1)

    ok = tk.Button(okno, text="Zatwierdz", command=logowanie).grid(row=2, column=0, padx=2, pady=2)

    okno.mainloop()

