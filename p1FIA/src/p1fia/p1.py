# Curso 2026-27 - FIA
# Programa que devuelve el hito más relevante de la IA dado un año
# Grupo:
# Nombres y apellidos:
#

# Ejercicio 1
# a) (respuesta al apartado a)
#
#
#
# b) (respuesta al apartado b)
#
#
#
# c) (respuesta al apartado c)
#
#
#
#

# Ejercicio 2

def pide_datos():
    anios = []
    anios = input("Hola, introduce varios anios y te dire los hitos mas importantes de la IA (introduce 0 para salir): ")
    return anios


def extrae_datos_linea(linea):
    elem = linea.strip().split(",")
    return {"inicio": elem[0], "fin": elem[1], "texto": " ".join(elem[2:])}


def extrae_datos_fichero(nombre_fichero):
    datos = []
    with open(nombre_fichero) as f:
        for linea in f:
            hito = extrae_datos_linea(linea)
            datos.append(hito)
    return datos


def muestra_hitos(lista_hitos):
    for hito in lista_hitos:
        if (hito['inicio'] == hito['fin']):
            print(f"En {hito['inicio']} {hito['texto']}")
        else:
            print(f"Entre el {hito['inicio']} y {hito['fin']} {hito['texto']}")


def busca_anio_en_lista(lista_hitos, anio):
    anio_int = int(anio)

    start = 0
    end = len(lista_hitos)-1
    while (start <= end):
        medio = (start + end) // 2
        startHito = int(lista_hitos[medio]["inicio"])
        if (startHito == anio_int):
            return lista_hitos[medio]["texto"]
        elif (startHito < anio_int):
            start = medio + 1
        else:
            end = medio-1

    for hito in lista_hitos:
        if int(hito["inicio"]) < anio_int < int(hito["fin"]):
            return hito["texto"]

    return "no tengo información suficiente"


def imprime_hito(hito, anio):
    print(f"En {anio} {hito['texto']}")


def main():
    print('Ejercicio 2a: Bienvenido al Programa modular de historia de la IA')
    print("Bienvenido al Programa modular de historia de la IA")
    lista_anios = pide_datos()
    lista_hitos = extrae_datos_fichero("historiaIAg2.csv")

    while (lista_anios != "0"):
        for anio in lista_anios:
            hito = busca_anio_en_lista(lista_hitos, anio)
            imprime_hito(hito, anio)
        lista_anios = pide_datos()
    print("Gracias por utilizar el programa")

    # Implementación de apartado b
    print('Ejercicio 2b: Bienvenido a la base de conocimiento de la historia de la IA')

#  def estadisticas_busqueda(hitos_consultados, lista_hitos):


if __name__ == "__main__":
    main()
