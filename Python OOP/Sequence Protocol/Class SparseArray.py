from typing import Any


class SparseArray:
    def __init__(self, default):
        self.default = default
        self.lst = []
    
    def __setitem__(self, index: int, value: Any) -> None:
        if index >= len(self.lst):
            quantity = index + 1 - len(self.lst)
            self.lst.extend([self.default] * quantity)
        self.lst[index] = value

    def __getitem__(self, index) -> Any:
        if index >= len(self.lst):
            return self.default
        return self.lst[index]


array = SparseArray(0)

array[5] = 1000
array[12] = 1001

print(array[5])
print(array[12])
print(array[13])

print()