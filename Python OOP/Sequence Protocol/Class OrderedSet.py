from copy import deepcopy


class OrderedSet:

    def __init__(self, iterable=set()) -> None:
        self.iterable = iterable

    def add(self, item):
        self.iterable.add(item)

    def discard(self, item):
        if item in self.iterable:
            self.iterable.remove(item)
    
    def __len__(self):
        return len(self.iterable)
    
    def __iter__(self):
        yield from self.iterable

    def __contains__(self, item):
        return item in self.iterable
    
    