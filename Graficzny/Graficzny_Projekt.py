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


def listaOsob(okno):
    a = 1
    b = 1
    for i, y in osoby.items():
        tk.Label(okno,bg='yellow',justify='right',foreground='#FF7D7D', activeforeground='yellow', text=str(i) + ':' + str(y) + '\n').grid(row=b, column=3)
        a += 1
        b += 1

def zamknijOkno(okno):
    okno.destroy()

def koniec():
    sys.exit()


def oknoWyswietlPowiazania():
    oknoH = tk.Tk()
    oknoH.title('Wyświetl powiązania')
    oknoH.geometry('300x300')
    nrKont = tk.StringVar(oknoH)
    tk.Label(oknoH, text='nr kontaktu\ndo wyświetlenia').grid(row=0, column=0)
    tk.Entry(oknoH, textvariable=nrKont).grid(row=0, column=1)
    tk.Button(oknoH, text="Zatwierdz", command=lambda: powiazaneKontakty(nrKont, oknoH)).grid(row=2, column=0, padx=2, pady=2)
    oknoH.mainloop()

def powiazaneKontakty(strVar, oknoG):
    kontakt = strVar.get()
    tk.Button(oknoG, text="Zamknij  ",command= lambda:zamknijOkno(oknoG)).grid(row=2, column=0, padx=2, pady=2)
    try:
        c = kontakty[str(kontakt)]
        tk.Label(oknoG, text='Powiązania dla kontaktu:\n'+ str(osoby[kontakt])+':').grid(row=2, column=1)
        print('Powiązania dla kontaktu:', osoby[kontakt])
        try:
            a=4
            for i in c:
                i = str(i)
                if osoby[i] == 'osoba usunięta':
                    print()
                else:
                    tk.Label(oknoG, text=osoby[i]).grid(row=a, column=0)
                    #print(osoby[i])
                    a+=1
        except TypeError:
            b = str(c)
            if osoby[b] == 'osoba usunięta':
                print()
            else:
                tk.Label(oknoG, text=osoby[b]).grid(row=3, column=0)
                #print(osoby[b])
    except KeyError:
        tk.Label(oknoG, text='Brak powiązań,\n lub źle wpisany numer').grid(row=3, column=0)
        print('Brak powiązań, lub źle wpisany numer')


def oknopowiazania():
    oknoP = tk.Tk()
    oknoP.title('Powiązania')
    oknoP.geometry('300x100')

    pierwszy = tk.StringVar(oknoP)
    drugi = tk.StringVar(oknoP)
    tk.Label(oknoP, text='Nr pierwszej osoby').grid(row=0, column=0)
    tk.Entry(oknoP, textvariable=pierwszy).grid(row=0, column=1)
    tk.Label(oknoP, text='Numer drugiej osoby').grid(row=1, column=0)
    tk.Entry(oknoP, textvariable=drugi).grid(row=1, column=1)
    tk.Button(oknoP, text="Zatwierdz", command=lambda: powiazania(pierwszy, drugi, oknoP)).grid(row=2, column=0, padx=2, pady=2)
    tk.Button(oknoP, text="Zrezygnuj", command=lambda: zamknijOkno(oknoP)).grid(row=2, column=1, padx=2, pady=2)
    oknoP.mainloop()

def powiazania(pierwszy, drugi, okno):
    nr1 = pierwszy.get()
    nr2 = drugi.get()
    a = str(nr1)
    b = str(nr2)


    if kontakty.get(a) == None:
            kontakty[a] = b
    else:
        kontakty[a] = kontakty.get(a), b

    if kontakty.get(b)  == None:
        kontakty[b] = a
    else:
        kontakty[b] = kontakty.get(b), a

    with open('kontakty.json','w') as file:
        json.dump(kontakty, file)

    zamknijOkno(okno)


def dodajOsobe(x,y,okno):
    okno.destroy()
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
    tk.Button(oknoD, text="Zatwierdz", command=lambda: dodajOsobe(imie, nazwisko,oknoD)).grid(row=2, column=0, padx=2, pady=2)
    tk.Button(oknoD, text="Zrezygnuj", command=lambda: zamknijOkno(oknoD)).grid(row=2, column=1, padx=2, pady=2)
    oknoD.mainloop()

