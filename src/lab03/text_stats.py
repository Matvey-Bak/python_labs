import os
import sys

'''
-С помощью os.path.dirname(__file__) получаем путь к дериктории текущего скрипта.
-Благодаря os.path.join(..., '..') переходим на уровень выше то есть в родительскую директорию
-Последним действие в данном блоке идет sys.path.append() данная функция добавляет 
этот путь в список путей для импорта модулей
-Все это вместе позволяет импортировать функции которые лежат в lib/text.py даже 
если он находится в другой директории
'''
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.text import normalize, tokenize, count_freq, top_n

'''
Работа блока с TABLE
-Функция os.getenv('TABLE_MODE', 'false') считывает переменную окружения TABLE_MODE
если переменная не установлена возвращает false
-Приводим все к нижнему регистру с помощью lower() для того чтобы код
 не выдавал ошибку если в строке появится true но не в обычном виде 
 Например: TRUE, TRue, tRuE и тд
-В коце сравнивем с true
'''
TABLE_MODE = os.getenv('TABLE_MODE', 'false').lower() == 'true'


'''
Работаем с блоком format_table
-Сначала с помощью проверки посмотрим есть ли данные
-С помощью генератора len(str(word)) for word, _ in top_words 
создаем список для длин всех слов
 и узнаем максимальную длину слова
- Благодря функции max(max_word_length, 6) гаранитируем что длина максимального слова
 будет не менее 6 символов

Создаем первую строчку таблицы
-Выравниваем по левому краю дополняя пробелами пока не достигнет нужной ширины
-Создаем строку для заголовка
-Создаем разделительную строку которая будет на 2 символа больше заголовка 

Собираем все вместе
- Функция lines = [header, separator] будет начинаь список строк с заголовка
 и разделителя
-В цикле пары вида (слово, частота) преобразуются в строку и выравниваются далее
форматируем строки и объединяем все строки ерез перевод строки 
'''
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


'''
Работаем с блоком format_simple()
-Данный блок несет идею прошлого но здесь мы не будем подводить все 
к виду красивой таблицы
-В данном блоке мы создаем список строк вида 'слово: частота' и объединяем 
через перевод строки
'''
def format_simple(top_words):
    lines = []
    for word, count in top_words:
        lines.append(f"{word}: {count}")
    return "\n".join(lines)

'''
Работаем с блоком main()
-С помощью input() вводим текст с котрым будет работать программа и с помощью strip() 
удаляем лишние пробелы в начале и конце
-После проверяем не пустой ли ввод
-Выполняем функции из  lib
-Далее в зависимости от результата проверки делаем вывод
'''

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