from copy import deepcopy


class OrderedSet:

    def __init__(self, iterable=None) -> None:
        self.iterable = {} if iterable is None else {key:None for key in iterable}

    def add(self, item):
        self.iterable[item] = None

    def discard(self, item):
        if item in self.iterable:
            self.iterable.pop(item)
    
    def __len__(self):
        return len(self.iterable)
    
    def __iter__(self):
        iterable = deepcopy(self.iterable)
        yield from iterable

    def __contains__(self, item):
        return item in self.iterable
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, OrderedSet):
            return self.iterable == other.iterable and tuple(self.iterable) == tuple(other.iterable)
        elif isinstance(other, set):
            return set(self.iterable) == other
        else:
            return NotImplemented


orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print(*orderedset)
print(len(orderedset))
    
print()

orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print('python' in orderedset)
print('C++' in orderedset)

print()

orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)

print()

print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
print(OrderedSet(['green', 'red', 'blue']) == 100)