def oknoUsun():
    oknoU = tk.Tk()
    oknoU.title('Usuń osobę')
    oknoU.geometry('300x100')
    numer = tk.StringVar(oknoU)
    tk.Label(oknoU, text='Nr osoby do usunięcia').grid(row=0, column=0)
    tk.Entry(oknoU, textvariable=numer).grid(row=0, column=1)
    tk.Button(oknoU, text="Zatwierdz", command=lambda: usunOsobe(numer,oknoU)).grid(row=2, column=0, padx=2, pady=2)
    tk.Button(oknoU, text="Zrezygnuj", command=lambda: zamknijOkno(oknoU)).grid(row=2, column=1, padx=2, pady=2)
    oknoU.mainloop()

def usunOsobe(nrStrVar, okno):
    okno.destroy()
    nrOsoby = nrStrVar.get()
    osoby[nrOsoby]= 'None'
    with open('osoby.json', 'w') as file:
        json.dump(osoby, file)
    kontakty.pop(nrOsoby)
    with open('kontakty.json','w') as file:
        json.dump(kontakty, file)

def wyswietlanie():

    okno1 = tk.Tk()
    okno1.title('Program',)
    okno1.geometry('480x480')
    okno1.config(bg='yellow')
    tekstowe= tk.Text(okno1,width = 29, height = 50)
    tekstowe.place(x=1,y=180)
    tekstowe.insert(tk.END,'⠀⠀⠀⠀⣠⡤⠒⠂⢀⣈⣉⠉⠑⠒⠢⠤⡀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⡰⠉⢁⣰⣶⣾⣿⣿⣿⣿⣷⣶⣼⣶⣼⣆⠀⠀⠀⠀⠀⠀\n⠀⢠⣁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀\n⠀⣿#byFCA⠛⠉⠉⠁⠀⠈⠉⠉⠙⠻⣿⣿⣷⣿⡄⠀⠀\n⠀⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⣿⢱⠀⠀\n⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣟⠂⡇⠀\n⠀⣿⣿⠀⢀⣤⣶⣶⣦⠀⠀⢠⣴⣿⣷⣶⡄⠀⠘⢿⣿⣧⡇⠀\n⢸⣿⡏⠀⠠⡶⢽⡶⠿⠃⠀⠘⢿⠿⠶⠟⠿⠂⠀⢸⣿⣿⡿⡀\n⡜⢿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠋⠀⡇\n⢱⠈⠙⠀⠀⠀⠀⣠⢠⣤⣤⣤⣤⣤⡤⡀⠀⠀⠀⠀⠀⣤⠀⢰\n⢸⠀⢢⡄⠀⠀⠴⣧⣴⡶⢿⢿⣿⣿⣿⣾⣦⠀⡀⢠⣆⠀⠙⠸\n⢠⠀⠈⣷⣀⡀⠨⣿⢿⢋⣉⣉⣉⣙⡿⣿⡿⣠⣟⣾⡿⣤⡠\n⠘⠦⠤⣿⣿⣷⣼⣿⠀⠉⠉⠉⠉⠉⠀⢸⣿⣿⣿⣿⣿⠁⠀⠀\n⠀⠀⠀⢸⢻⣿⣿⣿⣶⡀⠾⣦⣷⠔⢧⣾⣿⣿⣿⣿⢸⠀⠀⠀\n⠀⠀⢀⣾⠀⠉⣿⣿⣿⣧⣦⣻⣳⣶⣿⣿⣿⣾⣿⡿⢸⠀⠀⠀\n⠀⢀⣿⣿⡀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⢸⣧⠀⠀\n⠀⢸⣿⣿⣇⠀⠈⠿⢿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠀⠀⣿⣿⡆⠀\n⠀⠈⢿⣿⣿⡄⠀⠀⠀⠉⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⣿⣿⣇⠀\n⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⠀\n⠀⠀⠀⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⡇⠀\n⠀⠀⠀⠘⢿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠟⠁⠀\n⠀⠀⠀⠀⠀⠙⠿⢿⣿⣿⣶⣄⡀⠀⠀⠀⠀⣰⣿⣿⠋⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣦⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣷⣤⣺⣿⡇⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⣿⠿⠋⠀⠀⠀⠀⠀⠀\n\n🐐        🐐')

    tk.Label(okno1, relief='ridge', bg='#44A7FF', text="1 - wyświetl sieć kontaktów                           ").grid(row=1, column=0, padx=2, pady=2)
    tk.Label(okno1, relief='ridge', bg='#44A7FF', text="2 - dodaj osobę                                               ").grid(row=2, column=0, padx=2, pady=2)
    tk.Label(okno1, relief='ridge', bg='#44A7FF', text="3 - dodaj powiązanie pomiędzy kontaktami").grid(row=3, column=0, padx=2, pady=2)
    tk.Label(okno1, relief='ridge', bg='#44A7FF', text="4 - wyświetl powiązane osoby z kontaktem ").grid(row=4, column=0, padx=2, pady=2)
    tk.Label(okno1, relief='ridge', bg='#44A7FF', text="5 - usuń osobę                                                  ").grid(row=5, column=0, padx=2, pady=2)
    tk.Label(okno1, relief='ridge', bg='#44A7FF', text="9 - zamknij                                                        ").grid(row=6, column=0, padx=2, pady=2)

    tk.Button(okno1,bg='#99FF29',activebackground ='purple', text="Zatwierdz", command=lambda: listaOsob(okno1)).grid(row=1, column=1, padx=2, pady=2)
    tk.Button(okno1,bg='#99FF29',activebackground ='purple', text="Zatwierdz", command=oknoDodajOsobe ).grid(row=2, column=1, padx=2, pady=2)
    tk.Button(okno1,bg='#99FF29',activebackground ='purple', text="Zatwierdz", command=oknopowiazania ).grid(row=3, column=1, padx=2, pady=2)
    tk.Button(okno1,bg='#99FF29',activebackground ='purple', text="Zatwierdz", command=oknoWyswietlPowiazania ).grid(row=4, column=1, padx=2, pady=2)
    tk.Button(okno1,bg='#99FF29',activebackground ='purple', text="Zatwierdz", command=oknoUsun ).grid(row=5, column=1, padx=2, pady=2)
    tk.Button(okno1,bg='red',activebackground ='purple', text="Zamknij",command=koniec,width = 8, height = 1 ).grid(row=6, column=1, padx=2, pady=2)

    okno1.mainloop()
