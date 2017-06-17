class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, key, value):
        if key < len(self._coords):
            self._coords[key] = value
        else:
            return ValueError

