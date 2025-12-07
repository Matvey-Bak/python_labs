# Теория CRUD операций в Python

## Что такое CRUD?

**CRUD** — это акроним от **Create, Read, Update, Delete** (Создание, Чтение, Обновление, Удаление). Это четыре базовые операции, которые выполняются с данными в большинстве приложений.

---

## 1. **Create (Создание)**
Добавление новых записей в хранилище данных.

### Основные методы:
- `insert()` - добавление одной записи
- `add()` - добавление в коллекцию
- `create()` - создание нового объекта
- `save()` - сохранение объекта

### Примеры:

```python
# Список
users = []
users.append({"id": 1, "name": "Alice"})

# Словарь
products = {}
products[101] = {"name": "Laptop", "price": 999.99}

# Класс
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

new_user = User("Bob", "bob@email.com")
```

---

## 2. **Read (Чтение)**
Получение данных из хранилища.

### Основные методы:
- `get()` - получение по ключу/идентификатору
- `find()` - поиск записей
- `filter()` - фильтрация данных
- `all()` - получение всех записей

### Примеры:

```python
# Чтение из списка
first_user = users[0]  # по индексу

# Чтение из словаря
product = products.get(101)  # по ключу
product = products[101]      # альтернатива

# Поиск в списке
user_alice = next((u for u in users if u["name"] == "Alice"), None)

# Фильтрация
adults = [u for u in users if u.get("age", 0) >= 18]
```

---

## 3. **Update (Обновление)**
Изменение существующих данных.

### Основные методы:
- `update()` - обновление полей
- `modify()` - модификация записи
- `save()` - сохранение изменений

### Примеры:

```python
# Обновление в словаре
products[101]["price"] = 899.99
products[101].update({"price": 899.99, "discount": 10})

# Обновление в списке
for user in users:
    if user["id"] == 1:
        user["name"] = "Alice Smith"
        break

# Обновление объекта
user_alice.name = "Alice Johnson"
user_alice.email = "alice.j@email.com"
```

---

## 4. **Delete (Удаление)**
Удаление данных из хранилища.

### Основные методы:
- `delete()` - удаление записи
- `remove()` - удаление из коллекции
- `pop()` - удаление с возвратом значения

### Примеры:

```python
# Удаление из словаря
deleted_product = products.pop(101, None)  # с возвратом
del products[102]  # без возврата

# Удаление из списка
users.remove(users[0])  # по объекту
del users[1]  # по индекту

# Удаление по условию
users = [u for u in users if u["id"] != 1]  # через фильтрацию
```

---

## Реализация CRUD в разных контекстах

### 1. **Работа со списками/словарями (в памяти)**
```python
class InMemoryDB:
    def __init__(self):
        self.data = {}
        self.next_id = 1
    
    def create(self, item):
        item_id = self.next_id
        self.data[item_id] = item
        self.next_id += 1
        return item_id
    
    def read(self, item_id):
        return self.data.get(item_id)
    
    def read_all(self):
        return list(self.data.values())
    
    def update(self, item_id, updates):
        if item_id in self.data:
            self.data[item_id].update(updates)
            return True
        return False
    
    def delete(self, item_id):
        return self.data.pop(item_id, None)
```

### 2. **CRUD с классами**
```python
class CRUDRepository:
    def __init__(self):
        self.items = []
    
    def create(self, **kwargs):
        item = {**kwargs, 'id': len(self.items) + 1}
        self.items.append(item)
        return item
    
    def read(self, item_id):
        for item in self.items:
            if item.get('id') == item_id:
                return item
        return None
    
    def update(self, item_id, **updates):
        for item in self.items:
            if item.get('id') == item_id:
                item.update(updates)
                return True
        return False
    
    def delete(self, item_id):
        self.items = [item for item in self.items if item.get('id') != item_id]
```

### 3. **CRUD с файлами (JSON)**
```python
import json
import os

class JSONCRUD:
    def __init__(self, filename):
        self.filename = filename
        self.load_data()
    
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = []
    
    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def create(self, item):
        item['id'] = len(self.data) + 1
        self.data.append(item)
        self.save_data()
        return item['id']
    
    def read(self, item_id):
        for item in self.data:
            if item.get('id') == item_id:
                return item
        return None
    
    def update(self, item_id, updates):
        for item in self.data:
            if item.get('id') == item_id:
                item.update(updates)
                self.save_data()
                return True
        return False
    
    def delete(self, item_id):
        self.data = [item for item in self.data if item.get('id') != item_id]
        self.save_data()
```

---


## Заключение

CRUD операции — это фундамент большинства приложений, работающих с данными. В Python их можно реализовывать на разных уровнях:
- Простые коллекции (списки, словари)
- Файлы (JSON, CSV)
- Базы данных (SQLite, PostgreSQL, MySQL)
- ORM системы (SQLAlchemy, Django ORM)

Понимание принципов CRUD необходимо для разработки любых приложений, от простых скриптов до сложных веб-приложений и микросервисов.