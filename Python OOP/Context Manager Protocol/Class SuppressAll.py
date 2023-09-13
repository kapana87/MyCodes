class SuppressAll:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return True
    

print('start')

with SuppressAll():
    print('Python generation!')
    raise ValueError

print('end')