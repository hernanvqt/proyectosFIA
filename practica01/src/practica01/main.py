# Curso 2026-27 - FIA
# Programa que devuelve el hito más relevante de la IA dado un año
# Grupo: B
# Nombres y apellidos: Trajano Arthur Iacob, Hernan Velarde Quiros
#


# Ejercicio 1
# a) (respuesta al apartado a)
# Ninguno ha sido capaz de pasar por humano.
# La razon por la que Eliza no pasa el test de Turing es porque
# repite mucho algunas sentencias ignorando al entrevistador
# con la intencion de seguir su guion.
# Parry por otro lado, tiene un guion que impide que sea mas libre
# para cometer errores, sus respuestas con muy consisas, lo cual
# dificulta el test. Ademas de que el LLM le ayuda en gran medida.

# b) (respuesta al apartado b)
# Parry es mejor que las dos porque el LLM le ayuda mucho. Entre las dos
# Eliza es muy repititiva y siempre utiliza las mismas frase cambiando
# un par de palabras con las que usaste antes, Alicia lo disfraza mejor
#
# c) (respuesta al apartado c)
#
# No parecen dos humanos, porque ambos son muy insistentes con sus temas,
# Elizia repite constamente las mismas frases y Parry pese a pecar de lo
# mismo, es capaz de darse cuenta de que Elizia se repite por lo que es
# mejor.

# Ejercicio 2

def pide_datos():
    anios = input("Hola, introduce varios anios y te dire los hitos mas importantes de la IA (introduce 0 para salir): ").strip()
    if (anios == "0"):
        return []
    else:
        return anios.split()


def extrae_datos_linea(linea):
    elem = linea.strip().split(",")
    return {"inicio": elem[0], "fin": elem[1], "texto": " ".join(elem[2:])}


def extrae_datos_fichero(nombre_fichero):
    datos = []
    with open(nombre_fichero) as f:
        for linea in f:
            hito = extrae_datos_linea(linea)
            datos.append(hito)
    return datos[1:]


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
        endHito = int(lista_hitos[medio]["fin"])
        if (startHito == endHito and startHito == anio_int):
            return lista_hitos[medio]["texto"]
        elif (startHito < anio_int):
            start = medio + 1
        else:
            end = medio-1

    for hito in lista_hitos:
        if int(hito["inicio"]) <= anio_int <= int(hito["fin"]):
            return hito["texto"]

    return "no tengo información suficiente"


def imprime_hito(hito, anio):
    print(f"En {anio} {hito}")

def estadisticas_busqueda(hitos_consultados, lista_hitos):
    

def main():
    print('Ejercicio 2a: Bienvenido al Programa modular de historia de la IA')
    lista_anios = pide_datos()
    lista_hitos = extrae_datos_fichero("historiaIAg2.csv")

    while (len(lista_anios) > 0):
        for anio in lista_anios:
            hito = busca_anio_en_lista(lista_hitos, anio)
            imprime_hito(hito, anio)
        lista_anios = pide_datos()
    print("Gracias por utilizar el programa")

    # Implementación de apartado b
    print('Ejercicio 2b: Bienvenido a la base de conocimiento de la historia de la IA')




if __name__ == "__main__":
    main()
