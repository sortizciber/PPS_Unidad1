"""
lista.py solicita al usuario un número del 1 al 20 y después comprueba si se encuentra dentro de la lista.
"""

lista = [6,14,11,3,2,1,15,19]
minimo = 1
maximo = 20

try:
    valor = int(input("Introduce un número del 1 al 20: "))
except ValueError:
    valor = 10
    print("Tienes que introducir un número del 1 al 20. Elegimos 10 por defecto.")

def estaEnRango(valor, minimo, maximo):
    try:
        if valor >= minimo and valor <= maximo:
            return True
    except ValueError:
        return False
    except NameError:
        return False
        
def estaEnLista(valor, lista):
    try:
        if valor in lista:
            return True
    except NameError:
        return False
    except TypeError:
        return False

if estaEnRango(valor, minimo, maximo) and estaEnLista(valor, lista):
    print(f"{valor} está en rango y dentro de la lista.")
else:
    print(f"{valor} no está en la lista.")