from DomReina import DomReina

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


N = 4
problema = DomReina(N)

estado_inicial = ()
print(f"Inicio del problema: {estado_inicial}")

acciones_posibles = problema.actions(estado_inicial)
print(f"Acciones posibles: {acciones_posibles}")



