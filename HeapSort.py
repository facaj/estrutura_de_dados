#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

import time
from optparse import OptionParser

def heapify(array,tamanho,i_root):
	maior = i_root
	filho_esquerda = 2*i_root+1
	filho_direita = 2*i_root+2
	
	if filho_esquerda < tamanho and array[maior] < array[filho_esquerda]:
		maior = filho_esquerda
	if filho_direita < tamanho and array[maior] < array[filho_direita]:
		maior = filho_direita
	if maior != i_root:
		array[i_root],array[maior] = array[maior],array[i_root]
		heapify(array,tamanho,maior)

def heapSort(array):
	tamanho=len(array)
	for i in range(tamanho,-1,-1):
		heapify(array,tamanho,i)
	for i in range(tamanho-1,0,-1):
		array[i],array[0] = array[0],array[i] #swap
		heapify(array,i,0)
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
	#a=[3,5,26,1,6,12,5,1]
	print (heapSort(a))
	print ('Tempo gasto: ' + str(time.time() - inicio) + ' segundos')
else:
	argv.error("Passe o arquivo com instância")