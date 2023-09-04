class MutableString:
    def __init__(self, string = '') -> None:
        self.string = string

    def lower(self):
        self.string = self.string.lower()
        return self.string

    def upper(self):
        self.string = self.string.upper()
        return self.string
    
    def __str__(self) -> str:
        return self.string
    
    def __repr__(self) -> str:
        return f'MutableString({repr(self.string)})'
    
    def __len__(self):
        return len(self.string)
    
    def __add__(self, other):
        return MemoryError(self.string + other.string)
    
    def __iter__(self):
        yield from self.string

    def __getitem__(self, key):
        if isinstance(key, slice):
            return MutableString(self.string[key])
        return self.string[key]
    
    def __setitem__(self, key, value):
        lst = [item for item in self.string]
        lst[key] = value
        self.string = "".join(lst)

    def __delitem__(self, key):
        lst = [item for item in self.string]
        del lst[key]
        self.string = "".join(lst)


mutablestring = MutableString('beegeek')

print(*mutablestring)
print(str(mutablestring))
print(repr(mutablestring))

print()        

mutablestring = MutableString('beegeek')

s1 = mutablestring[2:]
s2 = mutablestring[:5]
s3 = mutablestring[2:5:2]

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))

print()

mutablestring = MutableString('beegeek')

print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)

print()

string = '''For a long time it was a mystery to me how something very expensive and technologically advanced could be 
so useless. And I soon realized that a computer is a stupid machine that has the ability to do incredibly smart things, 
while programmers are smart people who have a talent for doing incredibly stupid things. In short, 
they found each other.
Bill Bryson'''

mutablestring1 = MutableString(string)
mutablestring2 = mutablestring1[20:45]

print(mutablestring1 is mutablestring2)

print()

string = '''Many of you are familiar with the virtues of being a programmer. There are only three of them, 
and of course this is: laziness, impatience and pride. Larry Wall'''
mutablestring = MutableString(string)

print(mutablestring[20])
print(mutablestring[-30])
print(mutablestring[:11])
print(mutablestring[16:])
print(mutablestring[4::10])
print(mutablestring[::-10])

print()

mutablestring = MutableString('beegeek')

del mutablestring[1:3]
print(mutablestring)

print()

mutablestring1 = MutableString('bee')
mutablestring2 = MutableString('geek')

print(mutablestring1 + mutablestring2)
print(mutablestring2 + mutablestring1)

print()

mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)

print()

mutablestring = MutableString()
print(repr(mutablestring))

print()

mutablestring = MutableString('beegeek')

del mutablestring[2:5]
del mutablestring[1:5:2]
print(mutablestring)