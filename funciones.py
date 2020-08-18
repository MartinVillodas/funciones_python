def promedio(numeros):
    promedio = sum(numeros) / len(numeros)
    return promedio

def ordenar(numeros):
    """Se le ingresa una lista de numeros y te la devuelve ordenada de menor a mayor"""
    ordenado = sorted(numeros)
    return ordenado

def lista_aleatoria(inicio, fin, cantidad):

    """ Recibe como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar. """

    import random

    lista = []

    for i in range(cantidad):
        numero = random.randrange(inicio, fin+1)
        lista.append(numero)

    return lista

def contar(valores, numero):
    """Con esta funcion podemos contar cuantas veces se repite un valor dentro de una lista. \n
    Primero se inserta el parametro "valores" que corresponde a la lista de numeros\n
    En el segundo parametro se inserta el numero que se quiere saber cuantas veces aparece en la lista"""
    cantidad_veces = valores.count(numero)
    return cantidad_veces