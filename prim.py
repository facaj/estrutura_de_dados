
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

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
	for i in range(tamanho):
		heapify(array,tamanho,i)
	for i in range(tamanho-1,0,-1):
		array[i],array[0] = array[0],array[i] #swap
		heapify(array,i,0)
	return array


class Prim():
	"""
MST-PRIM (G, w, r) {

        for each key E G.V

            u.key = infinito
            u.parent = NIL

        r.key = 0
        Q = G.V
        while (Q != 0)

            u = Extract-Min(Q)
            for each v E G.Adj[u]

                if (v E Q) and w(u,v) < v.key

                    v.parent = u
                    v.key = w(u,v)    <== relax function, Pay attention here

}
	"""

	def __init__(self,grafo):
		self.grafo=grafo
		self.pai={}
		self.valores_vertices=[]
		self.infinito=sorted(self.grafo.arestas())[-1][0] + 1
		for v in self.grafo.vertices():
			self.valores_vertices.append([self.infinito,v])
	def get_valor_vertice(self,v):
		for i in self.valores_vertices:
			if i[1] == v:
				return i[0]

	def set_valor_vertice(self,v,valor):
		for i in  self.valores_vertices:
                        if i[1] ==v:
                                i[0]=valor
                                return

	def arvore_minima(self,v):
		self.set_valor_vertice(v,0)
		fila =  heapSort(self.valores_vertices)
		while len(fila)>0:
			v1=fila.pop(0)
			for v2 in self.grafo.grafo[v1[1]].keys():
				na_fila=False
				for i in fila:
					if v2 == i[1]:
						na_fila=True
				if na_fila and int(self.grafo.matriz[int(v1[1])][int(v2)]) < int(self.get_valor_vertice(v2)):
						self.pai[v2]=[v1[1],int(self.grafo.matriz[int(v1[1])][int(v2)])]
						self.set_valor_vertice(v2,int(self.grafo.matriz[int(v1[1])][int(v2)]))
			heapSort(fila)
		return self.pai
