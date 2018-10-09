from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth
from flask_cors import CORS

app = Flask(__name__)

# Expõe tudo em /jai/ para o CORS e permite content-type header;
# necessário para utilizar os recursos localmente com GET/POST usados no Ionic.
CORS(app, resources=r'/jai/*')

# auth = HTTPBasicAuth() # desnecessário por enquanto

null = None
false = False
true = True

trabalhos = {
        "id": null,
        "erro": false,
        "mensagem": "Sucesso",
        "trabalhos": [
    {
            "trabalho": {
                "id": 25424,
                "titulo": "SOBRE JORNALISTAS MILITANTES: FORMAÇÃO, PARTICIPAÇÃO E JORNALISMO EM MOVIMENTOS SOCIAIS",
                "apresentador": "JULIA MARA SAGGIORATO",
                "apresentacao": {
                    "data": "2018-05-11T09:12:43:435",
                    "predio": "CSSH 74A",
                    "sala": "Painel 12"
                        },
        "perguntas": [
    #{
    #            "discursiva":true,
    #            "id":121,
    #            "nome": "Preencha o campo ao lado com a palavra \"APROVADO\" e, caso deseje, faça um comentário sobre a qualidade do trabalho. Caso o trabalho necessite revisão ou não seja aprovado, use o campo para escrever sua justificativa.",
    #            "respostas":null
    #                    },
            {
                "discursiva":false,
                "id":141,
                "nome": "O título do trabalho reflete seu conteúdo e as palavras usadas são adequadas?",
                "resposta": "0;1;2;3;4;5"
                            },
             {
                "discursiva":false,
                "id":142,
                "nome": "O tema do trabalho é relevante na sua respectiva área do conhecimento?",
                "resposta": "0;1;2;3;4;5"
                            },
            {
                "discursiva":false,
                "id":143,
                "nome": "O título do trabalho reflete seu conteúdo e as palavras usadas são adequadas?",
                "resposta": "0;1;2;3;4;5"
                            },
            {
                "discursiva":false,
                "id":144,
                "nome": "A contextualização do trabalho com a literatura e/ou processos criativos existentes é feita de forma satisfatória?",
                "resposta": "0;1;2;3;4;5"
                            },
            {
                "discursiva":false,
                "id":145,
                "nome": " A metodologia empregada no trabalho reflete o atual estado da arte na sua respectiva área do conhecimento?",
                "resposta": "0;1;2;3;4;5"
                            },
            {
                "discursiva":false,
                "id":146,
                "nome": "Os resultados são apresentados de forma clara, estruturada e coerente, utilizando-se dos meios adequados (tabelas, gráficos etc)?",
                "resposta": "0;1;2;3;4;5"
                            },
            {
                "discursiva":false,
                "id":147,
                "nome": " A discussão dos resultados enfatizou seus aspectos mais relevantes e suas limitações?",
                "resposta": "0;1;2;3;4;5"
                            },
            {
                "discursiva":false,
                "id":148,
                "nome": "As conclusões do trabalho são coerentes com seus resultados, métodos e objetivos?",
                "resposta": "0;1;2;3;4;5"
                            },
            {
                "discursiva":false,
                "id":149,
                "nome": "O pôster ou os slides continham as informações necessárias de forma sintética e objetiva?",
                "resposta": "0;1;2;3;4;5"
                            },
            {
                "discursiva":false,
                "id":150,
                "nome": "O apresentador domina o conteúdo do trabalho apresentado?",
                "resposta": "0;1;2;3;4;5"
                            },
            {
                "discursiva":false,
                "id":151,
                "nome": "Qual nota o(a) Sr(a) daria para o trabalho/apresentador como um todo?",
                "resposta": "0;1;2;3;4;5"
                            }
            ]
        }
        },
    {
            "trabalho": {
                "id": 25426,
                "orientador": "OSVALDO BAZZAN KAIZER",
                "titulo": "ADESIVO CONTENDO SILANO INFLUENCIA NA RESISTÊNCIA ADESIVA DOS PINOS DE FIBRA DE VIBRO",
                "apresentador": "PATRÍCIA ELIANA FONTANA",
                "apresentacao": {
                    "data": "2018-09-06T00:00:00-03:00",
                    "predio": "GINÁSIO POLIVALENTE - PARQUE DE EXPOSIÇÕES",
                    "sala": "Painel 247"
                        },
            "perguntas": [
            #{
            #   "discursiva":true,
            #   "id":121,
            #   "nome": "Preencha o campo ao lado com a palavra \"APROVADO\" e, caso deseje, faça um comentário sobre a qualidade do trabalho. Caso o trabalho necessite revisão ou não seja aprovado, use o campo para escrever sua justificativa.",
            #   "respostas":null
            #   },
            {
                "discursiva":false,
                "id":163,
                "nome": "O título do trabalho reflete seu conteúdo e as palavras usadas são adequadas?",
                "resposta": "Sim;Não"
                            },
             {
                "discursiva":false,
                "id":164,
                "nome": "O tema do trabalho é relevante na sua respectiva área do conhecimento?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":165,
                "nome": "O título do trabalho reflete seu conteúdo e as palavras usadas são adequadas?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":166,
                "nome": "A contextualização do trabalho com a literatura e/ou processos criativos existentes é feita de forma satisfatória?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":167,
                "nome": " A metodologia empregada no trabalho reflete o atual estado da arte na sua respectiva área do conhecimento?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":168,
                "nome": "Os resultados são apresentados de forma clara, estruturada e coerente, utilizando-se dos meios adequados (tabelas, gráficos etc)?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":169,
                "nome": " A discussão dos resultados enfatizou seus aspectos mais relevantes e suas limitações?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":170,
                "nome": "As conclusões do trabalho são coerentes com seus resultados, métodos e objetivos?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":171,
                "nome": "O pôster ou os slides continham as informações necessárias de forma sintética e objetiva?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":172,
                "nome": "O apresentador domina o conteúdo do trabalho apresentado?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":173,
                "nome": "Qual nota o(a) Sr(a) daria para o trabalho/apresentador como um todo?",
                "resposta": "0;1;2;3;4;5"
                            }
            ]
        }
        },
    {
            "trabalho": {
                "id": 25425,
                "titulo": "TRACTATUS LOGICO-PHILOSOFICUS",
                "apresentador": "LUDWIG WITTGENSTEIN",
                "apresentacao": {
                    "data": "2018-05-11T09:14:48:235",
                    "predio": "CSSH 74A",
                    "sala": "Painel 12"
                        },
        "perguntas": [
    #{
    #            "discursiva":true,
    #            "id":121,
    #            "nome": "Preencha o campo ao lado com a palavra \"APROVADO\" e, caso deseje, faça um comentário sobre a qualidade do trabalho. Caso o trabalho necessite revisão ou não seja aprovado, use o campo para escrever sua justificativa.",
    #            "respostas":null
    #                    },
            {
                "discursiva":false,
                "id":152,
                "nome": "O título do trabalho reflete seu conteúdo e as palavras usadas são adequadas?",
                "resposta": "Sim;Não"
                            },
             {
                "discursiva":false,
                "id":153,
                "nome": "O tema do trabalho é relevante na sua respectiva área do conhecimento?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":154,
                "nome": "O título do trabalho reflete seu conteúdo e as palavras usadas são adequadas?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":155,
                "nome": "A contextualização do trabalho com a literatura e/ou processos criativos existentes é feita de forma satisfatória?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":156,
                "nome": " A metodologia empregada no trabalho reflete o atual estado da arte na sua respectiva área do conhecimento?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":157,
                "nome": "Os resultados são apresentados de forma clara, estruturada e coerente, utilizando-se dos meios adequados (tabelas, gráficos etc)?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":158,
                "nome": " A discussão dos resultados enfatizou seus aspectos mais relevantes e suas limitações?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":159,
                "nome": "As conclusões do trabalho são coerentes com seus resultados, métodos e objetivos?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":160,
                "nome": "O pôster ou os slides continham as informações necessárias de forma sintética e objetiva?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":161,
                "nome": "O apresentador domina o conteúdo do trabalho apresentado?",
                "resposta": "Sim;Não"
                            },
            {
                "discursiva":false,
                "id":162,
                "nome": "Qual nota o(a) Sr(a) daria para o trabalho/apresentador como um todo?",
                "resposta": "0;1;2;3;4;5"
                            }
            ]
        }
        }
        ],
        "errorEntity":false
}

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

