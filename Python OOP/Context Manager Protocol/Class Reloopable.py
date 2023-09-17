class Reloopable:
    def __init__(self, file) -> None:
        self.file = file

    def __enter__(self):
        return self.file.readlines()
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


with open('file.txt', 'w') as file:
    file.write('Evil is evil\n')
    file.write('Lesser, greater, middling\n')
    file.write('Makes no difference\n')
    
with Reloopable(open('file.txt')) as reloopable:
    for line in reloopable:
        print(line.strip())
    for line in reloopable:
        print(line.strip())

print()

with open('file.txt', 'w') as file:
    pass
    
file = open('file.txt')
print(file.closed)

with Reloopable(file) as reloopable:
    pass

print(file.closed)