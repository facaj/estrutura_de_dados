#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

import time
from optparse import OptionParser


def CountingSort(array):
	#Descobre o maior valor do array
	maior=array[0]
	for valor in array:
		if valor > maior:
			maior=valor
	#Criando um array do tamanho do maior valor
	CountArray=[]
	for i in range(0,maior+1):
		CountArray.append(0)
	#Contagem
	for valor in array:
		CountArray[valor]= CountArray[valor]+1
	#print CountArray
	#Ordenando
	k=0
	for indice in range(0,maior+1):
		if CountArray[indice]>0:
			for a in range(CountArray[indice]):
				array[k]=indice
				k=k+1
	return array
argv = OptionParser()
argv.add_option("-i", "--instancias", action = "store", dest = "arquivo",default="",help = "Arquivo com valores para ordenar")
(options,args) = argv.parse_args()

if options.arquivo != "":
	a=[]
	try:
		arq=open(options.arquivo,'r')
		a=arq.read().splitlines()
		arq.close()
	except:
		print('Erro ao ler o arquivo')

	inicio = time.time()
	#a=[3,5,62,6,7,4,3,7,5,8]
	print(a)
	print (CountingSort(a))
	print ('Tempo gasto: ' + str(time.time() - inicio) + ' segundos')
else:
	argv.error("Passe o arquivo com instância")
