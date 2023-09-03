class PermaDict:
    def __init__(self, data=None) -> None:
        self._data = dict(data or {})

    def __len__(self):
        return len(self._data)
    
    def __iter__(self):
        yield from self._data

    def __getitem__(self, key):
        return self._data[key]
        
    def __setitem__(self, key, value):
        if key in self.keys():
            raise KeyError('Изменение значения по ключу невозможно')
        self._data[key] = value

    def __delitem__(self, key):
        del self._data[key]

    def keys(self):
        return self._data.keys()
    
    def values(self):
        return self._data.values()
    
    def items(self):
        return self._data.items()


permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})

try:
    permadict['name'] = 'Arthur'
except KeyError as e:
    print(e)

print()

permadict = PermaDict()

permadict['name'] = 'Timur'
permadict['age'] = 30
del permadict['name']
print(permadict['age'])
print(len(permadict))

print()

permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})

print(*permadict)
print(*permadict.keys())
print(*permadict.values())
print(*permadict.items())