import ctypes


class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, j):
        if not 0 <= j < self._n:
            raise IndexError("Invalid Index")
        return self._A[j]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, capacity):
        B = self._make_array(capacity)
        for j in range(self._n):
            B[j] = self._A[j]
        self._A = B
        self._capacity = capacity

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

data = DynamicArray()
for k in range(5):
    data.append(k)
    print(data[k])
print('Length: ', len(data))