from dataclasses import dataclass
from datetime import datetime, date
from typing import Dict, Any
import re

@dataclass
class Student:
    """
    Класс для представления студента.
    
    Поля:
    - fio: ФИО студента (строка)
    - birthdate: Дата рождения в формате YYYY-MM-DD (строка)  
    - group: Группа (строка)
    - gpa: Средний балл от 0 до 5 (число с плавающей точкой)
    """
    
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        """
        Валидация данных после инициализации.
        Вызывается автоматически после конструктора.
        """
        self._validate_birthdate()
        self._validate_gpa()

    def _validate_birthdate(self):
        """Проверка корректности формата даты YYYY-MM-DD"""
        # Проверка формата с помощью регулярного выражения
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(date_pattern, self.birthdate):
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Ожидается: YYYY-MM-DD")
        
        # Проверка, что дата действительно существует
        try:
            year, month, day = map(int, self.birthdate.split('-'))
            datetime(year, month, day)
        except ValueError as e:
            raise ValueError(f"Некорректная дата: {self.birthdate}. Ошибка: {e}")

    def _validate_gpa(self):
        """Проверка диапазона GPA (0-5)"""
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"GPA должен быть в диапазоне от 0 до 5, получено: {self.gpa}")

    def age(self) -> int:
        """
        Возвращает количество полных лет студента.
        
        Returns:
            int: количество полных лет
        """
        # Преобразуем строку в объект datetime
        birth_date = datetime.strptime(self.birthdate, '%Y-%m-%d').date()
        today = date.today()
        
        # Вычисляем возраст
        age = today.year - birth_date.year
        
        # Корректируем, если день рождения в этом году еще не наступил
        if today < birth_date.replace(year=today.year):
            age -= 1
        
        return age

    def to_dict(self) -> Dict[str, Any]:
        """
        Сериализация объекта в словарь.
        
        Returns:
            dict: словарь с данными студента
        """
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student':
        """
        Десериализация объекта из словаря.
        
        Args:
            data: словарь с данными студента
            
        Returns:
            Student: новый объект Student
        """
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )

    def __str__(self) -> str:
        """
        Красивое строковое представление объекта.
        
        Returns:
            str: отформатированная строка с информацией о студенте
        """
        return f"{self.fio}, {self.group}, GPA: {self.gpa:.2f}, Возраст: {self.age()} лет"


if __name__ == "__main__":
    print("=== Демонстрация работы класса Student ===\n")
    

if __name__ == "__main__":
    student = Student(
        fio="Иванов Иван",
        birthdate="2000-05-15",
        group="SE-01",
        gpa=4.5
    )
    
    print(student)
    print(student.to_dict())