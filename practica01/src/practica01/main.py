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

from pathlib import Path

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
    ruta = Path(__file__).resolve().parent / nombre_fichero
    if not ruta.is_file():
        ruta = Path(__file__).resolve().parents[1] / nombre_fichero
    if not ruta.is_file():
        ruta = Path(nombre_fichero)

    datos = []
    with open(ruta, encoding="utf-8") as f:
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
    total_anios = len(hitos_consultados)
    print(f"a.Número total de años consultados: {total_anios}")

    min_anioInicio = float('inf')
    cont_inviernos = 0
    hito_mas_antiguo = None

    for anio in hitos_consultados:
        int_anio = int(anio)
        hito_encontrado = None

        for hito in lista_hitos:
            ini = int(hito["inicio"])
            fin = int(hito["fin"])

            if ini <= int_anio <= fin:
                if hito_encontrado is None or (ini == int_anio == fin):
                    hito_encontrado = hito

        if hito_encontrado:
            ini_hito = int(hito_encontrado["inicio"])
            if ini_hito < min_anioInicio:
                min_anioInicio = ini_hito
                hito_mas_antiguo = hito_encontrado["texto"]

            if "invierno" in hito_encontrado["texto"].lower():
                cont_inviernos += 1

    if hito_mas_antiguo:
        print(f"b. El hito histórico más antiguo de los que ha consultado el usuario: {hito_mas_antiguo}")
    else:
        print("b. No se ha encontrado ningún hito histórico consultado por el usuario.")
    
    print(f"c. Años consultados correspondieron a los inviernos de la IA.: {cont_inviernos}")
        

def main():
    print('Ejercicio 2: Bienvenido al Programa modular de historia de la IA')
    lista_hitos = extrae_datos_fichero("historiaIAg2.csv")
    lista_anios = pide_datos()
    hitos_consultados = []

    while (len(lista_anios) > 0):
        for anio in lista_anios:
            hitos_consultados.append(anio)
            hito = busca_anio_en_lista(lista_hitos, anio)
            imprime_hito(hito, anio)
        lista_anios = pide_datos()

    estadisticas_busqueda(hitos_consultados, lista_hitos)
    print("Gracias por utilizar el programa")

if __name__ == "__main__":
    main()