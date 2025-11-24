def transpose(mat: list[list[float | int]]):
    if len(mat) == 0:
        return []

    dlina = len(mat[0])
    for i in range(0, len(mat)):
        if dlina != len(mat[i]):
            raise TypeError("Длина не совпадает")

    col_strok = len(mat)
    col_stolb = len(mat[0])

    novaimatr = []
    for index_stolb in range(col_stolb):
        nov_strok = []
        for index_strok in range(col_strok):
            nov_strok.append(mat[index_strok][index_stolb])
        novaimatr.append(nov_strok)

    return novaimatr


print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
