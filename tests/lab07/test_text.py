import pytest  # type: ignore
import sys
import os

# Добавляем путь к src в PYTHONPATH для корректного импорта
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
src_path = os.path.join(project_root, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from lib.text import normalize, tokenize, count_freq, top_n


class TestNormalize:
    """Тесты для функции normalize"""

    @pytest.mark.parametrize(
        "input_text,expected",
        [
            ("Привет, МИР!", "привет мир"),
            ("Hello!!! World???", "hello world"),
            ("PyThOn JaVa", "python java"),
            ("ёлка Ёж", "елка еж"),
            ("", ""),
            ("   ", ""),
            ("!!!", ""),
            ("  test  string  ", "test string"),
        ],
    )
    def test_normalize_basic(self, input_text, expected):
        assert normalize(input_text) == expected

    @pytest.mark.parametrize(
        "text,casefold,yo2e,expected",
        [
            ("Привет МИР", True, True, "привет мир"),
            ("ёлка ЁЖ", True, True, "елка еж"),
            ("Test Case", True, False, "test case"),
        ],
    )
    def test_normalize_params(self, text, casefold, yo2e, expected):
        result = normalize(text, casefold=casefold, yo2e=yo2e)
        assert result == expected

    def test_normalize_special_cases(self):
        assert normalize("!!! @@@") == ""
        assert normalize("   \t\n") == ""


class TestTokenize:
    """Тесты для функции tokenize"""

    @pytest.mark.parametrize(
        "text,expected",
        [
            ("hello world", ["hello", "world"]),
            ("hello, world!", ["hello", "world"]),
            ("test123 string456", ["test123", "string456"]),
            ("", []),
            ("   ", []),
            ("!!!", []),
            ("single", ["single"]),
        ],
    )
    def test_tokenize_basic(self, text, expected):
        assert tokenize(text) == expected

    def test_tokenize_special_cases(self):
        assert tokenize("test\nstring\tdata") == ["test", "string", "data"]
        assert tokenize("Привет 世界 café") == ["привет", "世界", "café"]


class TestCountFreq:
    """Тесты для функции count_freq"""

    @pytest.mark.parametrize(
        "tokens,expected",
        [
            (["hello", "world", "hello"], {"hello": 2, "world": 1}),
            (["a", "b", "c"], {"a": 1, "b": 1, "c": 1}),
            (["word", "word"], {"word": 2}),
            ([], {}),
        ],
    )
    def test_count_freq_basic(self, tokens, expected):
        assert count_freq(tokens) == expected

    def test_count_freq_special(self):
        tokens = ["café", "café", "🚀"]
        assert count_freq(tokens) == {"café": 2, "🚀": 1}


class TestTopN:
    """Тесты для функции top_n"""

    @pytest.mark.parametrize(
        "freq,n,expected",
        [
            ({"python": 7, "hello": 5, "world": 3}, 2, [("python", 7), ("hello", 5)]),
            ({"test": 42}, 1, [("test", 42)]),
            ({}, 5, []),
            ({"a": 1, "b": 2}, 10, [("b", 2), ("a", 1)]),
        ],
    )
    def test_top_n_basic(self, freq, n, expected):
        assert top_n(freq, n) == expected

    def test_top_n_alphabetical_sort(self):
        freq = {"zebra": 5, "apple": 5, "cherry": 5}
        result = top_n(freq, 3)
        assert [word for word, _ in result] == ["apple", "cherry", "zebra"]


class TestIntegration:
    """Интеграционные тесты"""

    @pytest.mark.parametrize(
        "text,expected",
        [
            ("Hello hello world!", [("hello", 2), ("world", 1)]),
            ("Test test data", [("test", 2), ("data", 1)]),
        ],
    )
    def test_pipeline(self, text, expected):
        tokens = tokenize(text)
        freq = count_freq(tokens)
        result = top_n(freq, 3)
        assert result == expected

    def test_empty_pipeline(self):
        text = ""
        tokens = tokenize(text)
        freq = count_freq(tokens)
        result = top_n(freq, 5)
        assert result == []
