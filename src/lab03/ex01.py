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
    
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))