import csv

dados1 = []

dados2 = []
data2 = []
datasNaoRepetidadas2 = []

dados3 = []
data3 = []
datasNaoRepetidadas3 = []

dados4 = []
data4 = []
datasNaoRepetidadas4 = []

dados5 = []
data5 = []
datasNaoRepetidadas5 = []

dados6 = []
data6 = []
datasNaoRepetidadas6 = []

dados7 = []
data7 = []
datasNaoRepetidadas7 = []

dados8 = []
data8 = []
datasNaoRepetidadas8 = []

dados9 = []
data9 = []
datasNaoRepetidadas9 = []

dados10 = []
data10 = []
datasNaoRepetidadas10 = []

datasSelecionadas = []

listafinal = []


with open("autoverificacao769.csv") as arquivocsv:
    ler = csv.DictReader(arquivocsv, delimiter="\t")
    for linha in ler:
        dados1.append(linha)

x = str((dados1[0].items()))
y = int(x.find('DT_LNC'))
z = x[y+10:y+20]
datasSelecionadas.append(z)

def povoarVariaveis(arquivo, listaDeDados, dataDoRegistro, datasSelecionadas, datasNaoRepetidadas):
    with open(arquivo) as arquivocsv:
        ler = csv.DictReader(arquivocsv, delimiter="\t")
        for linha in ler:
            x = str((linha.items()))
            y = int(x.find('DT_LNC'))
            z = x[y+10:y+20]
            listaDeDados.append(linha)
            dataDoRegistro.append(z)
            if z not in datasSelecionadas:
                datasNaoRepetidadas.append(z)

povoarVariaveis("autoverificacao770.csv", dados2, data2, datasSelecionadas, datasNaoRepetidadas2)                
registroNaoRepetido2 = int(data2.index(datasNaoRepetidadas2[0]))
datasSelecionadas.append(datasNaoRepetidadas2[0])

povoarVariaveis("autoverificacao771.csv", dados3, data3, datasSelecionadas, datasNaoRepetidadas3)
registroNaoRepetido3 = int(data3.index(datasNaoRepetidadas3[0]))
datasSelecionadas.append(datasNaoRepetidadas3[0])

povoarVariaveis("autoverificacao772.csv", dados4, data4, datasSelecionadas, datasNaoRepetidadas4)
registroNaoRepetido4 = int(data4.index(datasNaoRepetidadas4[0]))
datasSelecionadas.append(datasNaoRepetidadas4[0])

povoarVariaveis("autoverificacao773.csv", dados5, data5, datasSelecionadas, datasNaoRepetidadas5)
registroNaoRepetido5 = int(data5.index(datasNaoRepetidadas5[0]))
datasSelecionadas.append(datasNaoRepetidadas5[0])

povoarVariaveis("autoverificacao774.csv", dados6, data6, datasSelecionadas, datasNaoRepetidadas6)
registroNaoRepetido6 = int(data6.index(datasNaoRepetidadas6[0]))
datasSelecionadas.append(datasNaoRepetidadas6[0])

povoarVariaveis("autoverificacao775.csv", dados7, data7, datasSelecionadas, datasNaoRepetidadas7)
registroNaoRepetido7 = int(data7.index(datasNaoRepetidadas7[0]))
datasSelecionadas.append(datasNaoRepetidadas7[0])

povoarVariaveis("autoverificacao776.csv", dados8, data8, datasSelecionadas, datasNaoRepetidadas8)
registroNaoRepetido8 = int(data8.index(datasNaoRepetidadas8[0]))
datasSelecionadas.append(datasNaoRepetidadas8[0])

povoarVariaveis("autoverificacao777.csv", dados9, data9, datasSelecionadas, datasNaoRepetidadas9)
registroNaoRepetido9 = int(data9.index(datasNaoRepetidadas9[0]))
datasSelecionadas.append(datasNaoRepetidadas9[0])

povoarVariaveis("autoverificacao778.csv", dados10, data10, datasSelecionadas, datasNaoRepetidadas10)
registroNaoRepetido10 = int(data10.index(datasNaoRepetidadas10[0]))
datasSelecionadas.append(datasNaoRepetidadas10[0])


listafinal.append(dados1[1])
listafinal.append(dados2[registroNaoRepetido2])
listafinal.append(dados3[registroNaoRepetido3])
listafinal.append(dados4[registroNaoRepetido4])
listafinal.append(dados5[registroNaoRepetido5])
listafinal.append(dados6[registroNaoRepetido6])
listafinal.append(dados7[registroNaoRepetido7])
listafinal.append(dados8[registroNaoRepetido8])
listafinal.append(dados9[registroNaoRepetido9])
listafinal.append(dados10[registroNaoRepetido10])

print(listafinal)