#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"

import funciones as fun

def ej1():
    print('Comencemos a crear lo nuestro!')

    '''
    Cree un nuevo archivo el cual será su módulo que utilizará
    para resolver todos los ejercicios de está guía.
    En el módulo implemente todas las funciones que le fueron
    solicitadas en "ejercicios_clase":
    - promedio
    - lista_aleatoria
    - ordenar
    - contar

    Importe el módulo a este programa/documento para su uso
    en el resto de los ejercicios
    '''


def ej2():
    print("Jugando a los dados")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 valores con resultados posibles
    de un dado)
    ejemplo, se tiraron 5 dados y los resultados de lista aleatoria
    se deben parecer a:
    [1, 2, 3, 2, 5]
    Cada valor representa el valor que sacó cada uno de los 5 dados

    1)
    Utilice la función "ordenar" para ordenar la lista
    de números generados.
    Imprimir en pantalla la lista ordenada
    '''
    tiro_dados = fun.lista_aleatoria(1, 6, 5)
    print("Los resultados de tirar los dados 5 veces fueron:", tiro_dados)
    print("Con los numeros ordenados seria:", fun.ordenar(tiro_dados))



def ej3():
    print("Jugando a los dados")

    '''
    Un dado común tiene 6 caras, 6 resultados posibles
    1 - 2 - 3 - 4 - 5 - 6

    Utilice la función "lista_aleatoria" para generar
    5 tiros de dados (una lista de 5 valores con resultados posibles
    de un dado)
    ejemplo, se tiraron 5 dados y los resultados de lista aleatoria
    se deben parecer a:
    [1, 2, 3, 2, 5]
    Cada valor representa el valor que sacó cada uno de los 5 dados

    1)
    Utilice la función "contar" para contar cuantas veces aparece:
    a - Cuantsa veces aparece el número 1 en su lista de dados tirados
    b - Cuantsa veces aparece el número 2 en su lista de dados tirados
    c - Cuantsa veces aparece el número 3 en su lista de dados tirados
    d - Cuantsa veces aparece el número 4 en su lista de dados tirados
    e - Cuantsa veces aparece el número 5 en su lista de dados tirados
    f - Cuantsa veces aparece el número 6 en su lista de dados tirados


    2)
    Utilice la función de Python max con la key de list.count para
    determinar cual fue el número que más se repitió. Consultar los ejemplos
    vistos en clase para ver como se implementa max con esa key

    '''
    tiro_dados = fun.lista_aleatoria(1 , 6, 5)
    print("Los resultados de tirar los dados 5 veces fueron:", tiro_dados)
    print("El numero 1 aparece {} veces".format(fun.contar(tiro_dados, 1)))
    print("El numero 2 aparece {} veces".format(fun.contar(tiro_dados, 2)))
    print("El numero 3 aparece {} veces".format(fun.contar(tiro_dados, 3)))
    print("El numero 4 aparece {} veces".format(fun.contar(tiro_dados, 4)))
    print("El numero 5 aparece {} veces".format(fun.contar(tiro_dados, 5)))
    print("El numero 6 aparece {} veces".format(fun.contar(tiro_dados, 6)))

    mas_repetido = max(tiro_dados, key=tiro_dados.count)
    print("El numero que mas veces se repitio fue:", mas_repetido)

def ej4():
    print("\n")
    print("Juguemos a la Generala")
    print("\n")

    '''
    Este ejercicio representa ya un problema que forma parte de un juego
    Lo que se desea realizar es una parte del juego "la generala".
    El enunciado está armado a modo de guía, pueden resolver el problemla
    de otra forma.
    Si tienen dudas sobre el enunciado o alguno de los puntos por favor
    comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
    puede haber varias interpretaciones de un mismo enunciado.

    Deberá realizar una lista para guardar 5 dados, guardar los números
    sacados en esa tirada de de dados (son 5 números del 1 al 6)

    1) El jugador tira la dados y sacar 5 números aleatorios, puede usar
    la función de "lista_aleatoria" para generar dichos números.

    2) Luego debe analizar los 5 números y ver cual es el número que
    más se repitio entre los 5 dados.
    Debe usar la función de Python max con la key de list.count paara
    determinar cual fue el número que más se repitió. Consultar los ejemplos
    vistos en clase o el ejercicio anterior de esta guia.

    3) Una vez reconocido el número más repetido entre los 5, debe
    guardar en una lista esos números.
    Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4"
    Debe extrarlos de la lista, quedándole una lista separada
    dados_guardados = [4,4,4]
    Debe realizar un bucle para recorrer la lista de dados_tirados
    y guardar los "4" en nuestra nueva lista dados_guardados
    Utilie append para ir sumando a dados_guardados los valores

    4) Debe volver a tira los dados, generar nuevos
    números aleatorios.
    Si en la lista "dados_guardados" tengo 3 dados guardados
    significa que ahora deberé tirar dos dados. Puede usar la función
    "len" para ver cuantos elementos hay en "dados_guardados"
    Es decir que en este caso debería generar dos números
    aleatorios nuevos con "lista_generica"
    Ahora tendré una nueva lista de "dados_tirados" en este caso
    de dos nuevos números aleatorios entre 1 y 6 representando a los dados
    tirados.

    5) Luego de tirar nuevamente los datos, por ejemplo digamos
    que salieron los números: 4-1
    Debo volver a quedarme con el "4" ya que es el número que estoy
    buscando.
    Sino salió el "4" vuelvo a tirar todos los dados.
    Si salió un "4" me lo quedo y lo guardo en "dados_guardados".

    5) Debe repetir este proceso hasta que en su lista de "dados
    guardados" tenga "generala", es decir, 5 números iguales.

    '''
    for h in range(1):

        print("Escriba `lanzar´ en el teclado para tirar los dados")
        inicio = str(input())
        print("\n")

        if inicio == "lanzar": #Genero 5 lanzamientos de dados aleatorios y los imprimo
            dados_lanzados = fun.lista_aleatoria(1, 6, 5)
            print("Tus dados salieron con los siguientes numeros:", dados_lanzados)
            print("\n")
        
            #Analizo cual es el numero que mas se repitio
            repetido = max(dados_lanzados, key= dados_lanzados.count) #Esto me dice el numero mas repetido
            cantidad_repetido = fun.contar(dados_lanzados, repetido) #Esto me dice cuantas veces sale el numero mas repetido
            print("El numero mas repetido es {} y sale {} veces".format(repetido, cantidad_repetido))
            print("\n")


            #Creo una lista vacia donde se guardaran los dados repetidos segun la cantidad de veces que salen
            dados_guardados = [] 
            for i in range(cantidad_repetido):
                dados_guardados.append(repetido)
            print("La nueva lista con los dados repetidos es:", dados_guardados)
            print("\n")


            #Vuelvo a tirar los dados o paro el juego, segun len(datos_guardados) > 1
            #Si se tiran los dados, se hace sin los dados repetidos
            
            if len(dados_guardados) > 1:
                
                while True:
                    inicio_2 = str(input("Lance los dados nuevamente con la palabra `lanzar´:\n"))
                    if inicio_2 == "lanzar":
                        dados_lanzados_2 = fun.lista_aleatoria(1, 6, len(dados_lanzados)- len(dados_guardados))
                        print("\n")
                        print("Los dados lanzados son:", dados_lanzados_2)
                        print("\n")

                        #Verifico si uno de los dados lanzados por segunda vez es igual a los dados guardados
                        for i in range(1):
                            if len(dados_guardados) < 5:
                                repetido_2 = fun.contar(dados_lanzados_2, dados_guardados[0])
                                for n in range(repetido_2):
                                    dados_guardados.append(dados_guardados[0])
                                    print("Tus dados guardados son:", dados_guardados)
                                    print("\n")
                                if repetido_2 == 0:
                                    print("No hubo coincidencia")
                                    break
                        for i in range(1):
                            if len(dados_guardados) == 5:
                                print("Felicitaciones, has hecho una generala")
                                break
                        if repetido_2 == 0:
                            break
                        if len(dados_guardados) == 5:
                            break

                    else:
                        break
            else:
                print("Lo siento, no te ha tocado ningun numero igual")
                break

        elif inicio == "fin":
            break
        else:
            print("El comando ingresado no existe, por favor escriba `lanzar´ para jugar o `fin´ para finalizar.")
            
  
    



if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()

    #while True:
     #   print("a")
      #  if True:
       #     print("b")
        #    while True:
         #       print("C")
          #      break # Con esto rompo el while interno y el if del medio solo se ejecuta una vez
        #break #Con esto rompo el primer while