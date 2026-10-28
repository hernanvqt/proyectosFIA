from problemagrafo import ProblemaGrafo
from search import uniform_cost_search
from search import greedy_best_first_graph_search
from search import astar_search
import time

nf_mapa = "src/g2_p3/mapa.txt"
nf_heuristica = "src/g2_p3/heuristica.txt"


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
    tiempo_total = sum(tiempos)/m
    print(f"{'BCU':<15} | {m:<4} | {tiempo_total:>25} | {
          str(solucion.solution()):>45} | {solucion.path_cost:>10} |")


def imprimir_tiempo_solucion_no_informada(lista_M, inicial, goal):
    print(f"{'Algoritmo':<15} | {'M':<4} | {'Tiempo':>25} | {
          'Solucion':>45} | {'Coste':>10} |")
    for m in lista_M:
        tiempos, solucion = medir_tiempo(
            uniform_cost_search, m, inicial, goal, nf_mapa, nf_heuristica)
        imprimir_tiempo_solucion(tiempos, solucion)


def medir_tiempo_informada(algoritmo, m, inicial, goal, nf_mapa, nf_heuristica):
    """devuelve la lista de tiempos"""
    lista_tiempos = []
    for i in range(m):
        problema = ProblemaGrafo(inicial, goal, nf_mapa, nf_heuristica)
        t_inicio = time.time()
        nodo_sol = algoritmo(problema, problema.h)
        t_fin = time.time()
        t_delta = t_fin-t_inicio
        lista_tiempos.append(t_delta)
    return lista_tiempos, nodo_sol


def imprimir_tiempo_solucion_informada(lista_M, inicial, goal):
    print(f"{'Algoritmo':<10} | {'M':<4} | {'Tiempo':>25} | {
          'Solucion':>45} | {'Coste':>10} |")
    for m in lista_M:
        tiemposBV, solucionBV = medir_tiempo_informada(
            greedy_best_first_graph_search, m, inicial, goal, nf_mapa, nf_heuristica)
        ruta = inicial + ", " + ", ".join(solucionBV.solution())
        print(f"{'BV':<10} | {m:<4} | {sum(tiemposBV)/m:>25} | {
            str(ruta):>45} | {solucionBV.path_cost:>10} |")

        tiemposBA, solucionBA = medir_tiempo_informada(
            astar_search, m, inicial, goal, nf_mapa, nf_heuristica)
        ruta = inicial + ", " + ", ".join(solucionBA.solution())
        print(f"{'BA*':<10} | {m:<4} | {sum(tiemposBA)/m:>25} | {
              str(ruta):>45} | {solucionBA.path_cost:>10} |")


lista_M = [20, 80, 160, 250, 2000]
inicial = 'Oviedo'
goal = 'Madrid'
imprimir_tiempo_solucion_informada(lista_M, inicial, goal)
# listaOrigenes = ('Valladolid', 'Barcelona', 'Zaragoza', 'Salamanca', 'Avila', 'Burgos', 'Bilbao', 'Sevilla', 'Merida', 'Cordoba',
#          'Albacete', 'Murcia', 'Oviedo', 'Leon', 'Lugo', 'Valencia', 'Soria', 'Guadalajara', 'Segovia', 'Palencia', 'Zamora', 'Santander')
#
# for inicial in listaOrigenes:
#     goal = 'Madrid'
#     imprimir_tiempo_solucion_informada(lista_M, inicial, goal)
