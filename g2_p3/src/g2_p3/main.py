from problemagrafo import ProblemaGrafo
from search import uniform_cost_search
from search import greedy_best_first_graph_search
from search import astar_search
import time
from pathlib import Path


def resolver_ruta(nombre_fichero):
    candidatos = [
        Path(nombre_fichero),
        Path(__file__).resolve().parent / nombre_fichero,
        Path("src/g2_p3") / nombre_fichero,
        Path("src/BusquedaGrafo") / nombre_fichero,
    ]
    for c in candidatos:
        if c.exists():
            return str(c)
    return nombre_fichero


nf_mapa = resolver_ruta("mapa.txt")
nf_heuristica = resolver_ruta("heuristica.txt")


def medir_tiempo(algoritmo, m, inicial, goal, *args, **kwargs):
    if len(args) == 2:
        mapa_file, heuris_file = args
    elif len(args) >= 3:
        _, mapa_file, heuris_file = args[:3]
    else:
        mapa_file = kwargs.get('nf_mapa', nf_mapa)
        heuris_file = kwargs.get('nf_heuristica', nf_heuristica)

    lista_tiempos = []
    nodo_sol = None
    for _ in range(m):
        problema = ProblemaGrafo(inicial, goal, mapa_file, heuris_file)
        t_inicio = time.time()
        nodo_sol = algoritmo(problema)
        t_fin = time.time()
        t_delta = t_fin - t_inicio
        lista_tiempos.append(t_delta)
    return lista_tiempos, nodo_sol


def imprimir_tiempo_solucion(tiempos, solucion, algoritmo_nombre="BCU"):
    m = len(tiempos)
    tiempo_medio = sum(tiempos) / m if m > 0 else 0
    sol_str = str(solucion.solution()) if hasattr(solucion, 'solution') else str(solucion)
    coste = solucion.path_cost if hasattr(solucion, 'path_cost') else "N/A"
    print(f"{algoritmo_nombre:<9} | {m:<5} | {tiempo_medio:>13.8f} s | {sol_str:<46} | {coste:>6} |")


def imprimir_tiempo_solucion_no_informada(lista_M, inicial, goal):
    """Mide y muestra la tabla para búsqueda no informada (BCU) para una lista de M iteraciones."""
    print(f"{'Algoritmo':<9} | {'M':<5} | {'Tiempo':>15} | {'Solución':<46} | {'Coste':>6} |")
    print("-" * 92)
    for m in lista_M:
        tiempos, solucion = medir_tiempo(
            uniform_cost_search, m, inicial, goal, nf_mapa, nf_heuristica)
        imprimir_tiempo_solucion(tiempos, solucion, "BCU")


def medir_tiempo_informada(algoritmo, m, inicial, goal, nf_mapa, nf_heuristica):
    lista_tiempos = []
    nodo_sol = None
    for _ in range(m):
        problema = ProblemaGrafo(inicial, goal, nf_mapa, nf_heuristica)
        t_inicio = time.time()
        nodo_sol = algoritmo(problema, problema.h)
        t_fin = time.time()
        t_delta = t_fin - t_inicio
        lista_tiempos.append(t_delta)
    return lista_tiempos, nodo_sol


def imprimir_tiempo_solucion_informada(lista_M, inicial, goal):
    print(f"{'Algoritmo':<9} | {'M':<5} | {'Tiempo':>15} | {'Solución':<46} | {'Coste':>6} |")
    print("-" * 92)
    for m in lista_M:
        tiemposBV, solucionBV = medir_tiempo_informada(
            greedy_best_first_graph_search, m, inicial, goal, nf_mapa, nf_heuristica)
        imprimir_tiempo_solucion(tiemposBV, solucionBV, "BV")

        tiemposBA, solucionBA = medir_tiempo_informada(
            astar_search, m, inicial, goal, nf_mapa, nf_heuristica)
        imprimir_tiempo_solucion(tiemposBA, solucionBA, "BA*")


def main():
    lista_M = [20, 80, 160, 250, 2000]

    casos = [
        ("Oviedo", "Madrid"),
        ("Zamora", "Madrid")
    ]

    for origen, destino in casos:
        print(f"\n>>> Comprobación solución individual: {origen} -> {destino}")
        prob = ProblemaGrafo(origen, destino, nf_mapa, nf_heuristica)
        sol = uniform_cost_search(prob)
        ruta = [n.state for n in sol.path()]
        print(f"    Ruta óptima: {' -> '.join(ruta)}")
        print(f"    Acciones:    {sol.solution()}")
        print(f"    Coste total: {sol.path_cost}")

    for origen, destino in casos:
        print(f"\n>>> Medición de tiempos BCU ({origen} -> {destino}):")
        imprimir_tiempo_solucion_no_informada(lista_M, origen, destino)


if __name__ == "__main__":
    main()