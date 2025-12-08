from typing import Any, Optional, Iterator


class Node:
    """Узел односвязного списка."""
    
    def __init__(self, value: Any, next: Optional['Node'] = None):
        self.value = value
        self.next = next
        
    def __repr__(self) -> str:
        """Строковое представление узла в виде [значение]."""
        return f"[{self.value}]"


class SinglyLinkedList:
    """Односвязный список."""
    
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None  # для ускорения append
        self._size: int = 0

    def append(self, value: Any) -> None:
        """Добавить элемент в конец списка за O(1) с использованием tail."""
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1

    def prepend(self, value: Any) -> None:
        """Добавить элемент в начало списка за O(1)."""
        new_node = Node(value, next=self.head)
        self.head = new_node
        
        # Если список был пуст, обновляем tail
        if self.tail is None:
            self.tail = new_node
        
        self._size += 1

    def insert(self, idx: int, value: Any) -> None:
        """Вставить элемент по индексу idx."""
        # Проверка корректности индекса
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")
        
        # Вставка в начало
        if idx == 0:
            self.prepend(value)
            return
        
        # Вставка в конец
        if idx == self._size:
            self.append(value)
            return
        
        # Вставка в середину
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        new_node = Node(value, next=current.next)
        current.next = new_node
        self._size += 1

    def remove(self, value: Any) -> bool:
        """Удалить первое вхождение значения value. Возвращает True, если элемент был удалён."""
        if self.head is None:
            return False
        
        # Удаление из начала
        if self.head.value == value:
            self.head = self.head.next
            # Если список стал пустым, обновляем tail
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        # Поиск элемента для удаления
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                # Удаляем элемент
                current.next = current.next.next
                # Если удалили последний элемент, обновляем tail
                if current.next is None:
                    self.tail = current
                self._size -= 1
                return True
            current = current.next
        
        return False

    def remove_at(self, idx: int) -> Any:
        """Удалить элемент по индексу idx и вернуть его значение."""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size - 1}]")
        
        # Удаление из начала
        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            # Если список стал пустым, обновляем tail
            if self.head is None:
                self.tail = None
            self._size -= 1
            return value
        
        # Удаление из середины или конца
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        value = current.next.value
        current.next = current.next.next
        
        # Если удалили последний элемент, обновляем tail
        if current.next is None:
            self.tail = current
        
        self._size -= 1
        return value

    def __iter__(self) -> Iterator[Any]:
        """Итератор по значениям в списке (от головы к хвосту)."""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        """Количество элементов в списке."""
        return self._size

    def __repr__(self) -> str:
        """Строковое представление списка в формате конструктора."""
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def visualize(self) -> str:
        """Красивое визуальное представление списка: [A] -> [B] -> [C] -> None"""
        if self.head is None:
            return "None"
        
        result_parts = []
        current = self.head
        
        while current is not None:
            result_parts.append(f"{current}")  # используем __repr__ Node
            current = current.next
        
        result_parts.append("None")
        return " -> ".join(result_parts)
    
    def __str__(self) -> str:
        """Строковое представление с красивой визуализацией связей."""
        return self.visualize()


if __name__ == "__main__":
    lst = SinglyLinkedList()
    
    lst.append(1)
    lst.append(2)
    lst.append(3)
    print(f"После append: {lst}")  
    print(f"Красивый вывод: {str(lst)}")  
    
    lst.prepend(0)
    print(f"\nПосле prepend: {lst}")  
    print(f"Красивый вывод: {str(lst)}") 

    lst.insert(2, 1.5)
    print(f"\nПосле insert(2, 1.5): {lst}") 
    print(f"Красивый вывод: {str(lst)}") 
    

    lst.remove(1.5)
    print(f"\nПосле remove(1.5): {lst}")  
    print(f"Красивый вывод: {str(lst)}")  
    
    removed = lst.remove_at(1)
    print(f"\nУдалён элемент: {removed}") 
    print(f"После remove_at(1): {lst}")  
    print(f"Красивый вывод: {str(lst)}") 
 
    letters = SinglyLinkedList()
    letters.append("A")
    letters.append("B")
    letters.append("C")
    print(f"\nСписок букв: {str(letters)}")  
    