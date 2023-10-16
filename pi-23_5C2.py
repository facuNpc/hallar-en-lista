
import random


def lista_aleatoria (inicio, fin):
    lista_random = []
    while True:
        try:
            cantidad = int(input("Cuantos numeros desea generar?: "))
            break
        except:
            pass

    for i in range(cantidad):
        numero = random.randint(inicio, fin)
        lista_random.append(numero)
    return lista_random


def contar_repeticiones(lista_numeros, numero_repite):
    se_repite = lista_numeros.count(numero_repite)
    return se_repite


if __name__ == '__main__':

    inicio = 0
    fin = 400

    lista_numeros = lista_aleatoria(inicio, fin)
    while True:
        try:
            numero_repite = float(input("Cuantas veces se repite el numero: "))
            break
        except:
            pass
    se_repite = contar_repeticiones(lista_numeros, numero_repite)
    print(f"El numero {numero_repite} se repite en la lista {se_repite} veces")
