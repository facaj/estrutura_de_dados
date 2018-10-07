
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

class Kruskal():
	def __init__(self,grafo):
		self.grafo=grafo
		self.pai={}
		self.rank={}
		self.arvore=[]
	def arvore_minima(self):
		ordenado=sorted(self.grafo.arestas())
		for v in self.grafo.vertices():
			self.make_set(v)
		for aresta in ordenado:
			if self.find_set(aresta[1]) != self.find_set(aresta[2]):
				self.arvore.append(aresta)
				self.union(aresta[1],aresta[2])
		return self.arvore
	def make_set(self,v):
		self.pai[v]= v
		self.rank[v]=0

	def find_set(self,v):
		if self.pai[v] != v:
			self.pai[v] = self.find_set(self.pai[v])
		return self.pai[v]

	def union(self,v1,v2):
		r1=self.find_set(v1)
		r2=self.find_set(v2)
		if r1 != r2:
			if self.rank[r1] > self.rank[r2]:
				self.pai[r2] = r1
			else:
				self.pai[r1] = r2
		if self.rank[r1] == self.rank[r2]:
			self.rank[r2] = self.rank[r2]+1
