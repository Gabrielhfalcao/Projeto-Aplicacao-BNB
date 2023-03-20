import csv
import os
import random
import pandas as pd

pasta = '.' 
extensoes = ['csv'] 
arq = []
listaParaSelecionar = []
escolhas = []

arquivos = os.listdir(pasta)
for i in arquivos:
	extensao = i.split('.')[-1]
	if extensao in extensoes:
		x = i.split('.')[0]
		listaParaSelecionar.append(x)
		arq.append(i)

while len(escolhas) < 10:
    escolha = random.choice(listaParaSelecionar)
    if not any([s.endswith(escolha[-3:]) for s in escolhas]):
        escolhas.append(escolha)

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


with open(str(escolhas[0] + ".csv")) as arquivocsv:
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

povoarVariaveis(str(escolhas[1])+ ".csv", dados2, data2, datasSelecionadas, datasNaoRepetidadas2)                
registroNaoRepetido2 = int(data2.index(datasNaoRepetidadas2[0]))
datasSelecionadas.append(datasNaoRepetidadas2[0])

povoarVariaveis(str(escolhas[2])+ ".csv", dados3, data3, datasSelecionadas, datasNaoRepetidadas3)
registroNaoRepetido3 = int(data3.index(datasNaoRepetidadas3[0]))
datasSelecionadas.append(datasNaoRepetidadas3[0])

povoarVariaveis(str(escolhas[3])+ ".csv", dados4, data4, datasSelecionadas, datasNaoRepetidadas4)
registroNaoRepetido4 = int(data4.index(datasNaoRepetidadas4[0]))
datasSelecionadas.append(datasNaoRepetidadas4[0])

povoarVariaveis(str(escolhas[4])+ ".csv", dados5, data5, datasSelecionadas, datasNaoRepetidadas5)
registroNaoRepetido5 = int(data5.index(datasNaoRepetidadas5[0]))
datasSelecionadas.append(datasNaoRepetidadas5[0])

povoarVariaveis(str(escolhas[5])+ ".csv", dados6, data6, datasSelecionadas, datasNaoRepetidadas6)
registroNaoRepetido6 = int(data6.index(datasNaoRepetidadas6[0]))
datasSelecionadas.append(datasNaoRepetidadas6[0])

povoarVariaveis(str(escolhas[6])+ ".csv", dados7, data7, datasSelecionadas, datasNaoRepetidadas7)
registroNaoRepetido7 = int(data7.index(datasNaoRepetidadas7[0]))
datasSelecionadas.append(datasNaoRepetidadas7[0])

povoarVariaveis(str(escolhas[7])+ ".csv", dados8, data8, datasSelecionadas, datasNaoRepetidadas8)
registroNaoRepetido8 = int(data8.index(datasNaoRepetidadas8[0]))
datasSelecionadas.append(datasNaoRepetidadas8[0])

povoarVariaveis(str(escolhas[8])+ ".csv", dados9, data9, datasSelecionadas, datasNaoRepetidadas9)
registroNaoRepetido9 = int(data9.index(datasNaoRepetidadas9[0]))
datasSelecionadas.append(datasNaoRepetidadas9[0])

povoarVariaveis(str(escolhas[9])+ ".csv", dados10, data10, datasSelecionadas, datasNaoRepetidadas10)
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

df = pd.DataFrame(listaFinal)
df.to_excel('registros.xlsx', index=False)


df = pd.DataFrame(listaFinal)

writer = pd.ExcelWriter('C:/Users/gabri/OneDrive/Documentos/a/RegistrosGerados/registrosAleatorios.xlsx', engine='openpyxl')
df.to_excel(writer, sheet_name='Dados', index=False)
worksheet = writer.sheets['Dados']

for col in worksheet.columns:
    max_length = 0
    column = col[0].column_letter
    
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
        
    adjusted_width = (max_length + 2)
    worksheet.column_dimensions[column].width = adjusted_width

writer.save()











import pandas as pd
import statistics
import sys
import os

listaDeDados = []

os.system('cls')
def povoarLista(lista):
    os.system('cls')
    x = int(input("Digite o tamanho da lista de dados a ser analisáda: "))
    print("")

    indice = 0
    while (indice < x):
        lista.append(int(input("Digite o " + str(indice + 1) + "º elemento: "))) 
        indice += 1

    listaDeDados.sort()
    os.system('cls')
    menuPrincipal()

