a = {"Jose", "X", 3, 12}

b = {"Keyla", 4, "Y", 88}

print("copy:", a.copy())
"""Copia el conjunto a."""

a.add(10)
"""Agrega el número 10 al conjunto a."""

print("add:", a)
"""Muestra el conjunto a después de agregar."""

temp = b.copy()
"""Copia el conjunto b en temp."""

temp.clear()
"""Vacía el conjunto temp."""

print("clear:", temp)
"""Muestra temp vacío."""

a.update([20, 30])
"""Agrega 20 y 30 al conjunto a."""

print("update:", a)
"""Muestra el conjunto a actualizado."""

print("difference:", a.difference(b))
"""Elementos en a que no están en b."""

print("union:", a.union(b))
"""Todos los elementos de a y b sin repetir."""

print("intersection:", a.intersection(b))
"""Elementos que están en ambos conjuntos."""

a.difference_update(b)
"""Quita de a los elementos que también están en b."""

print("difference_update:", a)
"""Muestra el conjunto a después de eliminar coincidencias con b."""