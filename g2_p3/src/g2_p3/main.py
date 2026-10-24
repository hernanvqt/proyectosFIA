from problemagrafo import ProblemaGrafo
from search import uniform_cost_search
import time

nf_mapa = "src/g2_p3/mapa.txt"
nf_heuristica = "src/g2_p3/heuristica.txt"

# oviedoProb = ProblemaGrafo('Oviedo', 'Madrid', nf_mapa, nf_heuristica)
# zamoraProb = ProblemaGrafo('Zamora', 'Madrid', nf_mapa, nf_heuristica)
#
# oviedoSol = uniform_cost_search(oviedoProb, display=False)
# zamoraSol = uniform_cost_search(zamoraProb, display=False)


def medir_tiempo(algoritmo, m, inicial, goal, nf_mapa, nf_heuristica):
    """devuelve la lista de tiempos"""
    lista_tiempos = []
    for i in range(m):
        problema = ProblemaGrafo(inicial, goal, nf_mapa, nf_heuristica)
        t_inicio = time.time()
        nodo_sol = algoritmo(problema)
        t_fin = time.time()
        t_delta = t_fin-t_inicio
        lista_tiempos.append(t_delta)
    return lista_tiempos, nodo_sol


def imprimir_tiempo_solucion(tiempos, solucion):
    m = len(tiempos)
    tiempo_total = sum(tiempos)
    print(f"{'BCU':<15} | {m:<4} | {tiempo_total:>20} | {
          str(solucion):>15} | {solucion.path_cost:>10} |")


print(f"{'Algoritmo':<15} | {'M':<4} | {'Tiempo':>20} | {
      'Solucion':>15} | {'Coste':>10} |")
lista_M = [20, 80, 160, 250, 2000]
algoritmo = uniform_cost_search
inicial = 'Oviedo'
goal = 'Madrid'
for m in lista_M:
    tiempos, solucion = medir_tiempo(
        algoritmo, m, inicial, goal, nf_mapa, nf_heuristica)
    imprimir_tiempo_solucion(tiempos, solucion)
