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

    #bellmanford(arquivo, origem, destino)

    #caminho = "toy.txt"  # Altera conforme arquivo que será testado
    grafo = ler_grafo(arquivo)
    grafo.printGrafo()

    caminho, custo = dijkstra(grafo, 0, 4)
    print("\nO caminho foi:\n")
    print(caminho)
    print("\nO custo foi:\n")
    print(custo)