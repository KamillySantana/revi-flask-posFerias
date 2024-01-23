from flask import Flask, render_template

app = Flask(__name__)

listaDestinos = [
    {'nome': 'Paris', 'pais': 'França'},
    {'nome': 'Nova York', 'pais': 'Estados Unidos'},
    {'nome': 'Tóquio', 'pais': 'Japão'},
    {'nome': 'Sydney', 'pais': 'Austrália'},
    {'nome': 'Rio de Janeiro', 'pais': 'Brasil'},
    {'nome': 'Seoul', 'pais': 'Coreia do Sul'},
    {'nome': 'Pequim', 'pais': 'China'},
    {'nome': 'Roma', 'pais': 'Itália'}
]

@app.route('/')
def destinos_viagem():
    return render_template('viagem.html', destino=listaDestinos)

if __name__ == '__main__':
    app.run()
