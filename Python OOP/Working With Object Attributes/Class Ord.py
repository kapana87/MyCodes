class Ord:
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        self.item = ord(item)
        return self.item


obj = Ord()

print(obj.a)
print(obj.b)