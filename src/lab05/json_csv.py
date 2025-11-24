import json
import csv
from pathlib import Path
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

"""
Функция для преобразования формта данных json в csv 
"""


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразуем в объект Path для удобной работы с путями
    и проверяем существует ли данный путь если такого пути нет выводится ошибка
    """
    json_file = Path(json_path)
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")

    """
    Проверяем что формат данных json приводя к нижнему регистру для избежания ошибок 
    """
    if json_file.suffix.lower() != ".json":
        raise ValueError(
            f"Неверный тип файла: ожидается .json, получен {json_file.suffix}"
        )

    """
    В блоке try считываем файл и обрабатываем типы данных для Python
    """
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка парсинга JSON: {e}")

    """
    С помощью данных проверок смотрим что в data лежит список, файл не пустой и все элементы списка являются словарями
    """
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")

    if len(data) == 0:
        raise ValueError("JSON файл пуст")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    """
    Так как мы делаем обработку в CSV нам нужно записать все возможные названия столбцов 
    """
    all_fields = set()
    for item in data:
        all_fields.update(item.keys())

    """
    В данном блоке мы проверяем что в dara что то лежит после
    в переменную записываем все ключи от первого элемента data
    далее из всех полей которые мы нашли в предыдущем блоке вычитаем поля первого элемента
    благодаря этому мы находим какие поля нужно добавить после чего складывем их
    в else есди у нас нет данных просто сортируем в алфавитном порядке
    """
    if len(data) > 0:
        first_item_fields = list(data[0].keys())
        remaining_fields = sorted(all_fields - set(first_item_fields))
        fieldnames = first_item_fields + remaining_fields

    else:
        fieldnames = sorted(all_fields)

    """
    Открываем файл и перезаписываем таким образом в строке
    write = ... сопоставляем ключ и пишем его значение после записычаем заголовок
    далее мы создаем строки и заполняем их после этого записываем строку 
    """
    try:
        with open(csv_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()

            for row in data:
                complete_row = {field: row.get(field, "") for field in fieldnames}
                writer.writerow(complete_row)

    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:

    csv_file = Path(csv_path)
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")

    if csv_file.suffix.lower() != ".csv":
        raise ValueError(
            f"Неверный тип файла: ожидается .csv, получен {csv_file.suffix}"
        )

    try:
        with open(csv_path, "r", encoding="utf-8") as f:
            """
            Преобразует каждую строку в CSV словарь
            """
            reader = csv.DictReader(f)

            """
            Если в файлк только строки без заголовков то вызываем ошибку
            """
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовка")

            """
            Здесь наоборот если только заголовок
            """
            data = list(reader)
            if len(data) == 0:
                raise ValueError("CSV файл пуст (только заголовок)")

    except csv.Error as e:
        raise ValueError(f"Ошибка парсинга CSV: {e}")

    """
    Записываем объекст в формате Python в файл формата json также 
    с помощью команды ensure_ascii=False не переводи в Юникод чтоб сохранился читаемый вид
    еще есть такая команда как indent=2 она отвечаетза красивое форматирование с отступами
    """
    try:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")


json_to_csv(
    r"python_labs\data\lab05\samples\FIO.json",
    r"python_labs\data\lab05\out\FIO from json.csv",
)
csv_to_json(
    r"python_labs\data\lab05\samples\Country.csv",
    r"python_labs\data\lab05\out\Country from csv.json",
)
csv_to_json(
    r"python_labs\data\lab05\samples\no_header.csv",
    r"python_labs\data\lab05\out\n0_header_from_csv.json",
)
json_to_csv(
    r"python_labs\data\lab05\samples\game_json to csv.json",
    r"python_labs\data\lab05\out\game_from json to csv.csv",
)
