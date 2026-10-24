from search import Problem, Graph

from collections import defaultdict
from pathlib import Path

# Practica 3
# Grupo: 2
# Nombres: Hernan Velarde Quiros, Trajano Arthur Iacob


class ProblemaGrafo(Problem):
    """Clase que define un problema de búsqueda en un grafo"""
    """
    nf_mapa: name file mapa
    nf_heuristica: name file heuristica
    mapa: dict de dict de distancias en el mapa
    grafo: grafo con los nodos y distancias del problema
    heuristica: dict de heuristicas
    """

    def __init__(self, inicial, goal, nf_mapa, nf_heuristica):
        super().__init__(inicial, goal)
        self.nf_mapa = nf_mapa
        self.nf_heuristica = nf_heuristica
        self.mapa = self.creaMapa()
        self.grafo = Graph(self.mapa, directed=False)
        self.heuristica = self.creaHeuristica()

    def creaMapa(self):
        """Función que lee el fichero de mapa y crea un
        diccionario con el mapa"""
        dists = defaultdict(dict)
        mapa = Path(self.nf_mapa)
        for line in mapa.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            origen, dest, distancia = line.split(" ")
            # No es necesario anadir dest -> origen porque el Grafo lo
            # puede interpretar como no dirigido y tenerlo en cuenta
            dists[origen][dest] = int(distancia)
        return dists

    def creaHeuristica(self):
        """Crea la heuristica, leyendo un fichero y la
        devuelve en un dicccionario"""
        heuristicas = dict()
        file = Path(self.nf_heuristica)
        for line in file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            lugar, heuris = line.split(" ")
            heuristicas[lugar] = int(heuris)
        return heuristicas

    def actions(self, A):
        """Devuelve la lista de los nodos a los que se puede llegar desde el nodo A"""
        return self.grafo.get(A)

    def result(self, state, action):
        """Devuelve el resultado de la acción"""
        # Implementacion de Node y sus metodos expand() y childNode()

        # def expand(self, problem):
        # """List the nodes reachable in one step from this node."""
        # return [self.child_node(problem, action)
        #         for action in problem.actions(self.state)]

        # def child_node(self, problem, action):
        # """[Figure 3.10]"""
        # next_state = problem.result(self.state, action)
        # next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        # return next_node

        """
        En la expansion de los nodos, se obtendran todas las acciones
        (siguientes nodos) correctos, y se creara un nodo hijo, este nodo hijo
        sera el resultado de aplicar result(), sabiendo que cada nodo solo
        contiene su localizacion entonces, si estamos en initial='Oviedo'
        y los siguientes disponibles son {'Leon', 'Lugo', 'Santander'}, aplicar
        la accion sera crear un nodo hijo 'Leon', por lo que se devuelve solo
        la accion en result()
        """
        return action

    def path_cost(self, coste_acumulado, A, action, B):
        """Devuelve el coste hasta el nodo B pasando por A"""
        return coste_acumulado + self.grafo.get(A, B)

    def h(self, node):
        """Devuelve la función heurística"""
        return self.heuristica.get(node)
