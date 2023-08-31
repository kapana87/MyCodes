import itertools as it


class CyclicList:
    """A class that creates an infinitely iterable object"""

    def __init__(self, iterable) -> None:
        self.iterable = [] if not iterable else list(iterable)

    def append(self, items):
        """Adds an undefined number of elements to an iterable object"""
        self.iterable += [items]
    
    def pop(self, index=None):
        if index is None:
            return self.iterable.pop()
        return self.iterable.pop(index)
    
    def __len__(self):
        return len(self.iterable)
    
    def __iter__(self):
        yield from it.cycle(self.iterable)

    def __getitem__(self, index):
        return self.iterable[index % len(self.iterable)]
    

cyclic_list = CyclicList([1, 2, 3])

cyclic_list.append(4)
print(cyclic_list.pop())
print(len(cyclic_list))
print(cyclic_list.pop(0))
print(len(cyclic_list))

print()

cyclic_list = CyclicList([1, 2, 3])

for index, elem in enumerate(cyclic_list):
    if index > 6:
        break
    print(elem, end=' ')

print()

indexes = [553, 555, 561, 606, 610, 744, 748, 766, 930, 1015, 1049, 1074, 1093, 1107, 1275, 1290, 1309, 1315, 1366,
           1398, 1552, 1573, 1629, 1639, 1651, 1656, 1755, 1792, 1857, 1909, 1918, 1919, 1937, 1949, 1997, 2002, 2085,
           2144, 2156, 2181, 2219, 2233, 2256, 2290, 2299, 2308, 2310, 2327, 2366, 2393, 2615, 2653, 2665, 2788, 2812,
           2902, 2914, 3035, 3094, 3219, 3221, 3254, 3315, 3412, 3502, 3532, 3567, 3572, 3614, 3694, 3740, 3753, 3760,
           3794, 3826, 3838, 3855, 3906, 3951, 4016, 4019, 4139, 4203, 4219, 4285, 4300, 4397, 4398, 4503, 4529, 4559,
           4587, 4589, 4710, 4747, 4783, 4785, 4790, 4890, 4995]

numbers = CyclicList([1, 2, 3, 4, 5])

numbers_list = [numbers[i] for i in indexes]
print(numbers_list)