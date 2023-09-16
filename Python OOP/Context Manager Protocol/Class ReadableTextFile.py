class ReadableTextFile:
    def __init__(self, filename) -> None:
        self.filename = filename

    def __enter__(self):
        with open(self.filename, 'r', encoding='UTF-8') as self.file_line:
            for item in self.file_line:
                yield item.strip()
    
    def __exit__(self, exc_type, exc_value, traceback):
        return self.file_line.close()


with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
    print('Только посмотрите!', file=file)
    print('Как величаво она парит в воздухе', file=file)
    print('Как орел', file=file)
    print('На воздушном шаре', file=file)

with ReadableTextFile('glados_quotes.txt') as file:
    for line in file:
        print(line)

print()

with open('poem.txt', 'w', encoding='utf-8') as file:
    print('Я кашлянул в звенящей тишине,', file=file)
    print('И от шального эха стало жутко…', file=file)
    print('Расскажет ли утятам обо мне', file=file)
    print('под утро мной испуганная утка?', file=file)

with ReadableTextFile('poem.txt') as file:
    for line in file:
        print(line)