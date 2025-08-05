#entrada: grafo representado por lista de adjacencia, vértice origem e vertice destino ("v" minusculo)
def bellmanford(grafo, origem):
    #dist guarda a menor distancia de v até a origem
    #prev guarda o vertice anterior a v no caminho mínimo
    dist = {}
    prev = {}
    #inicializa com dist infinito e prev nulo para o destino
    for v in grafo:
        dist[v] = float('inf')
        prev[v] = None
    #para a origem, a distancia dele até ele mesmo é 0 e o prev é ele mesmo
    dist[origem] = 0
    prev[origem] = origem
    #inicializa o conjunto V de todos os vértices do grafo
    V = len(grafo)
    #o loop principal é executado, no máximo, V-1 vezes
    k = 0
    for k in range(V-1):
        atualizou = False
        for u in grafo:
            for v, p in grafo[u]:
                if dist[v] > dist[u] + p:
                    dist[v] = dist[u] + p
                    prev[v] = u
                    atualizou = True
        if atualizou == False:
            k = V

