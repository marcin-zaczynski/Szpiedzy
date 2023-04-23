from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <html>
            <body>
                <h1>Kalkulator ilości kartek na arkuszu</h1>
                <form action="/calculate" method="post">
                    <label for="arkusz_dlugosc">Długość arkusza (w cm): </label>
                    <input type="number" id="arkusz_dlugosc" name="arkusz_dlugosc" required><br><br>
                    <label for="arkusz_szerokosc">Szerokość arkusza (w cm): </label>
                    <input type="number" id="arkusz_szerokosc" name="arkusz_szerokosc" required><br><br>
                    <label for="kartka_dlugosc">Długość kartki (w cm): </label>
                    <input type="number" id="kartka_dlugosc" name="kartka_dlugosc" required><br><br>
                    <label for="kartka_szerokosc">Szerokość kartki (w cm): </label>
                    <input type="number" id="kartka_szerokosc" name="kartka_szerokosc" required><br><br>
                    <input type="submit" value="Oblicz">
                </form>
                <br>
                <img src="/static/arkusz.png" alt="Układ kartek na arkuszu" width="500">
            </body>
        </html>
    '''

@app.route('/calculate', methods=['POST'])
def calculate():
    arkusz_dlugosc = request.form['arkusz_dlugosc']
    arkusz_szerokosc = request.form['arkusz_szerokosc']
    kartka_dlugosc = request.form['kartka_dlugosc']
    kartka_szerokosc = request.form['kartka_szerokosc']

    ilosc_kartek = (int(arkusz_dlugosc) * int(arkusz_szerokosc)) // (int(kartka_dlugosc) * int(kartka_szerokosc))

    return '''
        <html>
            <body>
                <h1>Wynik:</h1>
                <p>Ilość kartek, które zmieszczą się na arkuszu to: {}</p>
                <br>
                <img src="/static/kartki_na_arkuszu.png" alt="Układ kartek na arkuszu" width="500">
            </body>
        </html>
    '''.format(ilosc_kartek)

if __name__ == '__main__':
    app.run(debug=True)