#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

import time
from optparse import OptionParser

def SelectionSort(array):
	for i in range(0,len(array)):
		i_min=i
		j=i+1
		while j < len(array):
			if array[j] < array[i_min]:
				i_min=j
			j=j+1
		if array[i] != array[i_min]:
			array[i],array[i_min] = array[i_min],array[i]
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
	print (SelectionSort(a))
	print ('Tempo gasto: ' + str(time.time() - inicio) + ' segundos')
else:
	argv.error("Passe o arquivo com instância")

