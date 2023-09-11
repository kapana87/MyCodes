import sys

class RedirectedStdout:
    def __init__(self, new_output):
        self.new_output = new_output

    def __enter__(self):
        self.standard_output = sys.stdout
        sys.stdout = self.new_output

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = self.standard_output


with open('output.txt', mode='w', encoding='utf-8') as file:
    with RedirectedStdout(file):
        print('Python generation!')
    print('Возврат к стандартному потоку вывода')