import pytest
import json
import csv
from pathlib import Path


from lib.text import json_to_csv, csv_to_json

class TestJsonToCsv:
    """Тесты для функции json_to_csv"""
    
    def test_json_to_csv_correct_conversion(self, tmp_path):
        """Позитивный сценарий: корректная конвертация JSON → CSV"""
        # Создаем тестовый JSON файл
        json_data = [
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"},
            {"name": "Charlie", "age": 35, "city": "Kazan"}
        ]
        
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "output.csv"
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False)
        
        # Выполняем конвертацию
        json_to_csv(str(json_file), str(csv_file))
        
        # Проверяем результат
        assert csv_file.exists()
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
        # Проверяем количество записей
        assert len(rows) == len(json_data)
        
        # Проверяем набор ключей/заголовков
        expected_fields = {"name", "age", "city"}
        assert set(rows[0].keys()) == expected_fields
        
        # Проверяем данные
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "25"
        assert rows[0]["city"] == "Moscow"

    def test_json_to_csv_different_field_order(self, tmp_path):
        """Позитивный сценарий: JSON с разным порядком полей"""
        json_data = [
            {"name": "Alice", "age": 25},
            {"age": 30, "name": "Bob", "city": "SPb"},
            {"city": "Kazan", "name": "Charlie", "age": 35}
        ]
        
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "output.csv"
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False)
        
        json_to_csv(str(json_file), str(csv_file))
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
        # Все поля должны присутствовать
        assert set(rows[0].keys()) == {"name", "age", "city"}
        assert len(rows) == 3

    def test_json_to_csv_empty_list(self, tmp_path):
        """Негативный сценарий: пустой JSON файл"""
        json_file = tmp_path / "empty.json"
        csv_file = tmp_path / "output.csv"
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump([], f)
        
        with pytest.raises(ValueError, match="JSON файл пуст"):
            json_to_csv(str(json_file), str(csv_file))

    def test_json_to_csv_invalid_json(self, tmp_path):
        """Негативный сценарий: некорректный JSON"""
        json_file = tmp_path / "invalid.json"
        csv_file = tmp_path / "output.csv"
        
        with open(json_file, 'w', encoding='utf-8') as f:
            f.write('{"invalid": json}')
        
        with pytest.raises(ValueError, match="Ошибка парсинга JSON"):
            json_to_csv(str(json_file), str(csv_file))

    def test_json_to_csv_not_list(self, tmp_path):
        """Негативный сценарий: JSON не является списком"""
        json_file = tmp_path / "not_list.json"
        csv_file = tmp_path / "output.csv"
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump({"not": "a list"}, f)
        
        with pytest.raises(ValueError, match="JSON должен содержать список объектов"):
            json_to_csv(str(json_file), str(csv_file))

    def test_json_to_csv_mixed_types(self, tmp_path):
        """Негативный сценарий: смешанные типы в JSON"""
        json_data = [{"name": "Alice"}, "not a dict", 123]
        
        json_file = tmp_path / "mixed.json"
        csv_file = tmp_path / "output.csv"
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f)
        
        with pytest.raises(ValueError, match="Все элементы JSON должны быть словарями"):
            json_to_csv(str(json_file), str(csv_file))

    def test_json_to_csv_file_not_found(self, tmp_path):
        """Негативный сценарий: файл не существует"""
        json_file = tmp_path / "nonexistent.json"
        csv_file = tmp_path / "output.csv"
        
        with pytest.raises(FileNotFoundError, match="JSON файл не найден"):
            json_to_csv(str(json_file), str(csv_file))

    def test_json_to_csv_wrong_extension(self, tmp_path):
        """Негативный сценарий: неверное расширение файла"""
        txt_file = tmp_path / "test.txt"
        csv_file = tmp_path / "output.csv"
        
        txt_file.write_text('{"test": "data"}')
        
        with pytest.raises(ValueError, match="Неверный тип файла: ожидается .json"):
            json_to_csv(str(txt_file), str(csv_file))


class TestCsvToJson:
    """Тесты для функции csv_to_json"""
    
    def test_csv_to_json_correct_conversion(self, tmp_path):
        """Позитивный сценарий: корректная конвертация CSV → JSON"""
        # Создаем тестовый CSV файл
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "output.json"
        
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
            writer.writeheader()
            writer.writerow({"name": "Alice", "age": "25", "city": "Moscow"})
            writer.writerow({"name": "Bob", "age": "30", "city": "SPb"})
            writer.writerow({"name": "Charlie", "age": "35", "city": "Kazan"})
        
        # Выполняем конвертацию
        csv_to_json(str(csv_file), str(json_file))
        
        # Проверяем результат
        assert json_file.exists()
        
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Проверяем количество записей
        assert len(data) == 3
        
        # Проверяем набор ключей
        expected_fields = {"name", "age", "city"}
        assert set(data[0].keys()) == expected_fields
        
        # Проверяем данные
        assert data[0]["name"] == "Alice"
        assert data[0]["age"] == "25"
        assert data[0]["city"] == "Moscow"

    def test_csv_to_json_empty_file(self, tmp_path):
        """Негативный сценарий: пустой CSV файл"""
        csv_file = tmp_path / "empty.csv"
        json_file = tmp_path / "output.json"
        
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            pass
        
        with pytest.raises(ValueError, match="CSV файл не содержит заголовка"):
            csv_to_json(str(csv_file), str(json_file))

    def test_csv_to_json_only_header(self, tmp_path):
        """Негативный сценарий: CSV только с заголовком"""
        csv_file = tmp_path / "header_only.csv"
        json_file = tmp_path / "output.json"
        
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["name", "age", "city"])
        
        with pytest.raises(ValueError, match="CSV файл пуст"):
            csv_to_json(str(csv_file), str(json_file))

    def test_csv_to_json_invalid_csv(self, tmp_path):
        """Негативный сценарий: некорректный CSV"""
        csv_file = tmp_path / "invalid.csv"
        json_file = tmp_path / "output.json"
        
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            f.write('"name","age\n"Alice","25"')  # Незакрытые кавычки
        
        with pytest.raises(ValueError, match="Ошибка парсинга CSV"):
            csv_to_json(str(csv_file), str(json_file))

    def test_csv_to_json_file_not_found(self, tmp_path):
        """Негативный сценарий: файл не существует"""
        csv_file = tmp_path / "nonexistent.csv"
        json_file = tmp_path / "output.json"
        
        with pytest.raises(FileNotFoundError, match="CSV файл не найден"):
            csv_to_json(str(csv_file), str(json_file))

    def test_csv_to_json_wrong_extension(self, tmp_path):
        """Негативный сценарий: неверное расширение файла"""
        txt_file = tmp_path / "test.txt"
        json_file = tmp_path / "output.json"
        
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write("name,age\nAlice,25\n")
        
        with pytest.raises(ValueError, match="Неверный тип файла: ожидается .csv"):
            csv_to_json(str(txt_file), str(json_file))


