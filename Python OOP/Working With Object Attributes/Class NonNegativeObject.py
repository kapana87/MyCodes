class NonNegativeObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if isinstance(value, (int, float)):
                setattr(self, key, abs(value))
            else:
                setattr(self, key, value)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)


point = NonNegativeObject(x=1.5, y=-2.3, z=0.0, color='yellow')

print(point.x)
print(point.y)
print(point.z)
print(point.color)
