"""
La La ruina del apostador (Gambler's Ruin) dice que una persona que juegue algún juego con un valor esperado negativo llegará a perder todo su dinero tarde o temprano, 
sin importar el sistema que use para apostar.
Podemos hacer una simulación de este concepto en Python, usando la librería random.
Supongamos que comenzamos con 50 fichas (todas del mismo valor) y apostamos una ficha cada vez que jugamos.
Tenemos una probabilidad de 0.4 de ganar cada vez que jugamos (cómo podemos simular esto?). Si ganamos, tenemos una ficha más.
Caso contrario, perdemos la ficha que apostamos.
En una noche se estima que podemos jugar este juego hasta 300 veces, pero si llegamos a tener 0 fichas ya no vamos a poder apostar en toda la noche.
Crear un programa que simule nuestra noche de apuestas, que imprima en pantalla cuántas apuestas pudimos hacer antes de perder todo el dinero o 
si pudimos sobrevivir a las 300 apuestas.
Para resolver el problema, crear una función que tenga como entradas la cantidad de fichas inicial, la probabilidad de victoria de cada juego y 
la cantidad máxima de veces que podemos jugar, que devuelva la cantidad de fichas con la que terminamos al final de la noche y la cantidad de apuestas que pudimos hacer.
Correr esta función 20 veces y obtener el valor medio de la cantidad de apuestas final.
Cuánto tiempo tarda cada simulación en ejecutarse? Imprimir en pantalla este tiempo cada vez que se corre la función.
"""

#Integrantes = Higueras, Emiliano / Vinci da Silva, Juan Manuel / Venero, Héctor
import random 


def apostar (cantidad_fichas, cantidad_apuestas_límite):

    contador = 0
    while cantidad_fichas > 0 and contador < cantidad_apuestas_límite:
        # 1 gano siempre, 0 pierdo siempre, 0,4 es la probabilidad de acertar, osea el 40 %
        resultado = random.uniform (0,1) <= 0.4
        if resultado == 1:
            cantidad_fichas += 1
        else:
            cantidad_fichas -= 1

        contador += 1

    return contador, cantidad_fichas


for x in range (0, 20):
    resultado = apostar (50, 300)
    print (f"Esta noche tu límite de apuestas fue de {resultado [0]} veces y te quedaron un total de {resultado [1]} fichas ")

