def check_type(*arg_types):
    def decorator(func):
        def wrapped(self, other, *args, **kwargs):
            if isinstance(other, arg_types):
                return func(self, other, *args, **kwargs)
            return NotImplemented
        return wrapped
    return decorator


class PQueue:
    pass


class Queue(PQueue):
    def __init__(self, *args):
        self.args = list(args)

    def add(self, *args):
        self.args.extend(args)

    def pop(self):
        if len(self.args) != 0:
            return self.args.pop(0)

    def __str__(self):
        return " -> ".join(map(str, self.args))

    @check_type(PQueue)
    def __eq__(self, other):
        if self.args == other.args:
            return True
        return False

    @check_type(PQueue)
    def __ne__(self, other):
        if self.args != other.args:
            return True
        return False

    @check_type(PQueue)
    def __add__(self, other):
        self.args = self.args + other.args
        return self.__str__()

    @check_type(PQueue)
    def __iadd__(self, other):
        self.args += other.args
        return self

    @check_type(PQueue, int)
    def __rshift__(self, other):
        if other >= len(self.args):
            return Queue("")
        elif other == 0:
            return self.__str__()
        return Queue(*self.args[other:])


queue = Queue(1, 2)
queue.add(3)
queue.add(4, 5)

print(queue)
print(queue.pop())
print(queue)

print()

queue1 = Queue(1, 2, 3)
queue2 = Queue(1, 2)

print(queue1 == queue2)
queue2.add(3)
print(queue1 == queue2)

print()

queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

print(queue1 + queue2)

print()

queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

queue1 += queue2

print(queue1)

print()

queue = Queue(1, 2, 3, 4, 5)
id1 = id(queue)
print(queue)

queue += Queue(6, 7, 8, 9, 10)
id2 = id(queue)

print(queue)
print(id1 == id2)

queue = queue + Queue(11, 12, 13, 14, 15)
id3 = id(queue)

print(queue)
print(id1 == id3)

print()

queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)

print()

queue = Queue(1, 2, 3)
print(queue.__add__([]))
print(queue.__iadd__('bee'))
print(queue.__rshift__('geek'))