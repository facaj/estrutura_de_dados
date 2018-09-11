#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

import time
from optparse import OptionParser


def RadixSort(array):
	#Descobre o maior valor do array
        maior=array[0]
        for valor in array:
                if valor > maior:
                        maior=valor
	#Descobre quantos digitos tem o maior número
	quantidade = len(str(maior))
	modulo = 10
	div = 1
	for k in range(quantidade):
		p=0

		temp = [[],[],[],[],[],[],[],[],[],[]]
		for valor in array:
			ultimo_digito = (valor % modulo) // div
			temp[ultimo_digito].append(valor)
		modulo = modulo * 10
		div = div * 10
		for vetor in temp:
			for i in vetor:
				if p<len(array):
					array[p] = i
					p=p+1
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
	print(a)
	print (RadixSort(a))
	print ('Tempo gasto: ' + str(time.time() - inicio) + ' segundos')
else:
	argv.error("Passe o arquivo com instância")
