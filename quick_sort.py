#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

import time
from optparse import OptionParser


def Partition(array,p,fim):
	x = array[p]
	a = p+1
	b = fim
	while(True):
		while array[b]>x:
			b=b-1
		while array[a]<x and a <fim:
			a=a+1
		if a<b:
			array[a],array[b]=array[b],array[a]
			#print("loop")
		else:
			array[p],array[b]=array[b],array[p]
			return b

def QuickSort(array,inicio,fim):
	if inicio < fim:
		q= Partition(array,inicio,fim)
		QuickSort(array,inicio,q-1)
		QuickSort(array,q+1,fim)
	return array

argv = OptionParser()
argv.add_option("-i", "--instancias", action = "store", dest = "arquivo",default="",help = "Arquivo com valores para ordenar")
(options,args) = argv.parse_args()

if options.arquivo != "":
	a=[]
	try:
		arq=open(options.arquivo,'r')
		a=arq.readlines()
		arq.close()
	except:
		print('Erro ao ler o arquivo')

	inicio = time.time()
	#a=[3,5,62,6,7,4,3,7,5,8]
	print(a)
	print (QuickSort(a,0,int(len(a))-1))
	print ('Tempo gasto: ' + str(time.time() - inicio) + ' segundos')
else:
	argv.error("Passe o arquivo com instância")
