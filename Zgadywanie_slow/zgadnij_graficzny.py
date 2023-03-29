import random
import json
import tkinter as tk
import sys

with open("slowa.json", "r", encoding="utf-8") as file:
    slowa = json.load(file)
slowo = random.choice(slowa)

rozwiazanie = ['_','_','_','_','_']
podane=['pierwsze']
uzyte = []
ilosc_prob = [0]

def display_info(do_sprawdzenia):
    sprawdz = do_sprawdzenia.get()
    ilosc_prob[0]+=1
    podane[0] = sprawdz
    for litera in sprawdz:
        if litera in slowo:
            rozwiazanie[slowo.index(litera)] = litera
            x = slowo.index(litera)
            next = slowo[x + 1:]
            if litera in str(next):
                rozwiazanie[next.index(litera) + (x + 1)] = litera
    uzyte.append(sprawdz)
    wyswietl(sprawdz)

def wyswietl(sprawdz):
    if podane[0] == slowo and ilosc_prob[0]<11:
        rezultat.config(bg='yellow',text='Gratulacje,\n udało Ci się zgadnąć hasło za\n '+str(ilosc_prob[0])+' razem')
        button.config(text='Zakończ',command=koniec)
    if ilosc_prob[0] > 10:
        rezultat.config(bg='red',text='Przegrałeś,\n odpowiedź to słowo\n '+slowo + ' \nspróbuj ponownie')
        button.config(text='Zakończ', command=koniec)
    entry.delete(0, 'end')
    info_prob.config(text='Pozostało ' + str(10 - int(ilosc_prob[0])) + ' prób')
    info_postep.config(text=rozwiazanie)
    textbox.insert(tk.END, sprawdz+'\n', ("p"))

def koniec():
    sys.exit()

window = tk.Tk()
window.geometry('300x400')

info_prob = tk.Label(window,text='')
info_prob.pack()
info_prob.place(x=30, y=10)

info_postep = tk.Label(window,text=rozwiazanie)
info_postep.pack()
info_postep.place(x=50, y=30)

info_label = tk.Label(window, text="Spróbuj odgadnąć słowo\n 5-cio literowe")
info_label.pack()
info_label.place(x=20, y=60)

do_sprawdzenia = tk.StringVar()
entry = tk.Entry(window, textvariable= do_sprawdzenia)
entry.pack()
entry.place(x=20, y=100)
def character_limit(entry_text):
    if len(do_sprawdzenia.get()) > 0:
        entry_text.set(entry_text.get()[:5])
do_sprawdzenia.trace("w", lambda *args: character_limit(do_sprawdzenia))

button = tk.Button(window, text="Zatwierdź", command=lambda : display_info(do_sprawdzenia))
button.pack()
button.place(x=50, y=130)

button_koniec = tk.Button(window, text="Zakończ program", command= koniec)
button_koniec.pack()
button_koniec.place(x=30, y=250)

rezultat = tk.Label(window,text='')
rezultat.pack()
rezultat.place(x=20, y=160)

textbox = tk.Text(window, width = 20, height = 20)
textbox.pack()
textbox.place(x=170, y=0)
textbox.insert(tk.END, "Użyta słowa:"+'\n', ("h1"))

window.mainloop()