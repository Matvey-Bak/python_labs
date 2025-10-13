import os
import sys

# Добавляем путь для импорта из lib/text.py
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.text import normalize, tokenize, count_freq, top_n

def main():
    # Получаем текст через input()
    text = input("Введите текст для анализа: ").strip()

    if not text:
        return print("Ошибка: нет входных данных")
        

    # Обрабатываем текст
    normal_text = normalize(text)
    tokens = tokenize(normal_text)
    freq = count_freq(tokens)
    top_words = top_n(freq, n=5)

    # Выводим результаты
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()