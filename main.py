a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
fb = frozenset(b)

print(fb)
# c = a.intersection(b) # выборка одинаковых значений
# c = a.union(b) # объединение без дублирования
# c = a.difference(b)
# c = b.difference(a) # все элементы одного множества без элементов второго
# c = a.symmetric_difference(b) # симетричная разность (все, в обоих множествах без общих значений)
print(a)
# a.intersection_update(b)
a.update({6})
print(a)