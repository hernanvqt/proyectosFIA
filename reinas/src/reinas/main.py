from DomReina import DomReina
from collections import deque
from search import Node
import time


def imprime_estados(estados):
    for i, (accion, estado) in enumerate(estados.items()):
        print(f"Estado {i}, accion: {accion}: {estado}")


def genera_estados_siguientes(problema, estado_inicial, acciones):
    print("Estados siguientes generados despues de aplicar las acciones:")
    estados_siguientes = {}
    for a in acciones:
        estados_siguientes[a] = problema.result(estado_inicial, a)
    return estados_siguientes


def comprueba_objetivos(problema, estados):
    print("Comprobacion del objetivo: ")
    for (_, estado) in estados.items():
        print(f"El estado {estado}  es objetivo: {problema.goal_test(estado)}")

# N = 4
# problema = DomReina(N)
#
# acciones_posibles = problema.actions(problema.initial)
# estados_siguientes = genera_estados_siguientes(problema, problema.initial, acciones_posibles)
#
# imprime_estados(estados_siguientes)
# comprueba_objetivos(problema, estados_siguientes)


def breadth_first_tree_search(problem):
    frontier = deque([Node(problem.initial)])

    while frontier:
        node = frontier.popleft()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None


def imprimir_sol(nodo, algoritmo, size, coste, n_minimo):
    print(f"Algoritmo: {algoritmo}")
    print(f"Tablero: {size}x{size}")
    print(f"Coste de tiempo: {coste}")
    print(f"Numero minimo de reinas: {n_minimo}")
    imprimir_tabla_solucion(nodo)


def imprimir_tabla_solucion(nodo):
    print(f"{'Reinas':<8} | {'Fila':>4} | {'Col':>4} |")
    for fila, col in enumerate(nodo.state):
        print(f"{'Reina ' + str(fila + 1):<8} | {fila:>4} | {col:>4} |")


problema = DomReina(4)

inicio = time.time()
sol = breadth_first_tree_search(problema)
fin = time.time()
tiempo_total = fin - inicio

imprimir_sol(sol, "BDF", len(problema.initial), tiempo_total, 4)
