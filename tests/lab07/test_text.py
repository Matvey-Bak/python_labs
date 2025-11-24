import pytest
import re
from lib.text import normalize, tokenize, count_freq, top_n


class TestNormalize:
    """Тесты для функции normalize с приоритетом параметризации"""
    
    # ПАРАМЕТРИЗОВАННЫЕ ТЕСТЫ - ОСНОВНЫЕ СЦЕНАРИИ
    @pytest.mark.parametrize("input_text,expected", [
        # Базовые случаи
        ("Привет, МИР!", "привет мир"),
        ("Hello!!! World??? Test...", "hello world test"),
        ("PyThOn JaVa Script", "python java script"),
        ("Test123!@# String456$%^", "test123 string456"),
        ("ёлка Ёж ёжик", "елка еж ежик"),
        
        # Граничные случаи
        ("", ""),
        ("   ", ""),
        ("!!! ??? ...", ""),
        ("  test  string  ", "test string"),
        ("TEST\nDATA\tINFO", "test data info"),
        
        # Специальные символы
        ("hello\tworld\npython\rjava", "hello world python java"),
        ("hello    world   python", "hello world python"),
    ])
    def test_normalize_basic_cases(self, input_text, expected):
        """Параметризованные тесты основных сценариев"""
        assert normalize(input_text) == expected
    
    @pytest.mark.parametrize("text,casefold,yo2e,expected", [
        # Комбинации параметров
        ("Привет МИР", True, True, "привет мир"),
        ("Привет МИР", False, True, "Привет МИР"),
        ("ёлка ЁЖ", True, True, "елка еж"),
        ("ёлка ЁЖ", True, False, "ёлка ёж"),
        ("Test Case", False, False, "Test Case"),
        ("Test Case", True, False, "test case"),
        
        # Граничные случаи с параметрами
        ("", True, True, ""),
        ("!!!", False, False, "!!!"),
        ("  ё  ", False, True, "е"),
    ])
    def test_normalize_parameter_combinations(self, text, casefold, yo2e, expected):
        """Параметризованные тесты комбинаций параметров"""
        result = normalize(text, casefold=casefold, yo2e=yo2e)
        assert result == expected
    
    def test_normalize_only_special_chars(self):
        """Отдельная проверка: строка только из пунктуации"""
        text = "!!! @@@ ### $$$"
        result = normalize(text)
        expected = ""
        assert result == expected
    
    def test_normalize_only_whitespace(self):
        """Отдельная проверка: строка только из пробельных символов"""
        text = "   \t\n\r   \t\t"
        result = normalize(text)
        expected = ""
        assert result == expected
    
    def test_normalize_large_text_performance(self):
        """Отдельная проверка производительности на большом тексте"""
        large_text = "test " * 1000
        result = normalize(large_text)
        assert len(result) == len("test") * 1000 + 999
        assert result.count("  ") == 0
    
    def test_normalize_yo_replacement_comprehensive(self):
        """Отдельная проверка: все случаи замены буквы 'ё'"""
        text = "ё Ё ёё ЁЁ мёд МЁД ёлка ЁЖИК"
        result = normalize(text)
        expected = "е е ее ее мед мед елка ежик"
        assert result == expected
    
    def test_normalize_unicode_special_cases(self):
        """Отдельная проверка: специальные Unicode символы"""
        # Немецкие умлауты
        text = "Ä Ö Ü ß"
        result = normalize(text)
        expected = text.casefold()
        assert result == expected
    
    def test_normalize_input_validation(self):
        """Отдельная проверка валидации входных данных"""
        with pytest.raises(TypeError):
            normalize(None)
        with pytest.raises(TypeError):
            normalize(123)
        with pytest.raises(TypeError):
            normalize([])


class TestTokenize:
    """Тесты для функции tokenize с приоритетом параметризации"""
    
    @pytest.mark.parametrize("text,expected", [
        # Базовые случаи
        ("hello world python", ["hello", "world", "python"]),
        ("hello, world! python?", ["hello", "world", "python"]),
        ("test123 string456 data789", ["test123", "string456", "data789"]),
        ("Hello, World! Test123... Data_456", ["hello", "world", "test123", "data456"]),
        
        # Граничные случаи
        ("", []),
        ("   ", []),
        ("!!! @@@ ###", []),
        ("single", ["single"]),
        ("  hello  world  ", ["hello", "world"]),
        
        # Специальные символы и пробелы
        ("test\nstring\tdata", ["test", "string", "data"]),
        ("word1, word2! word3?", ["word1", "word2", "word3"]),
    ])
    def test_tokenize_basic_cases(self, text, expected):
        """Параметризованные тесты основных сценариев"""
        result = tokenize(text)
        assert result == expected
    

    def test_tokenize_only_punctuation(self):
        """Отдельная проверка: строка только из специальных символов"""
        text = "!!! @@@ ### $$$ %%% ^^^"
        result = tokenize(text)
        expected = []
        assert result == expected
    
    def test_tokenize_mixed_whitespace_comprehensive(self):
        """Отдельная проверка: все виды пробельных символов"""
        text = "word1\tword2\nword3\rword4\u00A0word5"
        result = tokenize(text)
        expected = ["word1", "word2", "word3", "word4", "word5"]
        assert result == expected
    
    def test_tokenize_unicode_text(self):
        """Отдельная проверка: Unicode символы"""
        text = "Привет 世界  Hello café naïve"
        result = tokenize(text)
        expected = ["привет", "世界", "hello", "café", "naïve"]
        assert result == expected
    
    def test_tokenize_large_text_performance(self):
        """Отдельная проверка производительности на большом тексте"""
        large_text = "token " * 5000
        tokens = tokenize(large_text)
        assert len(tokens) == 5000
        assert all(token == "token" for token in tokens)
    
    def test_tokenize_preserve_underscores(self):
        """Отдельная проверка: сохранение подчеркиваний"""
        text = "test_variable snake_case data_set"
        result = tokenize(text)
        expected = ["test_variable", "snake_case", "data_set"]
        assert result == expected
    
    def test_tokenize_input_validation(self):
        """Отдельная проверка валидации входных данных"""
        with pytest.raises(TypeError):
            tokenize(None)
        with pytest.raises(TypeError):
            tokenize(123)