class TestIntegrationJsonCsv:
    """Интеграционные тесты для полного цикла JSON ↔ CSV"""
    
    def test_json_csv_round_trip(self, tmp_path):
        """Полный цикл: JSON → CSV → JSON"""
        # Исходные данные
        original_data = [
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"},
            {"name": "Charlie", "age": 35, "city": "Kazan", "country": "Russia"}
        ]
        
        # JSON → CSV
        json_file1 = tmp_path / "original.json"
        csv_file = tmp_path / "converted.csv"
        json_file2 = tmp_path / "final.json"
        
        with open(json_file1, 'w', encoding='utf-8') as f:
            json.dump(original_data, f, ensure_ascii=False)
        
        json_to_csv(str(json_file1), str(csv_file))
        
        # CSV → JSON
        csv_to_json(str(csv_file), str(json_file2))
        
        # Проверяем, что данные сохранились
        with open(json_file2, 'r', encoding='utf-8') as f:
            final_data = json.load(f)
        
        # Проверяем количество записей
        assert len(final_data) == len(original_data)
        
        # Проверяем, что все поля присутствуют
        all_fields = set()
        for item in final_data:
            all_fields.update(item.keys())
        
        expected_fields = {"name", "age", "city", "country"}
        assert all_fields == expected_fields
        
        # Проверяем значения
        assert final_data[0]["name"] == "Alice"
        assert final_data[0]["age"] == "25"  # CSV сохраняет как строки
        assert final_data[0]["city"] == "Moscow"

    def test_csv_json_round_trip(self, tmp_path):
        """Полный цикл: CSV → JSON → CSV"""
        # Исходные данные
        csv_file1 = tmp_path / "original.csv"
        json_file = tmp_path / "converted.json"
        csv_file2 = tmp_path / "final.csv"
        
        # Создаем исходный CSV
        with open(csv_file1, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
            writer.writeheader()
            writer.writerow({"name": "Alice", "age": "25", "city": "Moscow"})
            writer.writerow({"name": "Bob", "age": "30", "city": "SPb"})
        
        # CSV → JSON
        csv_to_json(str(csv_file1), str(json_file))
        
        # JSON → CSV
        json_to_csv(str(json_file), str(csv_file2))
        
        # Проверяем, что данные сохранились
        with open(csv_file2, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            final_data = list(reader)
        
        # Проверяем количество записей
        assert len(final_data) == 2
        
        # Проверяем заголовки
        assert set(final_data[0].keys()) == {"name", "age", "city"}
        
        # Проверяем значения
        assert final_data[0]["name"] == "Alice"
        assert final_data[0]["age"] == "25"
        assert final_data[0]["city"] == "Moscow"


class TestEdgeCases:
    """Тесты граничных случаев"""
    
    def test_json_to_csv_special_characters(self, tmp_path):
        """Специальные символы и Unicode в JSON"""
        json_data = [
            {"name": "Анна", "message": "Hello, 世界! 🌍", "price": "100€"}
        ]
        
        json_file = tmp_path / "unicode.json"
        csv_file = tmp_path / "output.csv"
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False)
        
        json_to_csv(str(json_file), str(csv_file))
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
        assert rows[0]["name"] == "Анна"
        assert rows[0]["message"] == "Hello, 世界! 🌍"
        assert rows[0]["price"] == "100€"

    def test_csv_to_json_empty_values(self, tmp_path):
        """Пустые значения в CSV"""
        csv_file = tmp_path / "empty_values.csv"
        json_file = tmp_path / "output.json"
        
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
            writer.writeheader()
            writer.writerow({"name": "Alice", "age": "", "city": "Moscow"})
            writer.writerow({"name": "", "age": "30", "city": ""})
        
        csv_to_json(str(csv_file), str(json_file))
        
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        assert data[0]["age"] == ""
        assert data[1]["name"] == ""
        assert data[1]["city"] == ""

    def test_json_to_csv_large_dataset(self, tmp_path):
        """Большой набор данных"""
        json_data = [{"id": i, "value": f"test_{i}"} for i in range(1000)]
        
        json_file = tmp_path / "large.json"
        csv_file = tmp_path / "output.csv"
        
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f)
        
        json_to_csv(str(json_file), str(csv_file))
        
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            
        assert len(rows) == 1000
        assert rows[999]["id"] == "999"
        assert rows[999]["value"] == "test_999"