def logowanie(logi, hasl,okno):
    __login = 'login'
    __haslo = 'haslo'
    podlogin = logi.get()
    podhaslo = hasl.get()

    if podlogin == __login and podhaslo == __haslo:
        okno.destroy()
        wyswietlanie()
    else:
        okno_blad = tk.Tk()
        okno_blad.title('Błąd')
        okno_blad.geometry('200x200')

        tk.Label(okno_blad,text='               ').grid(row=1, column=1, )
        tk.Label(okno_blad,bg='red', text="Zły login lub hasło").grid(row=1, column=3,)
        tk.Button(okno_blad, text="spróbuj ponownie",command=okno_blad.destroy ).grid(row=2, column=3, )
        tk.Button(okno_blad, text="Zakończ program",command=koniec ).grid(row=3, column=3, )
        okno_blad.mainloop()
        okno.destroy()


def poczatek():
    okno = tk.Tk()
    okno.title('Logowanie')
    okno.geometry('300x100')
    log = tk.StringVar()
    has = tk.StringVar()
    tk.Label(okno, text="Login").grid(row=0, column=0, padx=2, pady=2)
    tk.Entry(okno,textvariable=log).grid(row=0, column=1)

    tk.Label(okno, text="Haslo").grid(row=1, column=0, padx=2, pady=2)
    tk.Entry(okno, textvariable=has).grid(row=1, column=1)

    tk.Button(okno, text="Zatwierdz", command=lambda: logowanie(log, has, okno)).grid(row=2, column=0, padx=2, pady=2)
    tk.Button(okno, text="Zrezygnuj", command=koniec).grid(row=2, column=1, padx=2, pady=2)
    okno.mainloop()
wyswietlanie()