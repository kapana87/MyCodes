class ProtectedObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __getattribute__(self, attr):
        if '_' in attr or '__' in attr:
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__getattribute__(self, attr)

    def __setattr__(self, key, value):
        if '_' in key or '__' in key:
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        return object.__setattr__(self, key, value)

    def __delattr__(self, attr):
        if '_' in attr or '__' in attr:
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        object.__delattr__(self, attr)


# TEST_1
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.login)
    print(user._password)
except AttributeError as e:
    print(e)

print()

# TEST_2:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    user._password = 'qwerty12345'
except AttributeError as e:
    print(e)

print()

# TEST_3:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    del user._password
except AttributeError as e:
    print(e)

print()

# TEST_4:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

del user.login
print('Успешное удаление атрибута')

print()

# TEST_5:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')
print(object.__getattribute__(user, 'login'))
print(object.__getattribute__(user, '_password'))

print()

# TEST_6:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    user.__dict__['attr'] = 1
except AttributeError as e:
    print(e)

print()

# TEST_7:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user.__dict__)
except AttributeError as e:
    print(e)

print()

# TEST_8:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    del user.__dict__['_password']
except AttributeError as e:
    print(e)

print()

# TEST_9:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

del user.login

try:
    print(user.login)
except AttributeError:
    print('Атрибут отсутствует')

print()

# TEST_10:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

user.login = 'Kamiya'
print(user.login)

user.nickname = 'PG'
print(user.nickname)

print()

# TEST_11:
user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

try:
    print(user._secret)
except AttributeError as e:
    print(e)

try:
    user._secret = 'PG'
except AttributeError as e:
    print(e)

try:
    del user._secret
except Exception as e:
    print(e)