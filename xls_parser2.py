# Script usado para gerar o JSON com os agrupadores-módulos-trabalhos,
# usado para o get em findTrabalhosModulo.
# obs.: o retorno do trabalho aqui é diferente do retorno usado no outro script,
# por conta disso fiz esse em separado.

import xlrd
from collections import OrderedDict
import simplejson as json

null = None
false = False
true = True

wb = xlrd.open_workbook('Listagem de Avaliadores 33ª JAI.xlsx')
sh = wb.sheet_by_index(0)

trabalhos = []
agrupadores = []
modulos = []
i = 1
j = 1
k = 1
l = 1
for rownum in range(1, sh.nrows):
    if (i != 565):
        trabalho = OrderedDict()
        trab = OrderedDict()
        apresentacao = OrderedDict()
        row_values = sh.row_values(rownum)

        agrupador = {
            "id": 0,
            "modulos": [
            ],
            "nome": ""
        }

        modulo = {
            "id": 0,
            "nome": "",
            "trabalhos": [],
        }

        if (row_values[10] != ""):
            agrup = row_values[10].split(' - ')
            nome_agrupador = agrup[0]
            nome_modulo = agrup[1]
            flag1 = True
            for ag in agrupadores:
                if ag['nome'] == nome_agrupador:
                    flag1 = False
                    break
            if flag1:
                agrupador['nome'] = nome_agrupador
                agrupador['id'] = k
                agrupadores.append(agrupador)
                k+=1

            flag2 = True
            for mod in modulos:
                if mod['nome'] == nome_modulo:
                    flag2 = False
                    break
            if flag2:
                modulo['nome'] = nome_modulo
                modulo['id'] = l
                modulos.append(modulo)
                for ag in agrupadores:
                    if ag['nome'] == nome_agrupador:
                        ag['modulos'].append(modulo)
                l+=1

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
        trab['id'] = i
        trab['apresentacao'] = apresentacao
        trab['apresentador'] = row_values[8]
        trab['orientador'] = row_values[9]
        trab['titulo'] = row_values[11]
        trab['agrupador'] = nome_agrupador
        trab['modulo'] = nome_modulo
        trabalho['trabalho'] = trab

        trabalhos.append(trabalho)
    i+=1

# para não adicionar os trabalho caso quiser só os módulos,
# comentar as linhas abaixo
for trab in trabalhos:
    for agrup in agrupadores:
        if trab['trabalho']['agrupador'] == agrup['nome']:
            for mod in agrup['modulos']:
                if trab['trabalho']['modulo'] == mod['nome']:
                    mod['trabalhos'].append(trab)

dados = {
    "id": null,
    "error": false,
    "codigo": 1001,
    "mensagem": "Sucesso",
    "agrupadores": [],
    "errorEntity": false
}

dados['agrupadores'] = agrupadores

#arq = json.dumps(agrupadores, ensure_ascii=False, encoding='utf8', indent=4, separators=(',', ': '), sort_keys=True)
arq = json.dumps(dados, ensure_ascii=False, encoding='utf8', indent=4, separators=(',', ': '), sort_keys=True)

with open('data2.json', 'w') as f:
    f.write(arq)
