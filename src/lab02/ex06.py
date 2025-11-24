def col_sums(mat: list[list[float | int]]) -> list[float]:
    dlina = len(mat[0])
    for i in range(0, len(mat)):
        if dlina != len(mat[i]):
            raise TypeError("Длина не совпадает")

    sp = []
    for index_stolb in range(len(mat[0])):
        summa = 0
        for riad in mat:
            summa += riad[index_stolb]

        sp.append(summa)

    return sp


print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
