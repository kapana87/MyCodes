class CustomContextManager:
    def __init__(self, value):
        self.value = value

    def __enter__(self):
        print('Вход в контекстный менеджер...')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('Выход из контекстного менеджера...')

    def __repr__(self):
        return f'CustomContextManager(value={repr(self.value)})' 


with CustomContextManager('pygen') as manager:
    print(manager)
    print(manager.value)