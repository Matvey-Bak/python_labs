<<<<<<< HEAD
# python_labs
# Лабораторная работа №1 
 Задание №1
```python
Name = input()
Age = int(input())
print("Привет,", Name + "!" ,"Через год тебе будет", Age + 1, end = ".")
```
![alt text](<images/lab_01/Задание №1.png>)

 Задание №2
```python
a = input()
b = input()
a = a.replace(",",".",1)
b = b.replace(",",".",1)
a = float(a)
b = float(b)
sum = a + b
avg = (a + b)/2
print(f"{sum:.2f}")
print(f"{avg:.2f}")
```
![alt text](images/lab_01/ex02.2.png)
 Задание №3
```python
price = float(input())
discount = float(input())
vat = float(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print("База после скидки:",f"{base:.2f} ₽")
print("НДС:",f"{vat_amount:.2f} ₽")
print("Итого к оплате:",f"{total:.2f} ₽")
```
![alt text](images/lab_01/ex03.2.png)
 Задание №4
```python
minutes = int(input())
print(minutes // 60, ":",minutes % 60, sep = "")
```
![alt text](images/lab_01/ex04.png)
 Задание №5
```python
FIO = input()
k = 0
b = []
c = []
x = []
t = len(FIO)
for i in FIO:
    if i == " ":
        k = k + 1

if k != 2:
    t = t - k + 2

a = FIO.split()

b.append(a[0])
c.append(a[1])
x.append(a[2])

q = b[0]
w = c[0]
e = x[0]
print("Инициалы:", q[0], w[0], e[0],sep="")
print("Длина символов:", t)
```
![alt text](images/lab_01/ex05.2.png)

 Задание №7 
```python
a = "thisisabracadabraHt1eadljjl12ojh."
index1 = 0
for j in range(0, len(a)):
    for i in "QWERTYUIOPASDFGHJKLZXCVBNM":
        if a[j] == i:
            index1 = j
            break

index2 = 0
for c in range(0, len(a) - 1):
    if (a[c] in "0123456789") and ((a[c + 1] in "qwertyuiopasdfghjklzxcvbnm") or (a[c + 1] in "QWERTYUIOPASDFGHJKLZXCVBNM")):
        index2 = c
        break

razn = abs(index1 - index2) + 1
g = a[index1::]
m= ""
for k in range(0, len(g), razn):
    m += g[k]
print(m)
```
![alt text](images/lab_01/ex07.png)


# Лабораторная работа №2
 Задание №1
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise TypeError
    else:
        return min(nums), max(nums)

print(min_max([3, -1, 5, 5, 0]))
print(min_max([]))
print(min_max([-5, -2, -9]))
```
![alt text](images/lab_02/ex01.png)

 Задание №2
``` python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    if len(nums) == 0:
        return nums
    else:
        mnojestvo = set(nums)
        mnojestvo = sorted(mnojestvo)
        return mnojestvo
    
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
```
![alt text](images/lab_02/ex02.png)

Задание №3
```python
def flatten(mat: list[list | tuple]) -> list:
    sp = []
    for i in mat:
        if not isinstance(i, (list, tuple)):
            raise TypeError ("Ошибка в типе данных")
        else:
            sp.extend(i)    
    return sp

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![alt text](images/lab_02/ex03.png)

Задание №4
```python
def transpose(mat: list[list[float | int]]):
    if len(mat) == 0:
        return []
    
    dlina = len(mat[0])
    for i in range(0, len(mat)):
        if dlina != len(mat[i]):
            raise TypeError ("Длина не совпадает")
        
    col_strok = len(mat)
    col_stolb = len(mat[0])

    novaimatr = []

    for index_stolb in range(col_stolb):
        nov_strok = []
        for index_strok in range(col_strok):
            nov_strok.append(mat[index_strok][index_stolb])
        novaimatr.append(nov_strok)

    return novaimatr

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
```
![alt text](images/lab_02/ex04.png)

Задание №5
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    dlina = len(mat[0])
    for i in range(0, len(mat)):
        if dlina != len(mat[i]):
            raise TypeError ("Длина не совпадает")
        
    summi = []
    for j in range(0, len(mat)):
        summi.append(sum(mat[j]))

    return summi

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
```
![alt text](images/lab_02/ex05.png)

Задание №6
```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    dlina = len(mat[0])
    for i in range(0, len(mat)):
        if dlina != len(mat[i]):
            raise TypeError ("Длина не совпадает")
    
    sp = []
    for index_stolb in range(len(mat[0])):
        summa = 0
        for riad in mat:
            summa += riad[index_stolb]
        
        sp.append(summa)

    return sp


print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))

```
![alt text](images/lab_02/ex06.png)

Задание №7
```python
def format_record(rec: tuple[str, str, float]):
    if len(rec) == 3 and isinstance(rec, tuple):

        name, group, eval = rec

        if not isinstance(name, str):
            raise TypeError ("Ошибка в записи ФИО")
        if not isinstance(group, str):
            raise TypeError ("Ошибка в записи группы")
        if not isinstance(eval, float):
            raise TypeError ("Ошибка в записи типа GPA")
        
        clean_name = " ".join(name.strip().split())
        parts_initialos = clean_name.split()
        familia = parts_initialos[0].title()
        initiale = ".".join(first[0].upper() for first in parts_initialos[1:]) + '.'

        new_group = group.strip()

        new_eval = f"{eval:.2f}"

        itog = f"{familia} {initiale}, гр. {new_group}, GPA {new_eval}" 

        return itog
    
    else:
        raise TypeError ("Некорректные записи (пустое ФИО, пустая группа, неверный тип GPA")

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(format_record(("Иванов Иван Иванович", "BIVT-25", "4.6")))
print(format_record(( "BIVT-25", 4.6)))





```
![alt text](images/lab_02/ex07.02.png)

# Лабораторная работа №3
Задание №1 normalize
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
    
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```
![alt text](images/lab_03/img01.png)

Задание №2 tokenize
```python
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
```

![alt text](images/lab_03/img02.png)

Задание №3 count_freq and top_n
```python
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
```
![alt text](images/lab_03/img03.png)

Задание № B *
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
![alt text](images/lab_03/img04.png)


![alt text](<images/lab_03/Задние B hard.png>)
