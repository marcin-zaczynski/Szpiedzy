import tkinter as tk
from math import ceil

# Rozmiary arkuszy
sizes = [
    (560, 830),
    (670, 910),
    (720, 1000)
]

def calculate_max_sheets(card_width, card_height, num_cards, sizes):
    card_area = card_width * card_height
    max_sheet = None
    max_sheet_cards = None
    shift = None
    for size in sizes:
        sheet_area = size[0] * size[1]
        max_cards_on_sheet = int(sheet_area / card_area)
        if max_sheet_cards is None or max_cards_on_sheet > max_sheet_cards:
            max_sheet_cards = max_cards_on_sheet
            max_sheet = size
    if max_sheet_cards is not None:
        shift = num_cards % max_sheet_cards
    return max_sheet, max_sheet_cards, shift

def calculate_sheet():
    card_size_str = card_size_entry.get()
    num_cards_str = num_cards_entry.get()

    if not card_size_str or not num_cards_str:
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Proszę wprowadzić wymiary kart oraz ilość kart w talii.")
        result_entry.config(state="readonly")
        return

    if "x" not in card_size_str:
        result_entry.config(state="normal")
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Proszę wprowadzić wymiary kart w formacie <szerokość>x<wysokość>.")
        result_entry.config(state="readonly")
        return

    card_width, card_height = map(int, card_size_str.split("x"))
    num_cards = int(num_cards_str)

    best_sheet, max_cards_on_sheet, shift = calculate_max_sheets(card_width, card_height, num_cards, sizes)

    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)

    if best_sheet is None:
        result_entry.insert(0, "Nie znaleziono arkusza o odpowiednim rozmiarze.")
        result_entry.config(state="readonly")
        return
    else:
        num_sheets = ceil(num_cards / max_cards_on_sheet)
        if shift == 0:
            result_entry.insert(0, f"Potrzebujesz {num_sheets} arkuszy o rozmiarze {best_sheet}.")
        else:
            result_entry.insert(0, f"Potrzebujesz {num_sheets} arkuszy o rozmiarze {best_sheet}, "
                                   f"w tym jednego arkusza o rozmiarze {card_width}x{card_height} z {shift} kartami.")
        result_entry.config(state="readonly")


# Tworzymy okno
root = tk.Tk()
root.title("Kalkulator rozmiaru arkusza")
card_size_var = tk.StringVar(value="45x78")

# Tworzymy etykietę i pole tekstowe dla wymiarów kart
card_size_label = tk.Label(root, text="Wymiary kart (szerokość x wysokość):")
card_size_entry = tk.Entry(root, textvariable=card_size_var)
card_size_label.pack()
card_size_entry.pack()

# Tworzymy etykietę i pole tekstowe dla ilości kart w talii
card_var = tk.StringVar(value='40')
num_cards_label = tk.Label(root, text="Ilość kart w talii:")
num_cards_entry = tk.Entry(root, textvariable= card_var)
num_cards_label.pack()
num_cards_entry.pack()

# Tworzymy przycisk do obliczenia rozmiaru arkusza
calculate_button = tk.Button(root, text="Oblicz rozmiar arkusza", command=calculate_sheet)
calculate_button.pack()

#Tworzymy przycisk do wyświetlenia wyniku
calculate_button = tk.Button(root, text="Oblicz", command=calculate_sheet)
calculate_button.pack()

#Tworzymy etykietę i pole tekstowe dla wyniku
result_label = tk.Label(root, text="Wynik:")
result_entry = tk.Entry(root, state="readonly")
result_label.pack()
result_entry.pack()

root.mainloop()