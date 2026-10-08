from DomReina import DomReina
from collections import deque
from search import Node, PriorityQueue, memoize
import sys
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


def depth_first_tree_search(problem):
    """
    [Figure 3.7]
    Search the deepest nodes in the search tree first.
    Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Repeats infinitely in case of loops.
    """

    frontier = [Node(problem.initial)]  # Stack

    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        frontier.extend(node.expand(problem))
    return None


def best_first_graph_search(problem, f, display=False):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None


def uniform_cost_search(problem, display=False):
    """[Figure 3.14]"""
    return best_first_graph_search(problem, lambda node: node.path_cost, display)


def depth_limited_search(problem, limit=50):
    """[Figure 3.17]"""

    def recursive_dls(node, problem, limit):
        if problem.goal_test(node.state):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for child in node.expand(problem):
                result = recursive_dls(child, problem, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    # Body of depth_limited_search:
    return recursive_dls(Node(problem.initial), problem, limit)


def iterative_deepening_search(problem):
    """[Figure 3.18]"""
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result


def imprimir_sol(nodo, algoritmo, size, coste, n_minimo):
    print(f"Algoritmo: {algoritmo}")
    print(f"Tablero: {size}x{size}")
    print(f"Coste de tiempo: {coste}")
    print(f"Numero minimo de reinas: {n_minimo}")
    imprimir_tabla_solucion(nodo)
    print()


def imprimir_tabla_solucion(nodo):
    print(f"{'Reinas':<8} | {'Fila':>4} | {'Col':>4} |")
    for i, (fila, col) in enumerate(nodo.state[0]):
        print(f"{'Reina ' + str(i + 1):<8} | {fila:>4} | {col:>4} |")


N = 4
problema = DomReina(N)

inicio = time.time()
sol = breadth_first_tree_search(problema)
fin = time.time()
tiempo_total = fin - inicio
imprimir_sol(sol, "BPA", problema.N, tiempo_total, len(sol.state[0]))

inicio = time.time()
sol = depth_first_tree_search(problema)
fin = time.time()
tiempo_total = fin - inicio
imprimir_sol(sol, "BPP", problema.N, tiempo_total, len(sol.state[0]))

inicio = time.time()
sol = uniform_cost_search(problema)
fin = time.time()
tiempo_total = fin - inicio
imprimir_sol(sol, "BCU", problema.N, tiempo_total, len(sol.state[0]))

inicio = time.time()
sol = depth_limited_search(problema)
fin = time.time()
tiempo_total = fin - inicio
imprimir_sol(sol, "BPL", problema.N, tiempo_total, len(sol.state[0]))

inicio = time.time()
sol = iterative_deepening_search(problema)
fin = time.time()
tiempo_total = fin - inicio
imprimir_sol(sol, "BPI", problema.N, tiempo_total, len(sol.state[0]))
