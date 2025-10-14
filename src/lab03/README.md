# Лабораторная работа №3 
## Задание A
1. normalize(text)
```python
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
```
Функция `normalize` выполняет предварительную обработку текста, подготавливая его к последующему анализу. Она приводит
весь текст к нижнему регистру и удаляет знаки препинания, обеспечивая единообразие данных. Такая стандартизация позволяет
корректно сравнивать и подсчитывать слова, исключая дублирование из-за разного регистра или наличия специальных символов, 
что значительно повышает точность лингвистического анализа.

2. tokenize(text) (в задании также использовались функции normalize and remove_emoji)
```python
def remove_emoji(text: str) -> str:
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
```
Функция `tokenize` выполняет разбиение текста на отдельные слова-токены, подготавливая данные для последующего анализа.
 Сначала она нормализует входной текст, приводя его к единому формату, а затем использует метод `split()` для разделения строки
  на список слов по пробельным символам. Такой подход обеспечивает корректную токенизацию текстовых данных, создавая 
  структурированную основу для подсчета статистики и выявления наиболее значимых лексем.

3. count_freq
```python
def count_freq(tokens: list[str]):
    count = {}
    for i in tokens:
        count[i] = count.get(i, 0) + 1
    return count
```
Функция `count_freq` выполняет подсчет частоты встречаемости слов в тексте, преобразуя список токенов в словарь частот. 
Используя метод `get()` с значением по умолчанию, она эффективно обновляет счетчики для каждого слова, избегая необходимости
проверки существования ключей. Такой подход обеспечивает точный учет статистики встречаемости лексем, формируя надежную
основу для последующего частотного анализа текстовых данных.

4. top_n
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]
```
Функция `top_n` выполняет сортировку слов по частоте встречаемости, возвращая N самых употребительных лексем.
 С помощью `sorted()` с ключом `(-x[1], x[0])` она упорядочивает элементы словаря по убыванию частоты, 
 а при равенстве частот - по алфавиту. Финальный срез `[:n]` выделяет требуемое количество наиболее частотных слов,
 обеспечивая стабильный и предсказуемый результат анализа текстовых данных.

## Задание B * 
```python
import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.text import normalize, tokenize, count_freq, top_n


TABLE_MODE = os.getenv('TABLE_MODE', 'false').lower() == 'true'

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
        raise ValueError('Ошибка: нет входных данных')

    normal_text = normalize(text)
    tokens = tokenize(normal_text)
    freq = count_freq(tokens)
    top_words = top_n(freq, n=5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    
    if TABLE_MODE:
        print(format_table(top_words))
    else:
        print(format_simple(top_words))

if __name__ == "__main__":
    main()
```
![alt text](../../images/lab_03/img04.png)


![alt text](<../../images/lab_03/Задние B hard.png>)

# Описание работы кода 

## Модуль импорта и настройки путей

**Принцип работы:**
- `os.path.dirname(__file__)` - определяет абсолютный путь к директории текущего исполняемого скрипта
- `os.path.join(..., '..')` - осуществляет переход на один уровень вверх в файловой системе (родительская директория) 
- `sys.path.append()` - добавляет вычисленный путь в системный список путей для поиска Python-модулей

**Результат:** Становится возможным импортировать функции из модуля `lib/text.py`, расположенного в соседней директории, независимо от текущего рабочего каталога.

## Блок управления режимом вывода TABLE_MODE

**Назначение:** Гибкое управление форматом отображения результатов через переменные окружения.

**Принцип работы:**
- `os.getenv('TABLE_MODE', 'false')` - получает значение переменной окружения TABLE_MODE, при отсутствии возвращает значение по умолчанию 'false'
- `.lower()` - нормализует строку к нижнему регистру, обеспечивая регистронезависимую обработку (корректно обрабатывает 'True', 'TRUE', 'tRuE' и т.д.)
- `== 'true'` - выполняет строгое сравнение с эталонным значением, возвращая булево значение

**Преимущество:** Позволяет изменять поведение программы без модификации исходного кода.

## Функция format_table()

**Назначение:** Форматированный вывод результатов в виде псевдографической таблицы с автоматическим выравниванием.

**Алгоритм работы:**
1. **Валидация данных:** Проверка наличия элементов для отображения
2. **Определение ширины столбца:**
   - Генератор списка `len(str(word)) for word, _ in top_words` вычисляет длины всех слов
   - `max()` находит максимальное значение длины
   - `max(max_word_length, 6)` гарантирует минимальную ширину 6 символов для заголовка "слово"
3. **Построение шапки таблицы:**
   - `"слово".ljust(max_word_length)` - выравнивание заголовка по левому краю
   - Формирование строки заголовка с разделителем
   - Создание разделительной линии соответствующей длины
4. **Генерация содержимого:**
   - Итерация по парам (слово, частота)
   - Выравнивание каждого слова до заданной ширины
   - Форматирование строк таблицы
   - Объединение всех элементов через `"\n".join(lines)`

## Функция format_simple()

**Назначение:** Альтернативный упрощенный формат вывода результатов.

**Принцип работы:**
- Последовательное формирование строк вида "слово: частота" для каждого элемента
- Объединение результирующих строк через символ переноса строки
- Обеспечение минималистичного и читаемого представления данных

## Функция main() - ядро программы

**Назначение:** Координация всего процесса анализа текста и управления потоком выполнения.

**Последовательность операций:**

1. **Ввод и предобработка данных:**
   - `input()` - интерактивный ввод текста от пользователя
   - `.strip()` - удаление лишних пробельных символов по краям строки

2. **Валидация входных данных:**
   - Проверка на пустую строку с генерацией исключения при нарушении

3. **Процесс анализа текста:**
   - `normalize()` - нормализация текста (приведение к единому регистру, удаление лишних символов)
   - `tokenize()` - токенизация (разбиение на отдельные слова/лексемы)
   - `count_freq()` - подсчет частоты встречаемости каждого уникального слова
   - `top_n()` - выделение N наиболее частотных элементов

4. **Вывод результатов:**
   - Отображение общей статистики (общее количество слов, количество уникальных слов)
   - Условное ветвление для выбора формата отображения топа слов на основе флага TABLE_MODE
   - Вывод результатов в выбранном формате
