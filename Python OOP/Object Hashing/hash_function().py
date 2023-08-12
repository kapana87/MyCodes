def hash_function(obj):
    obj = str(obj)
    first_sum = sum(ord(obj[index]) * ord(obj[-index - 1]) for index in range(len(obj) // 2))
    second_sum = 0
    if len(obj) % 2 != 0:
        first_sum += ord(obj[len(obj) // 2])

    for index in range(len(obj)):
        if index % 2 == 0:
            second_sum += ord(obj[index]) * (index + 1)
        else:
            second_sum -= ord(obj[index]) * (index + 1)
    return (first_sum * second_sum) % 123456791


print(hash_function('python'))
print()
print(hash_function(12345))
print()
print(hash_function(None))