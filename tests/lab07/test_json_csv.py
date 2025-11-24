import pytest  # type: ignore
import json
import csv
from pathlib import Path
import sys
import os

# Добавляем путь к src в PYTHONPATH для корректного импорта
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from lib.text import json_to_csv, csv_to_json


class TestJsonToCsv:
    @pytest.mark.parametrize(
        "data,expected_count",
        [
            ([{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}], 2),
            ([{"id": 1, "value": "test"}], 1),
            ([], 0),
        ],
    )
    def test_json_to_csv_basic(self, tmp_path, data, expected_count):
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "output.csv"

        with open(json_file, "w") as f:
            json.dump(data, f)

        json_to_csv(str(json_file), str(csv_file))

        assert csv_file.exists()
        with open(csv_file, "r") as f:
            reader = csv.DictReader(f)
            assert len(list(reader)) == expected_count


class TestCsvToJson:
    @pytest.mark.parametrize(
        "rows,expected_count",
        [
            ([{"name": "Alice", "age": "25"}, {"name": "Bob", "age": "30"}], 2),
            ([{"id": "1", "value": "test"}], 1),
            ([], 0),
        ],
    )
    def test_csv_to_json_basic(self, tmp_path, rows, expected_count):
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "output.json"

        with open(csv_file, "w", newline="") as f:
            if rows:
                writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                writer.writeheader()
                writer.writerows(rows)

        csv_to_json(str(csv_file), str(json_file))

        assert json_file.exists()
        with open(json_file, "r") as f:
            data = json.load(f)
            assert len(data) == expected_count


class TestIntegration:
    def test_roundtrip_conversion(self, tmp_path):
        original_data = [
            {"name": "Test", "value": "42"},
            {"name": "Demo", "value": "100"},
        ]

        json1 = tmp_path / "original.json"
        csv_file = tmp_path / "converted.csv"
        json2 = tmp_path / "restored.json"

        with open(json1, "w") as f:
            json.dump(original_data, f)

        json_to_csv(str(json1), str(csv_file))
        csv_to_json(str(csv_file), str(json2))

        with open(json2, "r") as f:
            restored_data = json.load(f)

        assert len(restored_data) == len(original_data)
        assert restored_data[0]["name"] == original_data[0]["name"]
