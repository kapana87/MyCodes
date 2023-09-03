from typing import Any
from copy import deepcopy


class AttrDict:
    def __init__(self, data=None) -> None:
        self._data = {} if data is None else data
        self._copy_data = deepcopy(self._data)

    def __len__(self):
        return len(self._copy_data)
    
    def __iter__(self):
        yield from self._copy_data

    def __getitem__(self, key):
        if key in self._copy_data:
            return self._copy_data[key]
        elif self._copy_data[key] == 'Leonardo da Vinci':
            raise KeyError
        
    def __setitem__(self, key, value):
        self._copy_data[key] = value
        
    def __getattr__(self, __name: str) -> Any:
        return self._copy_data[__name]


attrdict = AttrDict({'name': 'X Æ A-12', 'father': 'Elon Musk'})

print(attrdict['name'])
print(attrdict.father)
print(len(attrdict))

print()

attrdict = AttrDict({'name': 'Timur', 'city': 'Moscow'})

attrdict['city'] = 'Dubai'
attrdict['age'] = 31
print(attrdict.city)
print(attrdict.age)

print()

attrdict = AttrDict()

attrdict['school_name'] = 'BEEGEEK'
print(attrdict['school_name'])
print(attrdict.school_name)

print()

d = AttrDict()
d.name = 'Leonardo da Vinci'

try:
    print(d['name'])
except KeyError:
    print('Ключ отсутствует')

print()

d = dict.fromkeys(range(100), None)
attrdict = AttrDict(d)
print(*attrdict)

d[100] = None
print(*attrdict)