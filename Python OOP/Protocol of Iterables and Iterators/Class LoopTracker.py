class LoopTracker:
    def __init__(self, iterable):
        self._iterable = iter(iterable)
        self._empty_accesses = self._accesses = 0
        self._is_empty = False
        try:
            self._nextvalue = self._first = next(self._iterable)
        except StopIteration:
            self._is_empty = True

    def __iter__(self):
        return self

    def __next__(self):
        if self._is_empty:
            self._empty_accesses += 1
            raise StopIteration
        self._curvalue = self._nextvalue
        self._accesses += 1
        try:
            self._nextvalue = next(self._iterable)
        except StopIteration:
            self._is_empty = True
        return self._curvalue

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if hasattr(self, '_first'):
            return self._first
        raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if hasattr(self, '_curvalue'):
            return self._curvalue
        raise AttributeError('Последнего элемента нет')

    def is_empty(self):
        return self._is_empty


# TEST_1:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(list(loop_tracker))

# TEST_2:
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.accesses)
next(loop_tracker)
next(loop_tracker)
print(loop_tracker.accesses)

# TEST_3:
loop_tracker = LoopTracker([1, 2, 3])
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

# TEST_4:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

print(next(loop_tracker))
print(loop_tracker.last)

# TEST_5:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.empty_accesses)
next(loop_tracker)
next(loop_tracker)

for _ in range(5):
    try:
        next(loop_tracker)
    except StopIteration:
        pass

print(loop_tracker.empty_accesses)

# TEST_6:
loop_tracker = LoopTracker([1, 2])

print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())

# TEST_7:
loop_tracker = LoopTracker([1, 2, 3])

print(loop_tracker.first)
print(next(loop_tracker))

# TEST_8:
loop_tracker = LoopTracker([])

try:
    print(loop_tracker.first)
except AttributeError as e:
    print(e)

# TEST_9:
loop_tracker = LoopTracker([1, 2, 3])

print(next(loop_tracker))
print(loop_tracker.last)
print(next(loop_tracker))
print(loop_tracker.last)

# TEST_10:
loop_tracker = LoopTracker([1, 2, 3])

try:
    print(loop_tracker.last)
except AttributeError as e:
    print(e)

# TEST_11:
loop_tracker = LoopTracker(range(1_000))

for _ in range(100_000):
    next(loop_tracker, None)

print(loop_tracker.accesses)
print(loop_tracker.empty_accesses)

# TEST_12:
loop_tracker = LoopTracker(dict.fromkeys(range(100)))

print(next(loop_tracker))
print(next(loop_tracker))
print(next(loop_tracker))
print(loop_tracker.accesses)
print(loop_tracker.first)
print(loop_tracker.last)
print(loop_tracker.is_empty())

# TEST_13:
loop_tracker = LoopTracker([1, 2, 3])

try:
    loop_tracker.accesses = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.first = 1
except AttributeError as e:
    print(type(e))

try:
    loop_tracker.last = 1
except AttributeError as e:
    print(type(e))