def count_freq(tokens: list[str]):
    count = {}
    for i in tokens:
        count[i] = count.get(i, 0) + 1
    return count

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]

print(top_n(count_freq(["a","b","a","c","b",]), n = 2))
print(top_n(count_freq(["bb","aa","bb","aa","cc","bb"]), n = 2))