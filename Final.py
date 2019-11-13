#Teoria dos Grafos
#Caminho Mínimo (Dijkstra)
# 01/10/2019
from collections import deque, namedtuple
import time

inf = float('inf')#cria um número infinito
Aresta = namedtuple('Aresta', 'incio, fim, valor')

def aresta(incio, fim, valor=1):
  return Aresta(incio, fim, valor)


class Grafo:
    def __init__(self, arestas):
        self.arestas = [Aresta(*aresta) for aresta in arestas]

    @property #usado para orientação à objeto
    def vertices(self):
        return set(sum(([aresta.incio, aresta.fim] for aresta in self.arestas), []))#set == @property

    def add_vertices_pares(self, a, b, finais=True):
        if finais:
            vertices_pares = [[a, b], [b, a]]
        else:
            vertices_pares = [[a, b]]
        return vertices_pares

    def remove_aresta(self, a, b, both_ends=True):
        vertices_pares = self.add_vertices_pares(a, b, both_ends)
        arestas = self.arestas[:]
        for aresta in arestas:
            if [aresta.incio, aresta.fim] in vertices_pares:
                self.arestas.remove(aresta)

    @property
    def vizinhos(self):
        vizinhos = {vertice: set() for vertice in self.vertices}#set == @property
        for aresta in self.arestas:
            vizinhos[aresta.incio].add((aresta.fim, aresta.valor))
        return vizinhos

    def dijkstra(self, inicial, final):
        assert inicial in self.vertices, 'Vertíce Inicial não Existe!'
        distances = {vertice: inf for vertice in self.vertices}
        vertice_anterior = {
            vertice: None for vertice in self.vertices
        }
        distances[inicial] = 0
        vertices = self.vertices.copy()

        while vertices:
            vertice_visitado = min(
                vertices, key=lambda vertice: distances[vertice])
            vertices.remove(vertice_visitado)
            for vizinho, valor in self.vizinhos[vertice_visitado]:
                outro_caminho = distances[vertice_visitado] + int(valor)
                if outro_caminho < distances[vizinho]:
                    distances[vizinho] = outro_caminho
                    vertice_anterior[vizinho] = vertice_visitado

        caminho, vertice_visitado = deque(), final
        while vertice_anterior[vertice_visitado] is not None:
            caminho.appendleft(vertice_visitado)
            vertice_visitado = vertice_anterior[vertice_visitado]
        if caminho:
            caminho.appendleft(vertice_visitado)
        return caminho

#####################################################################
#Exemplos de Utilização
f = open(r"C:\Users\Daniella\Downloads\entrada.txt","r")
len = len(f.readlines())
f.close()
f = open(r"C:\Users\Daniella\Downloads\entrada.txt","r")
aux = []
for i in range(len):
    aux.append(tuple((f.readline().strip()).split(" ")))

graph = Grafo(aux)

print("Caminho Mínimo (graph):", graph.dijkstra("s", "y"))


#####################################################################