modulos = {
        "id": null,
        "error": false,
        "codigo": 1001,
        "mensagem": "Sucesso",
        "agrupadores": [
            {
                "id": 66,
                "modulos": [
                    {
                        "id": 464,
                        "nome": "QUÍMICA/MATERIAIS",
                        "trabalhos": [
                            {
                                "trabalho": {
                                "id": 25426,
                                "orientador": "OSVALDO BAZZAN KAIZER",
                                "titulo": "ADESIVO CONTENDO SILANO INFLUENCIA NA RESISTÊNCIA ADESIVA DOS PINOS DE FIBRA DE VIBRO",
                                "apresentador": "PATRÍCIA ELIANA FONTANA",
                                "apresentacao": {
                                    "data": "2018-09-06T00:00:00-03:00",
                                    "predio": "GINÁSIO POLIVALENTE - PARQUE DE EXPOSIÇÕES",
                                    "sala": "Painel 247"
                                },
                                }
                                }
                            ]
                        }
                    ],
                "nome": "CIÊNCIAS EXATAS E DA TERRA"
                },
            {
                "id": 67,
                "modulos": [
                    {
                        "id": 465,
                        "nome": "SOCIOLOGIA/ESTUDOS DA SOCIEDADE",
                        "trabalhos": [
                            {
                                "trabalho": {
                                "id": 25424,
                                "titulo": "SOBRE JORNALISTAS MILITANTES: FORMAÇÃO, PARTICIPAÇÃO E JORNALISMO EM MOVIMENTOS SOCIAIS",
                                "apresentador": "JULIA MARA SAGGIORATO",
                                "apresentacao": {
                                    "data": "2018-05-11T09:12:43:435",
                                    "predio": "CSSH 74A",
                                    "sala": "Painel 12"
                                },
                                }
                                }
                            ]
                        },
                    {
                        "id": 501,
                        "nome": "FILOSOFIA/FILOSOFIA DA LINGUAGEM",
                        "trabalhos": [
                            {
                                "trabalho": {
                                "id": 25425,
                                "titulo": "TRACTATUS LOGICO-PHILOSOFICUS",
                                "apresentador": "LUDWIG WITTGENSTEIN",
                                "apresentacao": {
                                    "data": "2018-05-11T09:14:48:235",
                                    "predio": "CSSH 74A",
                                    "sala": "Painel 12"
                                },
                                }
                                }
                            ]
                        }
                    ],
                "nome": "CIÊNCIAS HUMANAS"
                }
            ],
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
