from problemagrafo import ProblemaGrafo
from search import uniform_cost_search


def medir_tiempo(algoritmo, m, inicial, goal, grafo, nf_mapa, nf_heuristica):
    """devuelve la lista de tiempos"""
nf_mapa = "src/g2_p3/mapa.txt"
nf_heuristica = "src/g2_p3/heuristica.txt"

oviedoProb = ProblemaGrafo('Oviedo', 'Madrid', nf_mapa, nf_heuristica)
zamoraProb = ProblemaGrafo('Zamora', 'Madrid', nf_mapa, nf_heuristica)

oviedoSol = uniform_cost_search(oviedoProb, display=False)
zamoraSol = uniform_cost_search(zamoraProb, display=False)
