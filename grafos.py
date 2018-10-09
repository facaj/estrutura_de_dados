#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

class Grafo():
	def __init__(self,grafo):
		self.grafo = grafo
		self.tamanho = len(grafo)
		self.cria_matriz()

	def cria_matriz(self):
		self.matriz=[]
		self.nome2indice={}
		indice=0
		for key in self.grafo.keys():
			self.nome2indice[key]=indice
			indice=indice+1
		for i in range(self.tamanho):
			self.matriz.append([0]*self.tamanho)
		for key in self.grafo.keys():
			for visinho,peso in self.grafo[key].items():
				self.matriz[self.nome2indice[key]][self.nome2indice[visinho]]=peso

	def cria_grafo(self):
		k=0
		for linha in matriz:
		       	vetor=[]
	       		i=0
	        	for j in range(len(linha)):
		                if linha[i] !=0:
	               	        	vetor.append([str(j),linha[i]])
		               	i=i+1
		       	lista_encadeada[str(k)]=vetor
		        k=k+1
		return lista_encadeada


	def grafo_lista(self):
		return self.grafo

	def vertices(self):
		return self.grafo.keys()

	def arestas(self):
		arestas=[]
		for key in self.grafo.keys():
			for vizinho,valor in self.grafo[key].items():
				arestas.append((int(valor),key,vizinho))
		return arestas

	def busca_largura(self,no_inicio):
		visitados=[]
		no = no_inicio
		tam = self.tamanho
		while tam>0 :
			tam = tam -1
			for vizinho in self.grafo[no]:
				if vizinho[0] not in visitados:
					visitados.append(vizinho[0])
					no = vizinho[0]
		return visitados

	def busca_profundidade(self,no_inicio):
		self.visitados=[no_inicio]
		self.realiza_busca_profundidade(no_inicio)
		return self.visitados

	def realiza_busca_profundidade(self,no):
		for vizinho in self.grafo[no]:
			if vizinho[0] not in self.visitados:
				self.visitados.append(vizinho[0])
				self.realiza_busca_profundidade(vizinho[0])
	def ordena_pelo_peso(self):
		return sorted(self.arestas())


