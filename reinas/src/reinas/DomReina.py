from search import Problem


class DomReina(Problem):
    """
     Colocar el mínimo número de reinas en un tablero NxN, de forma
     que cada casilla sea ocupada o atacada por al menos una reina.
     Guardamos la posicion de las reinas colocadas, y para la
     cobertura de estas reinas utilizamos 4 sets para la cobertura
     de la dominacion y asi hacer una busqueda rapida de si esta contenido.
     1. tupla posiciones ocupadas de reinas
     2. conjunto inmutable de cobertura de filas
     3. conjunto inmutable de cobertura de columnas
     4. conjunto inmutable de cobertura de diagonal ascendente
     5. conjunto inmutable de cobertura de diagonal descendente
    """

    def __init__(self, N):
        super().__init__(
            tuple((tuple(), frozenset(), frozenset(), frozenset(), frozenset())))
        self.N = N

    def actions(self, state):
        """
        Una accion sera una casilla que no contiene una reina
        """
        reinas = state[0]
        return [(f, c) for f in range(self.N) for c in range(self.N)
                if (f, c) not in reinas]

    def result(self, state, action):
        """
        Al aplicar una accion, es decir, colocar una reina, debemos anadirlo
        a nuestra tupla de reinas y actualizar la cobertura en los 4 sets
        """
        reinas, filas, columnas, diag_asc, diag_desc = state
        f, c = action
        return (
            reinas + (action,),
            filas | {f},
            columnas | {c},
            diag_asc | {f+c},
            diag_desc | {f-c},
        )

    def goal_test(self, state):
        """ El objetivo sera cubrir todo el tablero, este caso se comprobara"""
        reinas, filas, cols, diag_asc, diag_desc = state
        N = self.N
        for f in range(N):
            for c in range(N):
                if (f not in filas and c not in cols
                        and (f + c) not in diag_asc and (f - c) not in diag_desc):
                    return False
        return True

    # def h(self, node):
    #     """Return number of conflicting queens for a given node"""
    #     num_conflicts = 0
    #     for (r1, c1) in enumerate(node.state):
    #         for (r2, c2) in enumerate(node.state):
    #             if (r1, c1) != (r2, c2):
    #                 num_conflicts += self.conflict(r1, c1, r2, c2)
    #
    #     return num_conflicts
