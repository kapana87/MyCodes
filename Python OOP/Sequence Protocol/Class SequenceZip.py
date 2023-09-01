class SequenceZip:
    def __init__(self, *sequences):
        self.sequences = sequences

    def __len__(self):
        # Найдем длину самой короткой последовательности
        min_length = min((len(seq) for seq in self.sequences), default=0)
        return min_length

    def __getitem__(self, index):
        if index < 0:
            raise IndexError("Index must be non-negative")

        if index >= len(self):
            raise IndexError("Index out of range")

        # Создаем кортеж из элементов на соответствующих позициях в каждой последовательности
        result = tuple(seq[index] for seq in self.sequences)
        return result

    def __iter__(self):
        return self.SequenceZipIterator(self)

    class SequenceZipIterator:
        def __init__(self, sequence_zip):
            self.sequence_zip = sequence_zip
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index < len(self.sequence_zip):
                result = self.sequence_zip[self.index]
                self.index += 1
                return result
            else:
                raise StopIteration



sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(list(sequencezip))
print(tuple(sequencezip))

print()

sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(len(sequencezip))
print(sequencezip[1])
print(sequencezip[2])

print()

# TEST_3:
print(len(SequenceZip([1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 3, 4])))
print(len(SequenceZip(range(5), [1, 2, 4], 'data')))

print()

# TEST_4:
x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])

print()

# TEST_5:
many_large_sequences = [range(100000) for _ in range(100)]
sequencezip = SequenceZip(*many_large_sequences)
print(sequencezip[99999])

print()

# TEST_6:
sequencezip = SequenceZip()
print(len(sequencezip))
print(list(sequencezip))

print()

# TEST_7:
data = {'bee': 'bee', 'geek': 'geek'}

sequencezip = SequenceZip(data)
data['python'] = 'python'
print(data)
print(len(sequencezip))
print(list(sequencezip))

print()

# TEST_8:
data = {'bee': 'bee', 'geek': 'geek'}
sequencezip = SequenceZip(data)
print(sequencezip[0])
print(list(sequencezip))