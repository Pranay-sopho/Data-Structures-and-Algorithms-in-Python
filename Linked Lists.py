class Empty(Exception):
    pass


class LinkedStack:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._head._element

    def push(self, element):
        self._head = self._Node(element, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer


"""
data = LinkedStack()
data.push(4)
data.push(3)
print(data.pop())
print(data.is_empty())
print(data.top())
"""


class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def enqueue(self, element):
        newest = self._Node(element, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer


class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._tail._next._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        head = self._tail._next
        answer = head._element
        head = head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, element):
        newest = self._Node(element, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next


class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        newest = self._Node(element, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        answer = node._element
        node._element = node._prev = node._next = None
        return answer


class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._trailer._prev._element

    def insert_first(self, element):
        self._insert_between(element, self._header, self._header._next)

    def insert_last(self, element):
        self._insert_between(element, self._trailer._prev, self._trailer)

    def delete_first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        first = self._delete_node(self._header._next)
        return first

    def delete_last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        last = self._delete_node(self._trailer._prev)
        return last


"""
data = LinkedDeque()
print(len(data))
data.insert_first(3)
data.insert_first(65)
data.insert_last(54)
print(data.first())
print(data.is_empty())
data.delete_first()
data.delete_last()
print(data.first())
print(data.last())
"""


class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        """
        start = p._container._header._next
        pos = self.Position(p._container, start)
        while pos != None:
            if pos == p:
                return True
            start = start._next
            pos = self.Position(p._container, start)
        return False
        """
        if not isinstance(p, self.Position):
            raise TypeError('p must be Proper Position Type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        # if node._prev is None or node._next is None:
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        # while cursor != None:
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, element, predecessor, successor):
        node = super()._insert_between(element, predecessor, successor)
        return self._make_position(node)

    def add_first(self, element):
        return self._insert_between(element, self._header, self._header._next)

    def add_last(self, element):
        return self._insert_between(element, self._trailer._prev, self._trailer)

    def add_before(self, position, element):
        node = self._validate(position)
        return self._insert_between(element, node._prev, node)

    def add_after(self, position, element):
        node = self._validate(position)
        return self._insert_between(element, node, node._next)

    def delete(self, position):
        node = self._validate(position)
        return self._delete_node(node)

    def replace(self, position, element):
        node = self._validate(position)
        old_value = node._element
        node._element = element
        return node._element


def insertion_sort(L):
    marker = L.first()
    while marker != L.last():
        pivot = L.after(marker)
        value = pivot.element()
        if value > marker.element():
            marker = pivot
        else:
            walk = marker
            while walk != L.first() and L.before(walk).element() > pivot.element():
                walk = L.before(walk)
            L.delete(pivot)
            L.add_before(walk, value)


"""
L = PositionalList()
L.add_first(5)
L.add_last(4)
L.add_first(6)
L.add_last(3)
print(L.first().element())
print(L.last().element())
insertion_sort(L)
print(L.first().element())
print(L.last().element())
"""


#             -------Priority Queues--------

class PriorityQueueBase:
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):
    def _find_min(self):
        if self.is_empty():
            raise Empty('Priority Queue is Empty')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        self._data.add_last(self._Item(key, value))

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._data.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        if self.is_empty():
            raise Empty('Priority Queue is Empty.')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Empty('Priority Queue is Empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
