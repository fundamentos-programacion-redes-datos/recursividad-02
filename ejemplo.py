"""

"""
# función recursiva
def suma_recursiva(lista_valores, numero_elementos):
    """
    Parámetro:
    - lista_valores: Lista que contiene los números para sumarlos.
    - numero_elementos: el tamaño de la lista, que se irá reduciendo en cada llamada recursiva.
    Retorna:
    - int: la suma de los elementos del arreglo o lista.
    """

    if numero_elementos == 1: 
        # caso base
        # El caso base es la condición que detiene la recursión.
        # Cuando se llega al último elemento de la lista, se retorna ese valor.
        # Sin el caso base, la función seguiría llamándose a sí misma infinitamente.
        return lista_valores[0]
    else:
        # proceso/paso recursivo
        # La función se llama a sí misma con el mismo parámetro de lista_valores,
        # pero con numero_elementos reducido en 1. Esto reduce el tamaño del problema
        # en cada llamada hasta llegar al caso base.
        # En cada paso, se agrega el valor actual de lista_valores[numero_elementos - 1]
        # al resultado de la llamada recursiva que suma los elementos anteriores.
        return lista_valores[numero_elementos - 1] + \
            suma_recursiva(lista_valores, numero_elementos - 1)

def valores_cadena(lista_valores):
    """
    Parámetro:
    - lista_valores: lista de elementos para pasarlos a una sola cadena.
    Retorna:
    - str: una cadena que contiene todos los elementos de la lista.
    """
    cadena = ""
    # El ciclo for recorre cada valor de la lista y lo convierte en una cadena.
    for valor in lista_valores:
        # En cada iteración, concatenamos el valor con un salto de línea.
        # De esta manera, generamos una cadena de texto donde cada valor de la lista está
        # separado por una nueva línea.
        cadena = f"{cadena}{valor}\n"
    return cadena


if __name__ == '__main__':
    
    valores = [10, 20, 100, 3000, 40]
    # Se convierte la lista de valores a una cadena con formato
    valores_en_cadena = valores_cadena(valores)
    
    # Se calcula la suma de los valores en la lista utilizando recursividad
    suma = suma_recursiva(valores, len(valores))
    
    # Se muestra la cadena con los valores y la suma final calculada recursivamente
    print(f"La suma de los valores del arreglo {valores_en_cadena}es: {suma}")
