import csv
from pathlib import Path
from models import Student
from top_n import top_n

class Group:
    def __init__(self, storage_path: str):
        """Инициализация группы и файла-хранилища."""
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self):
        """Создать файл с заголовком, если его ещё нет."""
        if not self.path.exists() or self.path.stat().st_size == 0:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
                writer.writeheader()

    def _read_all(self) -> list[dict]:
        """Прочитать все строки из CSV и вернуть список словарей."""
        rows = []
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                # Пропускаем пустые строки
                for row in reader:
                    if any(row.values()):  # Проверяем, что строка не пустая
                        rows.append(row)
        except FileNotFoundError:
            pass  # Файл будет создан при первой записи
        return rows

    def list(self) -> list[Student]:
        """Вернуть всех студентов в виде списка объектов Student."""
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                # Преобразуем строку в объект Student
                student = Student(
                    fio=row['fio'],
                    birthdate=row['birthdate'],
                    group=row['group'],
                    gpa=float(row['gpa'])
                )
                students.append(student)
            except (ValueError, KeyError) as e:
                # Пропускаем некорректные строки с предупреждением
                print(f"Warning: Skipping invalid row: {row} - {e}")
                continue
        return students

    def add(self, student: Student):
        """Добавить нового студента в CSV."""
        # Сначала читаем существующие данные
        rows = self._read_all()
        
        # Проверяем, нет ли уже студента с таким ФИО
        for row in rows:
            if row['fio'] == student.fio:
                raise ValueError(f"Student with fio '{student.fio}' already exists")
        
        # Добавляем нового студента
        new_row = {
            'fio': student.fio,
            'birthdate': student.birthdate,
            'group': student.group,
            'gpa': str(student.gpa)
        }
        rows.append(new_row)
        
        # Записываем все данные обратно
        self._write_all(rows)

    def find(self, substr: str):
        """Найти студентов по подстроке в fio (регистронезависимый поиск)."""
        rows = self._read_all()
        # Регистронезависимый поиск
        substr_lower = substr.lower()
        matching_rows = [r for r in rows if substr_lower in r["fio"].lower()]
        
        # Преобразуем в объекты Student
        students = []
        for row in matching_rows:
            try:
                student = Student(
                    fio=row['fio'],
                    birthdate=row['birthdate'],
                    group=row['group'],
                    gpa=float(row['gpa'])
                )
                students.append(student)
            except (ValueError, KeyError):
                continue
        return students

    def remove(self, fio: str):
        """Удалить запись(и) с данным fio (точное совпадение)."""
        rows = self._read_all()
        initial_count = len(rows)
        
        # Удаляем все записи с указанным ФИО
        rows = [r for r in rows if r["fio"] != fio]
        
        # Если что-то изменилось, записываем обратно
        if len(rows) != initial_count:
            self._write_all(rows)
            return True
        return False

    def update(self, fio: str, **fields):
        """Обновить поля существующего студента."""
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row["fio"] == fio:
                # Обновляем только разрешенные поля
                allowed_fields = {'fio', 'birthdate', 'group', 'gpa'}
                for field, value in fields.items():
                    if field in allowed_fields:
                        if field == 'gpa':
                            row[field] = str(value)  # GPA как строка
                        else:
                            row[field] = value
                updated = True
        
        if updated:
            self._write_all(rows)
        return updated

    def _write_all(self, rows):
        """Записать все строки в CSV."""
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(rows)
    
    def clear(self):
        """Очистить файл (оставить только заголовок)."""
        self._write_all([])
    
    def count(self) -> int:
        """Количество студентов в группе."""
        return len(self._read_all())
    
    def get_by_fio(self, fio: str) -> Student | None:
        """Получить студента по точному ФИО."""
        rows = self._read_all()
        for row in rows:
            if row['fio'] == fio:
                try:
                    return Student(
                        fio=row['fio'],
                        birthdate=row['birthdate'],
                        group=row['group'],
                        gpa=float(row['gpa'])
                    )
                except (ValueError, KeyError):
                    return None
        return None

    def stats(self) -> dict:
        students = self.list()
        # Если нет студентов, возвращаем пустую статистику
        if not students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5_students": []
            }
        
        # 1. Основные статистики GPA
        gpa_values = [s.gpa for s in students]
        count = len(students)
        min_gpa = min(gpa_values)
        max_gpa = max(gpa_values)
        avg_gpa = sum(gpa_values) / count
        
        groups_dict = {}
        for student in students:
            group_name = student.group
            groups_dict[group_name] = groups_dict.get(group_name, 0) + 1
        
        student_gpa_dict = {s.fio: int(s.gpa * 100) for s in students} 
        
        # Получаем топ-5 студентов по GPA
        top_5_tuples = top_n(student_gpa_dict, 5)
        
        top_5_list = [
            {"fio": fio, "gpa": gpa / 100.0}  
            for fio, gpa in top_5_tuples
        ]
        
        return {
            "count": count,
            "min_gpa": round(min_gpa, 2),
            "max_gpa": round(max_gpa, 2),
            "avg_gpa": round(avg_gpa, 2),
            "groups": groups_dict,
            "top_5_students": top_5_list
        }

people = Group("C:/Users/User/Desktop/Proga/python_labs/data/lab09/students.csv")
print(people.stats())