#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

import time
from optparse import OptionParser


def Merge(array):
	meio=int(len(array)/2)
	i=0
	j=int(len(array[meio:]))
	NovoArray=[]
	while i < meio and j < int(len(array)):
		print("\ni->"+str(array[i])+"\nj->"+str(array[j]))
		if array[i] <= array[j]:
			NovoArray.append(array[i])
			i=i+1
		else:
			NovoArray.append(array[j])
			j=j+1
		print(NovoArray)
	while i < meio:
		NovoArray.append(array[i])
		i=i+1
	while j < int(len(array)):
		NovoArray.append(array[j])
		j=j+1
	#print (NovoArray)
	#return NovoArray
	return NovoArray

def MergeSort(array):
	if len(array)>1:
		meio = int(len(array)/2)
		MergeSort(array[:meio])
		MergeSort(array[meio:])
		array=Merge(array)
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
	a=[3,5,62,6,7,4,3,7,5,8]
	print(a)
	print (MergeSort(a))
	print ('Tempo gasto: ' + str(time.time() - inicio) + ' segundos')
else:
	argv.error("Passe o arquivo com instância")
