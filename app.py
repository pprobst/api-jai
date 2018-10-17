from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS
import json

app = Flask(__name__)

# Expõe tudo em /jai/ para o CORS e permite content-type header;
# necessário para utilizar os recursos localmente com GET/POST usados no Ionic.
 CORS(app, resources=r'/jai/*')

# auth = HTTPBasicAuth() # desnecessário por enquanto

null = None
false = False
true = True

with open('data.json') as json_data:
    trabalhos = json.load(json_data)

with open('data2.json') as json_data2:
    modulos = json.load(json_data2)

# Aqui eu me distanciei um pouco da documentação; nela, não está claro como as avaliações
# dos trabalhos estão separadas. Por conta disso, tomei a liberdade de fazer uma lista.
avaliacoes = [
        {
            "trabalho": 25424,
            "respostas": {
                "141": "9",
                "142": "8",
                "143": "9",
                "144": "8",
                "145": "8",
                "146": "6",
                "147": "7",
                "148": "7",
                "149": "4",
                "150": "9",
                "151": "7"
            }
        }
]

edicao_corrente = {
        "id": null,
        "error": false,
        "codigo": 1001,
        "mensagem": "Sucesso",
        "edicao": {
            "ano": 2018,
            "fim": "2018-10-26T00:00:00-03:00",
            "id": 84,
            "inicio": "2018-10-22T00:00:00-03:00",
            "nome": "33ª Jornada Acadêmica Integrada"
            },
        "errorEntity": false
        }

# GET todos os trabalhos
@app.route('/jai/avaliacaoRest/findTrabalhos', methods=['GET'])
def get_trabalhos():
    return jsonify({'trabalhos': trabalhos['trabalhos']})
    #return jsonify({'trabalhos': trabalhos['trabalhos'][0]['trabalho']['perguntas'][1]['id']})

# GET trabalho específico
@app.route('/jai/avaliacaoRest/findTrabalhos/<int:trabalho_id>', methods=['GET'])
def get_trabalho(trabalho_id):
    trabalho = [trabalho for trabalho in trabalhos['trabalhos'] if trabalho['trabalho']['id'] == trabalho_id]
    if len(trabalho) == 0:
        abort(404)
    return jsonify({'trabalho': trabalho[0]})

# GET perguntas
@app.route('/jai/avaliacaoRest/findTrabalhos/<int:trabalho_id>/perguntas', methods=['GET'])
def get_perguntas(trabalho_id):
    trabalho = [trabalho for trabalho in trabalhos['trabalhos'] if trabalho['trabalho']['id'] == trabalho_id]
    perguntas = trabalho[0]['trabalho']['perguntas']
    #pergunta = [pergunta['id'] for pergunta in perguntas]

    if len(trabalho) == 0 or len(perguntas) == 0:
        abort(404)
    return jsonify({'perguntas': perguntas})


# GET todas as avaliacoes
@app.route('/jai/avaliacaoRest/postAvaliacao', methods=['GET'])
def get_avaliacoes():
    return jsonify({'avaliacoes': avaliacoes})

# POST nova avaliacao
@app.route('/jai/avaliacaoRest/postAvaliacao', methods=['POST'])
def post_avaliacao():
    if not request.json:
        abort(400)

    trabalho_id = request.json['trabalho']

    trabalho = [trabalho for trabalho in trabalhos['trabalhos'] if trabalho['trabalho']['id'] == trabalho_id]
    if len(trabalho) == 0:
        abort(404)

    perguntas = trabalho[0]['trabalho']['perguntas']
    pergunta_ids = [pergunta['id'] for pergunta in perguntas]

    avaliacao = {
            "trabalho": trabalho_id,
            "respostas": {
            }
        }

    for pergunta_id in pergunta_ids:
        avaliacao['respostas'][str(pergunta_id)] = request.json[str(pergunta_id)]

    for aval in avaliacoes:
        if aval['trabalho'] == trabalho_id:
            avaliacoes.remove(aval)
            break

    avaliacoes.append(avaliacao)

    """ atualiza o json (descontinuado!)
    # aqui, a resposta (nota) das perguntas de um trabalho são atualizadas com as respostas recebidas pelo POST
    trabalho_id = avaliacao.get("trabalho")
    trabalho = [trabalho for trabalho in trabalhos['trabalhos'] if trabalho['trabalho']['id'] == trabalho_id]

    for pergunta in trabalho[0]['trabalho']['perguntas']:
        for resposta in avaliacao['respostas']:
            if resposta == str(pergunta['id']):
                pergunta['resposta'] = avaliacao['respostas'][resposta]
    """

    return jsonify({'avaliacao':avaliacao["trabalho"]}), 201

# GET das informações sobre a edição atual da JAI
@app.route('/jai/avaliacaoRest/findEdicao', methods=['GET'])
def get_edicao():
    return jsonify({'edição': edicao_corrente})

# GET dos módulos
@app.route('/jai/avaliacaoRest/findModulos', methods=['GET'])
def get_modulos():
    return jsonify({'modulos': modulos})


# GET dos trabalhos da data passada
@app.route('/jai/avaliacaoRest/findTrabalhosModulo', methods=['GET'])
def get_trabalhos_modulo():
    #if not request.json:
    #    abort(400)

    data_trabalho = request.args.get('data')
    modulo_trabalho = request.args.get('modulo')
    agrupadores = modulos['agrupadores']
    modulos_todos = [modulo['modulos'] for modulo in agrupadores]
    modulos_indiv = []
    for mod in modulos_todos:
        for m in mod:
            modulos_indiv.append(m)
    modulo = [modulo for modulo in modulos_indiv if str(modulo['id']) == modulo_trabalho]
    if len(modulo) == 0:
        abort(404)

    trabalhos_modulo = [mod['trabalhos'] for mod in modulo]
    trabalhos_modulo_indiv = []
    for trab in trabalhos_modulo:
        for t in trab:
            trabalhos_modulo_indiv.append(t)

    trabalho = [trabalho for trabalho in trabalhos_modulo_indiv if trabalho['trabalho']['apresentacao']['data'][:10] == data_trabalho]
    if len(trabalho) == 0:
        abort(404)

    return jsonify({'trabalhos': trabalho})

if __name__ == '__main__':
    app.run(debug=True)
