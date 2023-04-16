import tkinter as tk
import tkinter.simpledialog as simpledialog


class Category:
    def __init__(self, name):
        self.name = name
        self.items = []


class ShoppingListApp:
    def __init__(self, master):
        self.master = master
        master.title("Lista zakupów")

        # etykieta z tytułem
        self.title_label = tk.Label(master, text="Do kupienia", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # kontener z przyciskami kategorii
        self.categories_frame = tk.Frame(master)
        self.categories_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # przycisk "Dodaj kategorię"
        self.add_category_button = tk.Button(master, text="Dodaj kategorię", command=self.add_category)
        self.add_category_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # słownik przechowujący kategorie
        self.categories = {}

    def add_category(self):
        # otwiera okno dialogowe z prośbą o wpisanie nazwy kategorii
        category_name = simpledialog.askstring("Nowa kategoria", "Wpisz nazwę kategorii:")
        if category_name:
            # dodaje nową kategorię do słownika i tworzy dla niej przycisk
            self.categories[category_name] = Category(category_name)
            category_button = tk.Button(self.master, text=category_name,
                                        command=lambda name=category_name: self.open_category(name))
            category_button.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)


    def open_category(self, category_name):
        # tworzy nowe okno z przyciskami i polami tekstowymi dla wybranej kategorii
        category = self.categories[category_name]
        window = tk.Toplevel(self.master)
        window.title(category_name)
        window.geometry("400x400")

        # przycisk "Dodaj element"
        add_item_button = tk.Button(window, text="Dodaj element", command=lambda: self.add_item(category, items_frame))
        add_item_button.pack(side=tk.TOP, padx=10, pady=10)

        # ramka z elementami kategorii
        items_frame = tk.Frame(window)
        items_frame.pack(side=tk.TOP, padx=10, pady=10)

        # dodaje elementy kategorii do ramki
        for item in category.items:
            self.add_item(category, items_frame, item)

    def add_item(self, category, frame, item_text=None):
        # dodaje nowy element do kategorii i ramki z elementami
        if item_text is None:
            item_text = simpledialog.askstring("Nowy element", "Wpisz nazwę elementu:")
        if item_text:
            category.items.append(item_text)
            item_frame = tk.Frame(frame)
            item_frame.pack(side=tk.TOP, padx=5, pady=5)
            item_label = tk.Label(item_frame, text=item_text, width=30)
            item_label.pack(side=tk.LEFT)
            delete_button = tk.Button(item_frame, text="Usuń",
                                      command=lambda: self.delete_item(category, frame, item_frame, item_text))
            delete_button.pack(side=tk.LEFT, padx=5)

    def delete_item(self, category, frame, item_frame, item_text):
        # usuwa wybrany element z kategorii i ramki z elementami
        category.items.remove(item_text)
        item_frame

root = tk.Tk()
root.geometry('350x350')
app = ShoppingListApp(root)
root.mainloop()