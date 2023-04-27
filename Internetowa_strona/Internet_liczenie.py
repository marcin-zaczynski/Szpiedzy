from flask import Flask, request

app = Flask(__name__)
dane = []
wyniki = []
@app.route('/')
def home():
    return '''
        <html>
            <body>
                <h1>Kalkulator ilości kart na arkuszu</h1>
                <form id="calculator-form">
                    <label for="arkusz_dlugosc">Długość arkusza (w cm): </label>
                    <input type="number" id="arkusz_dlugosc" name="arkusz_dlugosc" value="670" required><br><br>
                    <label for="arkusz_szerokosc">Szerokość arkusza (w cm): </label>
                    <input type="number" id="arkusz_szerokosc" name="arkusz_szerokosc" value="910" required><br><br>
                    <label for="kartka_dlugosc">Długość kartki (w cm): </label>
                    <input type="number" id="kartka_dlugosc" name="kartka_dlugosc" value=58 required><br><br>
                    <label for="kartka_szerokosc">Szerokość kartki (w cm): </label>
                    <input type="number" id="kartka_szerokosc" name="kartka_szerokosc" value=88 required><br><br>
                    <input type="button" value="Oblicz" onclick="calculate()">
                </form>
                <br>
                <div id="wynik"></div>
                <br>
                <script>
                    function calculate() {
                        const form = document.getElementById('calculator-form');
                        const formData = new FormData(form);
                        fetch('/calculate', {
                            method: 'POST',
                            body: formData
                        })
                        .then(response => response.text())
                        .then(data => {
                            document.getElementById('wynik').innerHTML = data;
                        })
                    }
                </script>
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
    dan = str(arkusz_dlugosc), str(arkusz_szerokosc),str(kartka_dlugosc), str(kartka_szerokosc)
    dane.append(dan)
    wyniki.append(ilosc_kartek)
    wynik_html = '''
            <h1>Wynik:</h1>
            <p>Ilość kart, które zmieszczą się na arkuszu to: {}</p>
            <p>Poprzednie wyniki to : {}</p>
        '''.format(ilosc_kartek, dane)

    return wynik_html

if __name__ == '__main__':
    app.run(debug=True)
