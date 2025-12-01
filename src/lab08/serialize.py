import json
from typing import List
from models import Student


def students_to_json(students: List[Student], path: str) -> None:
    data = [student.to_dict() for student in students]
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Данные успешно сохранены в {path}")


def students_from_json(path: str) -> List[Student]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if not isinstance(data, list):
            raise ValueError("JSON должен содержать массив объектов")
        
        students = []
        for i, item in enumerate(data):
            try:
                if not isinstance(item, dict):
                    raise ValueError(f"Элемент {i} должен быть словарем, а не {type(item).__name__}")
                
                required_fields = ['fio', 'birthdate', 'group', 'gpa']
                for field in required_fields:
                    if field not in item:
                        raise ValueError(f"Отсутствует обязательное поле '{field}' в элементе {i}")
                
                student = Student.from_dict(item)
                students.append(student)
                
            except ValueError as e:
                print(f"Ошибка валидации элемента {i}: {e}")
                raise
            except Exception as e:
                print(f"Неожиданная ошибка при обработке элемента {i}: {e}")
                raise
        
        print(f"Успешно загружено {len(students)} студентов из {path}")
        return students
        
    except FileNotFoundError:
        print(f"Ошибка: файл {path} не найден")
        raise

if __name__ == "__main__":
    students = students_from_json("python_labs/data/lab08/students_input.json")
    print("Загружено студентов:", len(students))
    for student in students:
        print(student)
    

    students = sorted(students, key=lambda s: s.gpa, reverse=True)
    
    output = "python_labs/data/lab08/students_output.json"
    students_to_json(students, output)
    print(f"\nСтуденты сохранены в {output}")