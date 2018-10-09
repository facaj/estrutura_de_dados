
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

class Djisktra():
	def __init__(self,grafo):
		self.grafo=grafo.grafo
		self.pai={}
		self.menor_distancia={}
		self.infinito=sorted(grafo.arestas())[-1][0] + 1
		for v in self.grafo:
			self.menor_distancia[v] = self.infinito
	def caminho_minimo(self,v):
		self.menor_distancia[v]=0
		while len(self.grafo)>0:
			melhor_caminho = None
			for v in self.grafo:
				if melhor_caminho is None:
					melhor_caminho = v
				elif self.menor_distancia[v] < self.menor_distancia[melhor_caminho]:
					melhor_caminho = v
			for vertice,distancia in self.grafo[melhor_caminho].items():
				if int(distancia) + int(self.menor_distancia[melhor_caminho]) < int(self.menor_distancia[vertice]):
					self.menor_distancia[vertice] =  int(distancia) + int(self.menor_distancia[melhor_caminho])
					self.pai[vertice] = [melhor_caminho,self.menor_distancia[vertice]]
			self.grafo.pop(melhor_caminho)

		return self.pai
