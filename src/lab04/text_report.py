import csv
from pathlib import Path
from lib.text import normalize, tokenize, count_freq, top_n
import sys
import os


def write_csv_report(sorted_words: list[tuple[str, int]], output_path: str | Path):
     path_obj = Path(output_path)
     path_obj.parent.mkdir(parents=True, exist_ok=True)

     with open(path_obj, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['word', 'count'])
        
        for word, count in sorted_words:
            writer.writerow([word, count])

def main():
     if len(sys.argv) > 1:
        input_file = Path(sys.argv[1])
     else:
        input_file = Path(r"C:\Users\User\Desktop\Proga\python_labs\data\input.txt")
    
     output_file = Path(r"C:\Users\User\Desktop\Proga\python_labs\data\report.csv")
    
     try:
        # 1. Читаем входной файл
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # 2. Нормализуем текст
        normalized_text = normalize(text)
        
        # 3. Токенизируем
        tokens = tokenize(normalized_text)
        total_words = len(tokens)
        
        # 4. Считаем частоты
        frequencies = count_freq(tokens)
        unique_words = len(frequencies)
        
        # 5. Сортируем слова для CSV отчета
        sorted_words = top_n(frequencies, 5)
        
        
        # 6. Сохраняем отчет в CSV
        write_csv_report(sorted_words, output_file)
        
        # 7. Печатаем резюме в консоль
        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for i, (word, count) in enumerate(sorted_words, 1):
            print(f"  {i}. '{word}' - {count} раз(а)")
        
        
     except FileNotFoundError:
        print(f"Ошибка: Файл {input_file} не найден!")
        print("Убедитесь, что файл существует по указанному пути.")
        sys.exit(1)

     except Exception:
        print(f"Произошла ошибка: {Exception}")
        sys.exit(1)


if __name__ == "__main__":
    main()