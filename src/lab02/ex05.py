def row_sums(mat: list[list[float | int]]) -> list[float]:
    dlina = len(mat[0])
    for i in range(0, len(mat)):
        if dlina != len(mat[i]):
            raise TypeError("Длина не совпадает")

    summi = []
    for j in range(0, len(mat)):
        summi.append(sum(mat[j]))

    return summi


print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
