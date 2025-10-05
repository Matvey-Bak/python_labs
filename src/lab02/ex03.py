def flatten(mat: list[list | tuple]) -> list:
    sp = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            return "TypeError"
        else:
            sp.extend(i)    
    return sp

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
