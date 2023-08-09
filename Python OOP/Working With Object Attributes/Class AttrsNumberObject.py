class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.attrs_num = 0
        self.__dict__.update(kwargs)
    def __getattribute__(self, item):
        if item == 'attrs_num':
            self.__dict__['attrs_num'] = len(self.__dict__)
        return object.__getattribute__(self, item)


music_group = AttrsNumberObject(name='Woodkid', genre='pop')

print(music_group.attrs_num)
music_group.country = 'France'
print(music_group.attrs_num)

print()

person = AttrsNumberObject(name='Mark')

print(person.attrs_num)

person.surname = 'Zuckerberg'
print(person.attrs_num)

person.age = 38
print(person.attrs_num)

person.job = 'Programmer'
print(person.attrs_num)
