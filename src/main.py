from listaAdjacencias import ListaAdjacencias
from listaAdjacencias import ler_grafo
from dijkstra import dijkstra
import sys
from bellmanford import bellmanford

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Por favor, insira os argumentos no modo: grafo origem destino")
        sys.exit(1)
    arquivo = sys.argv[1]
    origem = int(sys.argv[2])
    destino = int(sys.argv[3])

    grafo = ler_grafo(arquivo)
    #ATENÇÃO. COMENTAR ESTA LINHA AO EXECUTAR OS GRAFOS MAIORES
    grafo.printGrafo() #COMENTE ESTA LINHA !!!!!!!!!!!!!!!

    print("Processando...")
    print("-------------------------------------------------------------")
    caminho_dij, custo_dij = dijkstra(grafo, origem, destino)
    print("Algoritmo de Dijkstra:")
    print("Caminho minimo:", caminho_dij)
    print("Custo:", custo_dij)
    #add print tempo e memoria aqui!
    print("-------------------------------------------------------------")
    caminho_bell, custo_bell = bellmanford(grafo, origem, destino)
    print("Algoritmo Bellman-Ford:")
    print("Caminho minimo:", caminho_bell)
    print("Custo:", custo_bell)
    #add print tempo e memoria aqui!
    print("-------------------------------------------------------------")