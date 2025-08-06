from listaAdjacencias import ListaAdjacencias
from listaAdjacencias import ler_grafo
from dijkstra import dijkstra

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Por favor, insira os argumentos no modo: grafo origem destino")
        print("lembre de especificar o caminho do grafo, caso nao esteja na pasta principal")
        sys.exit(1)
    arquivo = sys.argv[1]
    origem = int(sys.argv[2])
    destino = int(sys.arg[3])
    
    grafo = ler_grafo(arquivo)
    grafo.printGrafo()

    caminho, custo = dijkstra(grafo, origem, destino)
    print("\nO caminho foi:\n")
    print(caminho)
    print("\nO custo foi:\n")
    print(custo)
