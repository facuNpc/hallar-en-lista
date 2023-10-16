
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


if __name__ == '__main__':

    inicio = 0
    fin = 1000

    lista_numeros = lista_aleatoria(inicio, fin)


