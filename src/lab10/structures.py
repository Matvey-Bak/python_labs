from collections import deque
from typing import Any


class Stack:
    """Структура данных «стек» (LIFO) на базе list."""
    
    def __init__(self):
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """Добавить элемент на вершину стека."""
        self._data.append(item)

    def pop(self) -> Any:
        """Снять верхний элемент стека и вернуть его."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self) -> Any | None:
        """Вернуть верхний элемент без удаления. Возвращает None, если стек пуст."""
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        """Вернуть True, если стек пуст, иначе False."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в стеке."""
        return len(self._data)
    
stack = Stack()
print(f"1. Создан стек: {stack}")
print(f"   Пустой? {stack.is_empty()}, Длина: {len(stack)}, Верх: {stack.peek()}")


elements = [10, 20, 30, "текст", [1, 2]]
for elem in elements:
    stack.push(elem)
    print(f"2. Добавили {elem}: {stack}")
    print(f"   Верхний: {stack.peek()}, Длина: {len(stack)}")


print("\n3. Извлекаем (LIFO порядок):")
while not stack.is_empty():
    item = stack.pop()
    print(f"   Извлекли: {item}, Осталось: {len(stack)}, Верх: {stack.peek()}")

print(f"\n4. Итог: {stack}, Пустой? {stack.is_empty()}")


class Queue:
    """Структура данных «очередь» (FIFO) на базе collections.deque."""
    
    def __init__(self):
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Добавить элемент в конец очереди."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """Взять элемент из начала очереди и вернуть его."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def peek(self) -> Any | None:
        """Вернуть первый элемент без удаления. Возвращает None, если очередь пуста."""
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        """Вернуть True, если очередь пуста."""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в очереди."""
        return len(self._data)
    
q = Queue()

# Инициализация
print(f"1. Создана очередь: {q}")
print(f"   Пустая? {q.is_empty()}, Длина: {len(q)}, Первый: {q.peek()}")

# Добавляем элементы
elements = ["первый", "второй", "третий", 100, 200]
for elem in elements:
    q.enqueue(elem)
    print(f"2. Добавили {elem}: {q}")
    print(f"   Первый: {q.peek()}, Длина: {len(q)}")

# Извлекаем элементы
print("\n3. Извлекаем (FIFO порядок):")
while not q.is_empty():
    item = q.dequeue()
    print(f"   Извлекли: {item}, Осталось: {len(q)}, Первый: {q.peek()}")

# Итог
print(f"\n4. Итог: {q}, Пустая? {q.is_empty()}")