def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not isinstance(freq, dict):
        raise TypeError(f"Ожидается dict, получен {type(freq).__name__}")
    if not isinstance(n, int):
        raise TypeError(f"n должен быть int, получен {type(n).__name__}")

    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
