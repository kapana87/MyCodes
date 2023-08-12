def limited_hash(left, right, hash_function=hash):
    def custom_hash(obj):
        h = hash_function(obj)
        if h > right:
            return left + ((h - right - 1) % (right - left + 1))
        elif h < left:
            return right - ((left - h - 1) % (right - left + 1))
        else:
            return h

    return custom_hash


hash_function = limited_hash(10, 15)

print(hash_function(10))
print(hash_function(11))
print(hash_function(15))