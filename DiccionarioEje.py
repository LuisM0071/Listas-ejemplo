Mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
"""Ejemplo de diccionario corto"""

print("copy:", Mi_diccionario.copy())
"""Crea una copia superficial del diccionario."""

print("fromkeys:", dict.fromkeys(['x', 'y'], 0))
"""Crea un nuevo diccionario con claves dadas y un valor por defecto."""

print("get:", Mi_diccionario.get('b'))
"""Obtiene el valor de la clave 'b' sin error si no existe."""

print("items:", list(Mi_diccionario.items()))
"""Devuelve una lista de pares (clave, valor)."""

print("keys:", list(Mi_diccionario.keys()))
"""Devuelve una lista de todas las claves."""

print("values:", list(Mi_diccionario.values()))
"""Devuelve una lista de todos los valores."""

print("pop:", Mi_diccionario.pop('c'))
"""Elimina la clave 'c' y devuelve su valor."""

print("popitem:", Mi_diccionario.popitem())
"""Elimina y devuelve el último par insertado."""

print("setdefault:", Mi_diccionario.setdefault('d', 4))
"""Devuelve el valor de 'd'; si no existe, lo crea con valor 4."""

print("update:", Mi_diccionario.update({'e': 5}), Mi_diccionario)
"""Agrega o actualiza claves con nuevos valores."""

Mi_diccionario.clear()
print("clear:", Mi_diccionario)
"""Elimina todos los elementos del diccionario."""
