"""
Ejercicio
"""

conjunto = []

conjunto.append(1)
print(conjunto)

conjunto.insert(0, 2)
print(conjunto)

conjunto.extend((3, 4, 5))
print(conjunto)

conjunto[4:4] = [6, 7, 8]
print(conjunto)

del conjunto[4]
print(conjunto)

conjunto[3] = 2
print(conjunto)

print({5 in conjunto})

conjunto.clear()
print(conjunto)


"""
Extra
"""

set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 2, 3, 4, 6, 7}

print(set_1.union(set_2))
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_1.symmetric_difference(set_2))