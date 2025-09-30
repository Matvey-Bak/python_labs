def srt(sp):
    if len(sp) == 0:
        return "ValueError"
    elif len(sp) > 1:
        return min(sp), max(sp)
    elif len(sp) == 1:
        return min(sp), max(sp)
    

sp1 = [3, -1, 5, 5, 0]
sp2 = [42]
sp3 = [-5, -2, -9]
sp4 = []
sp5 = [1.5, 2, 2.0, -3.1]
print(srt(sp1))
print(srt(sp2))
print(srt(sp3))
print(srt(sp4))
print(srt(sp5))

mn1 = {3, 1, 2, 1, 3}
a = sorted(mn1)
print(a)

sp6 = [[1, 2], "ab"]
sp7 = []
for item in sp6:
    if isinstance(item, str):
        print("TypeError")
        break
    elif isinstance(item, list):
        sp7.extend(item)
else:
    print(sp7)




