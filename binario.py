"""
binario.py solicita al usuario un número binario e imprime por pantalla el número
convertido a formato decimal utilizando la función esBinario() para comprobar.
"""

print("Conversor de números binarios a decimales\n")

strbinario = input("Introduce un número binario: ")


def esBinario(strbinario):
    try:
        for digito_string in strbinario:
            if digito_string !="0" and digito_string !="1":
                 return False
        return True
    except TypeError:
        return False
        
if esBinario(strbinario):
    decimal = int(strbinario, 2) #el 2 indica la base en la que se encuentra el número a convertir, binario en este caso
    print(f"{strbinario} es en {decimal}")
else:
     print("El número introducido no es binario")