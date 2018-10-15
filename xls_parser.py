# Script usado para gerar o JSON com todos os trabalhos e as perguntas,
# usado no GET em findTrabalhos.

import xlrd
from collections import OrderedDict
import simplejson as json

null = None
false = False
true = True

wb = xlrd.open_workbook('Listagem de Avaliadores 33ª JAI.xlsx')
sh = wb.sheet_by_index(0)

trabalhos = []
# avaliador: row_values[0]
# dia: row_values[1]
# horário: row_values[3]
# prédio: row_values[5]
# sala: row_values[6]
# apresentador: row_values[8]
# orientador: row_values[9]
# módulo: row_values[10]
# título: row_values[11]
i = 1
j = 1
for rownum in range(1, sh.nrows):
    if (i != 565):
        perguntas = [
        {
            "discursiva":false,
            "id":0,
            "nome": "O título do trabalho reflete seu conteúdo e as palavras usadas são adequadas?",
            "resposta": "Sim;Não"
            },
        {
            "discursiva":false,
            "id":0,
            "nome": "O tema do trabalho é relevante na sua respectiva área do conhecimento?",
            "resposta": "Sim;Não"
            },
        {
            "discursiva":false,
            "id":0,
            "nome": "O título do trabalho reflete seu conteúdo e as palavras usadas são adequadas?",
            "resposta": "Sim;Não"
            },
        {
            "discursiva":false,
            "id":0,
            "nome": "A contextualização do trabalho com a literatura e/ou processos criativos existentes é feita de forma satisfatória?",
            "resposta": "Sim;Não"
            },
        {
            "discursiva":false,
            "id":0,
            "nome": " A metodologia empregada no trabalho reflete o atual estado da arte na sua respectiva área do conhecimento?",
            "resposta": "Sim;Não"
            },
        {
            "discursiva":false,
            "id":0,
            "nome": "Os resultados são apresentados de forma clara, estruturada e coerente, utilizando-se dos meios adequados (tabelas, gráficos etc)?",
            "resposta": "Sim;Não"
            },
        {
            "discursiva":false,
            "id":0,
            "nome": " A discussão dos resultados enfatizou seus aspectos mais relevantes e suas limitações?",
            "resposta": "Sim;Não"
            },
        {
            "discursiva":false,
            "id":0,
            "nome": "As conclusões do trabalho são coerentes com seus resultados, métodos e objetivos?",
            "resposta": "Sim;Não"
            },
        {
            "discursiva":false,
            "id":0,
            "nome": "O pôster ou os slides continham as informações necessárias de forma sintética e objetiva?",
            "resposta": "Sim;Não"
            },
        {
            "discursiva":false,
            "id":0,
            "nome": "O apresentador domina o conteúdo do trabalho apresentado?",
            "resposta": "Sim;Não"
            },
        {
            "discursiva":false,
            "id":0,
            "nome": "Qual nota o(a) Sr(a) daria para o trabalho/apresentador como um todo?",
            "resposta": "0;1;2;3;4;5"
            }
        ]


        trabalho = OrderedDict()
        trab = OrderedDict()
        apresentacao = OrderedDict()
        row_values = sh.row_values(rownum)

        data = ""
        if (row_values[1] == "22 de outubro"):
            data = "2018-10-22"
        elif (row_values[1] == "23 de outubro"):
            data = "2018-10-23"
        elif (row_values[1] == "24 de outubro"):
            data = "2018-10-25"
        elif (row_values[1] == "25 de outubro"):
            data = "2018-10-25"
        elif (row_values[1] == "26 de outubro"):
            data = "2018-10-26"

        data += "T" + row_values[3][:5] + ":00-03:00"

        apresentacao['data'] = data
        if (row_values[6] == ""):
            apresentacao['sala'] = str(row_values[7])
        else:
            apresentacao['sala'] = str(row_values[6])
        apresentacao['predio'] = row_values[5]
        trab['apresentacao'] = apresentacao
        trab['apresentador'] = row_values[8]
        trab['orientador'] = row_values[9]
        trab['id'] = i

        for pergunta in perguntas:
            pergunta['id'] = j
            j+=1

        trab['perguntas'] = perguntas
        trab['titulo'] = row_values[11]
        trabalho['trabalho'] = trab

        trabalhos.append(trabalho)
    i+=1


dados = {
    'id': null,
    'erro': false,
    'mensagem': "Sucesso",
    'trabalhos': [],
    'errorEntity': false
}

dados['trabalhos'] = trabalhos;

#arq = json.dumps(trabalhos, ensure_ascii=False, encoding='utf8', indent=4, separators=(',', ': '), sort_keys=True)
arq = json.dumps(dados, ensure_ascii=False, encoding='utf8', indent=4, separators=(',', ': '), sort_keys=True)

with open('data.json', 'w') as f:
    f.write(arq)