class TestCountFreq:
    """Тесты для функции count_freq с приоритетом параметризации"""
    
    # ПАРАМЕТРИЗОВАННЫЕ ТЕСТЫ - ОСНОВНЫЕ СЦЕНАРИИ
    @pytest.mark.parametrize("tokens,expected", [
        # Базовые случаи
        (["hello", "world", "hello", "python"], {"hello": 2, "world": 1, "python": 1}),
        (["a", "b", "c", "d"], {"a": 1, "b": 1, "c": 1, "d": 1}),
        (["word", "word", "word", "word"], {"word": 4}),
        (["test"], {"test": 1}),
        
        # Граничные случаи
        ([], {}),
        (["", "word", "", "test"], {"": 2, "word": 1, "test": 1}),
        
        # Специальные случаи
        (["Hello", "hello", "HELLO"], {"Hello": 1, "hello": 1, "HELLO": 1}),
        (["café", "café", "naïve"], {"café": 2, "naïve": 1}),
    ])
    def test_count_freq_basic_cases(self, tokens, expected):
        """Параметризованные тесты основных сценариев"""
        result = count_freq(tokens)
        assert result == expected
    
    # ОТДЕЛЬНЫЕ ПРОВЕРКИ - СПЕЦИФИЧЕСКИЕ И СЛОЖНЫЕ СЛУЧАИ
    def test_count_freq_special_characters_in_tokens(self):
        """Отдельная проверка: специальные символы в токенах"""
        tokens = ["test_123", "test-456", "test.789", "var@name"]
        result = count_freq(tokens)
        expected = {"test_123": 1, "test-456": 1, "test.789": 1, "var@name": 1}
        assert result == expected
    
    def test_count_freq_unicode_comprehensive(self):
        """Отдельная проверка: комплексные Unicode случаи"""
        tokens = ["café", "café", "naïve", "café", "🚀", "🚀", "世界"]
        result = count_freq(tokens)
        expected = {"café": 3, "naïve": 1, "🚀": 2, "世界": 1}
        assert result == expected
    
    def test_count_freq_large_dataset_performance(self):
        """Отдельная проверка производительности на большом наборе данных"""
        tokens = ["word"] * 1000 + ["test"] * 500 + ["data"] * 250
        result = count_freq(tokens)
        assert result["word"] == 1000
        assert result["test"] == 500
        assert result["data"] == 250
        assert len(result) == 3
    
    def test_count_freq_preserve_order_independence(self):
        """Отдельная проверка: независимость от порядка токенов"""
        tokens1 = ["a", "b", "a", "c", "b", "a"]
        tokens2 = ["b", "a", "c", "a", "a", "b"]
        result1 = count_freq(tokens1)
        result2 = count_freq(tokens2)
        assert result1 == result2 == {"a": 3, "b": 2, "c": 1}
    
    def test_count_freq_input_validation(self):
        """Отдельная проверка валидации входных данных"""
        with pytest.raises(TypeError):
            count_freq(None)
        with pytest.raises(TypeError):
            count_freq("not a list")
        with pytest.raises(TypeError):
            count_freq([1, 2, 3])  


