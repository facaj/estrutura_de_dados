
import grafos
import kruskal
import prim

arq=open("dij10.txt","r")
doc= arq.read().splitlines()
arq.close()
tamanho = int(doc[0])

matriz=[]
for i in range(tamanho):
	matriz.append([0]*tamanho)
i=0

lista_encadeada={}
for linha in doc[1::]:
	j=i+1
	for coluna in linha.split(" "):
		if coluna != "":
			matriz[i][j]=coluna
			matriz[j][i]=coluna
		j=j+1
	i=i+1
k=0
for linha in matriz:
	vetor={}
	i=0
	for j in range(len(linha)):
		if linha[i] !=0:
			vetor[str(j)]=linha[i]
		i=i+1
	lista_encadeada[str(k)]=vetor
	k=k+1


for i,k in lista_encadeada.items():
	print i +"-"+str(k)
#print matriz

grafo=grafos.Grafo(lista_encadeada)

#kruskal = kruskal.Kruskal(grafo)
#valor=0
#print kruskal.arvore_minima()
#for i in  kruskal.arvore_minima():
#	valor = valor + int(i[0])
#print valor



prim = prim.Prim(grafo)
print prim.arvore_minima('0')


