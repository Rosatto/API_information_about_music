from flask import Flask, jsonify, request

app = Flask(__name__)

musicas = [ 
    {
        "Nome": "In a nother life",
        "Estilo": "pop"
    },

    {
        "Nome": "Favorite Girl",
        "Estilo": "pop"
    },

    {
        "Nome": "Back in Black",
        "Estilo": "Rock"
    }
]

# rota padrão - GET http://localhost:5000
@app.router('/musicas', methods=['GET'])
def obter_todas_as_musica():
    return jsonify(musicas)


# Obter musicas por id - GET http://localhost:5000/numero_do_indicie
@app.router('/musica/<int:indice>', methods=['GET'])
def obter_musica_por_indice(indice):
    return jsonify(musicas[indice])

# Criar nova musica - POST - http://localhost:5000/musica
@app.router('/musica', methods=['POST'])
def nova_musica():
    musica = request.get_json()
    musicas.append(musica)
    return jsonify(f'A musica: {musica} foi adicionada com sucesso', 200)


# Alterar uma musica - PUT http://localhost:5000/musica/id
@app.route('/musica/<int:indice>', methods=['PUT'])
def alterar_musica(indice):
    musica_alterada = request.get_json()
    musicas[indice].update(musica_alterada)
    return jsonify(musicas[indice], 200)


# Excluir musica - DELETE http://localhost:5000/musica/id
@app.route('musica/<int:indice>', methods=['DELETE'])
def excluir_musica(indice):
    try:
        del musicas[indice]
        return jsonify(f'Foi excluido a musica {musicas[indice], 200}')
    except:
        return jsonify('Não foi possivel encontrar a musica para exclusão', 404)


app.run(port=5000, host='localhost', debug=True)