def menuPrincipal():
    os.system('cls')  
    print()
    print("---------Menu Principal---------")
    print("Lista de dados: " + str(listaDeDados))
    print("Digite o número relativo a operação que deseja realizar: ")
    print("1 --> Média Aritmética")
    print("2 --> Média Ponderada")
    print("3 --> Moda")
    print("4 --> Mediana")
    print("5 --> Digitar lista de dados novamente")
    print("6 --> Sair do Programa")

    x = int(input())
    if x == 1:
        print()
        print("Lista de dados: " + str(listaDeDados)) 
        print("A Média Aritmética da lista de dados é: " + str(mediaAritmetica(listaDeDados)))
        opcaoVoltarAoMenuOuSair()
    
    elif x == 2:
        print()
        print("Lista de dados: " + str(listaDeDados)) 
        print("A Média Ponderada da lista de dados é: " + str(mediaPoderada(listaDeDados)))
        opcaoVoltarAoMenuOuSair()

    elif x == 3:
        print()
        print("A Moda da lista de dados é: " + str(moda(listaDeDados)))
        print()
        opcaoVoltarAoMenuOuSair()

    elif x == 4: 
        print()
        print("A Mediana da lista de dados é: " + str(mediana(listaDeDados)))
        print()
        opcaoVoltarAoMenuOuSair()

    elif x == 5:
        listaDeDados.clear()
        print()
        povoarLista(listaDeDados)
    elif x == 6:
        sairDoPrograma()
    else:
        print()
        ("Digite uma opção válida!")
        menuPrincipal()

def mediaAritmetica(lista):
    os.system('cls')
    print("Lista de dados: " + str(listaDeDados)) 
    return statistics.mean(lista)  

def moda(lista):
    os.system('cls')
    print("Lista de dados: " + str(listaDeDados)) 
    x = statistics.multimode(lista)
    if len(x) == len(lista):
        return("A lista não possui moda")
    elif len(x) == 1:
        return(str(statistics.multimode(lista)) + " (MODAL)")
    elif len(x) == 2:
        return(str(statistics.multimode(lista)) + " (BIMODAL)")        
    elif len(x) == 3:
        return(str(statistics.multimode(lista)) + " (TRIMODAL)")
    else:
        return(str(statistics.multimode(lista)) + " (MULTIMODAL)")

def mediaPoderada(lista):
    os.system('cls')
    print("Lista de dados: " + str(listaDeDados)) 
    indice = 0
    somaNumerador = 0
    somaDenominador = 0
    while (indice < len(lista)):
        x = int(input("Digite o peso referente ao " + str(indice + 1) + ("º dado: ")))
        somaNumerador += lista[indice] * x
        somaDenominador += x 
        indice += 1
    return (somaNumerador/somaDenominador)    

def mediana(lista):
    os.system('cls')
    print("Lista de dados: " + str(listaDeDados)) 
    return statistics.median(lista)

def opcaoVoltarAoMenuOuSair():
    x = int(input("-----Para sair do Programa digite [0] ou para voltar ao menu digite [1]----"))
    if x == 0:
        sairDoPrograma()
    elif x == 1:
        menuPrincipal()
    else:
        ("Digite uma opção válida:")
        opcaoVoltarAoMenuOuSair()    

def sairDoPrograma():    
    sys.exit()

povoarLista(listaDeDados)



var pecas_tabuleiro = [
    [4, 3, 2, 5, 6, 2, 3, 4],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [4, 3, 2, 5, 6, 2, 3, 4]
]    

function contarTorres(){
    var totalTorres = 0;
    var indice = 0;
    while(indice < pecas_tabuleiro.length){
        var listaTorres = pecas_tabuleiro[indice].filter(torres => torres == 4)
        totalTorres += listaTorres.length
        indice++
    }
    console.log(totalTorres)
}
contarTorres()



var pecas_tabuleiro = [
    [4, 3, 2, 5, 6, 2, 3, 4],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [4, 3, 2, 5, 6, 2, 3, 4]
]    

function contarPecas(numeroPeca){
    var totalPecas = 0;
    var indice = 0;
    while(indice < pecas_tabuleiro.length){
        var listaPeca = pecas_tabuleiro[indice].filter(peca => peca == numeroPeca)
        totalPecas += listaPeca.length
        indice++
    }
    return totalPecas
}

console.log(contarPecas(4))
