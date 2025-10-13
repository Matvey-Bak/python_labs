def remove_emoji(text: str) -> str:
    # Основные диапазоны эмодзи в Unicode
    emoji_ranges = [
        (0x1F600, 0x1F64F),  
        (0x1F300, 0x1F5FF), 
        (0x1F680, 0x1F6FF),  
        (0x1F1E0, 0x1F1FF),
        (0x2600, 0x26FF),    
        (0x2700, 0x27BF),    
        (0xFE00, 0xFE0F),    
        (0x1F900, 0x1F9FF),  
    ]
    
    result = []
    for char in text:
        # Проверяем, попадает ли символ в любой из диапазонов эмодзи
        is_emoji = any(start <= ord(char) <= end for start, end in emoji_ranges)
        if not is_emoji:
            result.append(char)
    
    return ''.join(result)


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True, remove_emojis: bool = True):
    normalize_text = ""
    
    if remove_emojis:
        text = remove_emoji(text)
    
    for part_text in text:
        if part_text in ['\t', '\r', '\n']:
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

    
def tokenize(text: str):
    token = normalize(text)
    token_1 = token.split()
    return token_1


print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("emoji 😀 не слово"))
