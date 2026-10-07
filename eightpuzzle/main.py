from eightpuzzle import EightPuzzle


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


estado_inicial = (1, 5, 2, 4, 3, 0, 7, 8, 6)
puzzle = EightPuzzle(estado_inicial)
print(f"Inicio del problema: {estado_inicial}")
acciones_posibles = puzzle.actions(estado_inicial)
print(f"Acciones posibles: {acciones_posibles}")
estados_siguientes = genera_estados_siguientes(puzzle, estado_inicial, puzzle.actions(estado_inicial))
imprime_estados(estados_siguientes)
comprueba_objetivos(puzzle, estados_siguientes)
