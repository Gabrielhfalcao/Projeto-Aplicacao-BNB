import os
import random

pasta = '.' 
extensoes = ['csv'] 
randDisc = []

arquivos = os.listdir(pasta)
for i in arquivos:
	extensao = i.split('.')[-1]
	if extensao in extensoes:
		print(i)