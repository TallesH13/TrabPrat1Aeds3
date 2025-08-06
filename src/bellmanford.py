#entrada: grafo representado por lista de adjacencia, vértice origem e vertice destino ("v" minusculo)
def bellmanford(grafo, origem,destino):
    #dist guarda a menor distancia de v até a origem
    #prev guarda o vertice anterior a v no caminho mínimo
    dist = {}
    prev = {}
    V = grafo.numVertices
    #inicializa com dist infinito e prev nulo para o destino
    for v in range (V):
        dist[v] = float('inf')
        prev[v] = None
    #para a origem, a distancia dele até ele mesmo é 0 e o prev é ele mesmo
    dist[origem] = 0
    prev[origem] = origem
    #inicializa o conjunto V de todos os vértices do grafo
    #o loop principal é executado, no máximo, V-1 vezes
    k = 0
    for k in range(V-1):
        atualizou = False
        for u in range(V):
            for v, p in grafo.vizinhos(u):
                if dist[v] > dist[u] + p:
                    dist[v] = dist[u] + p
                    prev[v] = u
                    atualizou = True
        if atualizou == False:
            k = V
            break

#encontrando o caminho minimo ate o vertice de destino
    caminho = []
    atual = destino
    if dist[destino] == float('inf'):
        print("Nao ha caminho possivel... :(")
        return None
    
    #percorre a lista de predecessores começando do vertice destino,
    #removendo vertices da lista prev e montando a lista caminho, até chegar na origem
    #depois inverte a ordem da lista para a ordem correta
    while atual != origem:
        caminho.append(atual)
        atual = prev[atual]
        if atual is None:
            print("Erro! Vertice invalido!")
            return None

    caminho.append(origem)
    caminho.reverse()

    return caminho, dist[destino]
