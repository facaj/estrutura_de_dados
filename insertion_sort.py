#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

import time
from optparse import OptionParser


def InsertionSort(array):
	for i in range(1,len(array)):
		pivo=array[i]
		j=i-1
		while j>=0 and array[j] > pivo:
			array[j+1]=array[j]
			j=j-1
		array[j+1]=pivo
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
	print (InsertionSort(a))
	print ('Tempo gasto: ' + str(time.time() - inicio) + ' segundos')
else:
	argv.error("Passe o arquivo com instância")
