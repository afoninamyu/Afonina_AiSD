from enum import Enum

LINEAR = "linear"
QUADRATIC = "quadratic"
DOUBLE = "double"

class State(Enum): #enum-класс меток для состояний ячейки
    EMPTY = 0 #не использовалась
    DELETED = 1 #tombstone - была удалена, можно переиспользовать

class HashTable:
    def __init__(self, capacity=11, method="linear", load_limit=0.7):
        self.capacity = self._find_next_prime(capacity) #для hash2 capacity должно быть простым числом
        self.size = 0
        self.table = [State.EMPTY] * self.capacity #в каждой ячейке: кортеж (ключ, значение), или EMPTY, или DELETED
        self.method = method
        self.load_limit = load_limit

    @staticmethod #статистический метод - не привязан ни к экземплярам (self), ни к классу (cls)
    def _is_prime(n): #простое ли число. Нижнее подчёркивание - приватный (непубличный) метод, для внутреннего использования
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5 + 1)):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def _find_next_prime(n): #поиск следующего простого числа для расширения capacity
        if n <= 2:
            return 2
        if n % 2 == 0: #делает число нечётным. Чётное число никогда не может быть простым
            n += 1
        while not HashTable._is_prime(n): #перебирает по 2, чтобы обойти чётные числа
            n += 2
        return n

    def _hash1(self, key): #приватные, пользователю не нужно знать, как считается индекс
        return hash(key) % self.capacity

    def _hash2(self, key): #для двойного хеширования
        h = abs(hash(key))
        return 1 + (h % (self.capacity - 1))

    def _probe_index(self, key, i):
        m = self.capacity
        h1 = self._hash1(key)
        if self.method == LINEAR: #АЛЬТЕРНАТИВА: без глобальных констант:  if self.method == "linear"
            return (h1 + i) % m
        elif self.method == QUADRATIC:
            return (h1 + i + i * i) % m
        elif self.method == DOUBLE:
            h2 = self._hash2(key)
            return (h1 + i * h2) % m
        else:
            raise ValueError("Unknown method")

    def insert(self, key, value): #вставка
        if (self.size + 1) / self.capacity > self.load_limit:
            self._rehash()
        m = self.capacity
        for i in range(m):
            idx = self._probe_index(key, i)
            cell = self.table[idx]
            if cell is State.EMPTY or cell is State.DELETED:    #нашли пустую ячейку или tombstone — можно вставить
                self.table[idx] = (key, value)
                self.size += 1
                return
            elif cell[0] == key:    #ключ уже есть — обновляем значение
                self.table[idx] = (key, value)
                return
        raise RuntimeError("Hash table is full")

    def get(self, key): #извлечение
        m = self.capacity
        for i in range(m):
            idx = self._probe_index(key, i)
            cell = self.table[idx]
            if cell is State.EMPTY:
                raise KeyError(key)
            if cell is not State.DELETED and cell[0] == key:
                return cell[1]
        raise KeyError(key)

    def delete(self, key): #удаление
        m = self.capacity
        for i in range(m):
            idx = self._probe_index(key, i)
            cell = self.table[idx]
            if cell is State.EMPTY:
                raise KeyError(key)
            if cell is not State.DELETED and cell[0] == key:
                self.table[idx] = State.DELETED
                self.size -= 1
                return True
        raise KeyError(key)

    def _rehash(self): #обновление размера
        old_table = self.table
        self.capacity = self._find_next_prime(self.capacity * 2)
        self.size = 0
        self.table = [State.EMPTY] * self.capacity
        for cell in old_table:
            if cell is not State.EMPTY and cell is not State.DELETED:
                self.insert(cell[0], cell[1])