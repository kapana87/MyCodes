class Greeter:
    def __init__(self, name) -> None:
        self.name = name

    def __enter__(self):
        print(f'Приветствую, {self.name}!')
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f'До встречи, {self.name}!')
    

with Greeter('Кейв'):
    print('...')

print()

with Greeter('Михаил Г.') as greeter:
    print(
        '\nКак бессонница в час ночной\n'
        'Меняет, нелюдимая, облик твой,\n'
        'Чьих невольница ты идей?\n'
        'Зачем тебе охотиться на людей?\n'
    )

print()

with Greeter('Кейв') as greeter:
    print(greeter.name)