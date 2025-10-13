# Лабораторная работа №3
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    normalize_text = ""
    for part_text in text:
        if part_text in {'\t', '\r', '\n'}:
            normalize_text += ' '
        else:
            normalize_text += part_text

    if yo2e:    
        normalize_text = normalize_text.replace("ё", "е")
        normalize_text = normalize_text.replace("Ё", "Е")

    if casefold:
        normalize_text = normalize_text.casefold()

    normalize_text = " ".join(normalize_text.split())

    return normalize_text

import re

def tokenize(text: str):
    token = normalize(text)
    
    token = re.sub(r'[^\w\s]', '', token)
    
    token_1 = token.split()
    return token_1


def count_freq(tokens: list[str]):
    count = {}
    for i in tokens:
        count[i] = count.get(i, 0) + 1
    return count

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]