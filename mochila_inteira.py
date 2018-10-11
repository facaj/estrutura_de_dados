#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Aluno: Francisco de Assis

""" RESPOSTA
Valores: [100, 60, 70, 15, 15]
Pesos:[8, 3, 6, 4, 2]
G0(4) :130
Nao usa produto: X1
Usa produto: X2
Usa produto: X3
Nao usa produto: X4
Nao usa produto: X5
"""


arq=open("mochila02.txt.txt","r")
arquivo = arq.read().splitlines()
arq.close()




valores=[]
pesos=[]
mochila=int(arquivo[0].split(" ")[1])

tamanho = int(arquivo[0].split(" ")[0])
matriz = []
for i in range(mochila+1):
	matriz.append([0]*(tamanho+1))


for linha in arquivo[1:]:
	a,b = linha.split(" ")
	valores.append(int(b))
	pesos.append(int(a))

for i in range(mochila+1):
	matriz[i][tamanho] = [0,0]


#----------------------------

def max(i,tam_mochila):

	esq=matriz[tam_mochila][i+1][0]
	dir = matriz[tam_mochila -pesos[i]][i+1][0] + valores[i]

	if esq > dir:
		return [esq,0]
	else:
		return [dir,1]
for i in range(tamanho-1,-1,-1):
	for tam_mochila in range(mochila+1):
		if pesos[i] > tam_mochila:
			matriz[tam_mochila][i]=[matriz[tam_mochila][i+1][0],0]
		else:
			matriz[tam_mochila][i]=max(i,tam_mochila)

print "Valores: " + str(valores)
print "Pesos:" + str(pesos)
print "G0("+str(tamanho-1)+") :"+ str(matriz[mochila][0][0])

g=0
for i in range(tamanho):
	if matriz[mochila][g][1] == 1:
		print "Usa produto: X" +str(g+1)
		mochila=mochila - pesos[i]
		g=g+1
	else:
		print "Nao usa produto: X" +str(g+1)
		g=g+1
