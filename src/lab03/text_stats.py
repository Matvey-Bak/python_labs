import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from lib.text import normalize, tokenize, count_freq, top_n


table_mode = os.getenv("table_mode", "true").lower() == "true"


def format_table(top_words):
    if not top_words:
        raise ValueError("Нет данных для отображения")

    max_word_length = max(len(str(word)) for word, _ in top_words)
    max_word_length = max(max_word_length, 6)

    header_word = "слово".ljust(max_word_length)
    header = f"{header_word} | частота"
    separator = "-" * (len(header) + 2)

    lines = [header, separator]
    for word, count in top_words:
        word_str = str(word).ljust(max_word_length)
        lines.append(f"{word_str} | {count}")

    return "\n".join(lines)


def format_simple(top_words):
    lines = []
    for word, count in top_words:
        lines.append(f"{word}: {count}")
    return "\n".join(lines)


def main():
    text = input("Введите текст для анализа: ").strip()

    if not text:
        raise ValueError("Ошибка: нет входных данных")

    normal_text = normalize(text)
    tokens = tokenize(normal_text)
    freq = count_freq(tokens)
    top_words = top_n(freq, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    if table_mode:
        print(format_table(top_words))
    else:
        print(format_simple(top_words))


if __name__ == "__main__":
    main()