class TestTopN:
    
    @pytest.mark.parametrize("freq,n,expected", [
        ({"hello": 5, "world": 3, "python": 7, "java": 2}, 3, [("python", 7), ("hello", 5), ("world", 3)]),
        ({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}, 5, [("f", 6), ("e", 5), ("d", 4), ("c", 3), ("b", 2)]),
        ({"test": 42}, 1, [("test", 42)]),
        
        ({}, 5, []),
        ({"a": 1, "b": 2}, 10, [("b", 2), ("a", 1)]),
        ({"a": 1, "b": 2, "c": 3}, 0, []),
        ({"a": 1, "b": 2}, -1, []),
        
        ({"banana": 3, "apple": 3, "cherry": 3, "date": 2}, 4, [("apple", 3), ("banana", 3), ("cherry", 3), ("date", 2)]),
        ({"z": 1, "y": 2, "x": 3}, 1, [("x", 3)]),
    ])
    def test_top_n_basic_cases(self, freq, n, expected):
        """Параметризованные тесты основных сценариев"""
        result = top_n(freq, n)
        assert result == expected
    
    @pytest.mark.parametrize("freq,expected", [
        ({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}, [("f", 6), ("e", 5), ("d", 4), ("c", 3), ("b", 2)]),
        ({"single": 10}, [("single", 10)]),
        ({}, []),
    ])
    def test_top_n_default_parameter(self, freq, expected):
        """Параметризованные тесты с параметром по умолчанию"""
        result = top_n(freq)
        assert result == expected
    

    def test_top_n_complex_alphabetical_sort(self):
        """Отдельная проверка: сложная алфавитная сортировка с учетом регистра"""
        freq = {"apple": 2, "Apple": 2, "banana": 2, "Banana": 2}
        result = top_n(freq, 4)
        expected = [("Apple", 2), ("Banana", 2), ("apple", 2), ("banana", 2)]
        assert result == expected
    
    def test_top_n_preserve_order_same_frequency(self):
        """Отдельная проверка: сохранение алфавитного порядка при одинаковых частотах"""
        freq = {"zebra": 5, "apple": 5, "cherry": 5, "banana": 5}
        result = top_n(freq, 4)
        expected = [("apple", 5), ("banana", 5), ("cherry", 5), ("zebra", 5)]
        assert result == expected

        assert [word for word, freq in result] == ["apple", "banana", "cherry", "zebra"]
    
    def test_top_n_mixed_frequencies_complex_sort(self):
        """Отдельная проверка: смешанные частоты с комплексной сортировкой"""
        freq = {"delta": 1, "alpha": 3, "gamma": 1, "beta": 3, "epsilon": 2}
        result = top_n(freq, 5)
        expected = [("alpha", 3), ("beta", 3), ("epsilon", 2), ("delta", 1), ("gamma", 1)]
        assert result == expected
    
    def test_top_n_unicode_sorting(self):
        """Отдельная проверка: сортировка Unicode символов"""
        freq = {"世界": 3, "hello": 3, "café": 2, "🚀": 4}
        result = top_n(freq, 4)
        # Должны отсортироваться по частоте, а при равной - по алфавиту
        expected = [("🚀", 4), ("hello", 3), ("世界", 3), ("café", 2)]
        assert result == expected
    
    def test_top_n_stability_multiple_calls(self):
        """Отдельная проверка: стабильность при многократных вызовах"""
        freq = {"a": 1, "b": 1, "c": 1, "d": 1, "e": 1}
        
        for i in range(10):
            result = top_n(freq, 5)
            expected = [("a", 1), ("b", 1), ("c", 1), ("d", 1), ("e", 1)]
            assert result == expected
    
    def test_top_n_input_validation(self):
        """Отдельная проверка валидации входных данных"""
        with pytest.raises(TypeError):
            top_n(None, 5)
        with pytest.raises(TypeError):
            top_n("not a dict", 5)
        with pytest.raises(TypeError):
            top_n({"a": 1}, "not an int")


class TestIntegration:
    """Интеграционные тесты полного pipeline обработки текста"""
    
    @pytest.mark.parametrize("text,expected_top", [
        ("Hello hello world! World python. Python Python!", [("python", 3), ("hello", 2), ("world", 2)]),
        ("Test!!! Test... Data? Data! Info; Info: Info", [("info", 3), ("data", 2), ("test", 2)]),
        ("Café café naïve Naïve test Test", [("café", 2), ("naïve", 2), ("test", 2)]),
    ])
    def test_integration_pipeline_parametrized(self, text, expected_top):
        """Параметризованные интеграционные тесты полного pipeline"""
        tokens = tokenize(text)
        freq = count_freq(tokens)
        top_words = top_n(freq, 3)
        assert top_words == expected_top
    
    def test_integration_complex_scenario(self):
        """Отдельная проверка: сложный сценарий с mixed case и разными языками"""
        text = """
        Python python JAVA java C++ c++ 
        JavaScript javascript TypeScript typescript
        Python is great! Java is good.
        """
        tokens = tokenize(text)
        freq = count_freq(tokens)
        top_words = top_n(freq, 5)
        
        assert top_words[0][0] == "python"
        assert top_words[0][1] == 3
        assert "java" in [word for word, freq in top_words]
    
    def test_integration_empty_text(self):
        """Отдельная проверка: пустой текст через весь pipeline"""
        text = ""
        tokens = tokenize(text)
        freq = count_freq(tokens)
        top_words = top_n(freq, 5)
        
        assert tokens == []
        assert freq == {}
        assert top_words == []
    
    def test_integration_special_characters_only(self):
        """Отдельная проверка: текст только из специальных символов"""
        text = "!!! @@@ ### $$$ %%% ^^^ &&&"
        tokens = tokenize(text)
        freq = count_freq(tokens)
        top_words = top_n(freq, 5)
        
        assert tokens == []
        assert freq == {}
        assert top_words == []