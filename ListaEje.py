Mi_lista = [12, 22, 33, 41, 52, 62, 75, 87, 92]
"""Se crea una simple lista"""


Mi_lista.insert(3, 44)
print("Resultado de insert(3, 44):", Mi_lista)
"""se remplaza la posicion de un digito"""


Mi_lista.append(10)
print("Resultado de append(10):", Mi_lista)
"""Se agrega al final de la lista otro numero"""

Mi_lista.extend([11, 12, 13])
print("Resultado de extend([11, 12, 13]):", Mi_lista)
"""Se agregan varios elementos o otra lista al final"""

Mi_lista.remove(44)
print("Resultado de remove(44):", Mi_lista)
"""Elimina el numero en especifico """


elemento_eliminado = Mi_lista.pop(5)
print("Elemento eliminado con pop(5):", elemento_eliminado)
print("Resultado después de pop(5):", Mi_lista)
"""Se elimina un indice en especifico"""


Mi_lista.clear()
print("Resultado de clear():", Mi_lista)
"""Se vacia la lista completamente"""