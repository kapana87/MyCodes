class Pet:
    _lst = []
    def __init__(self, name):
        self.name = name
        Pet._lst.append(self)

    @classmethod
    def first_pet(cls):
        return cls._lst[0] if cls._lst else None

    @classmethod
    def last_pet(cls):
        return cls._lst[-1] if cls._lst else None

    @classmethod
    def num_of_pets(cls):
        return len(cls._lst)


pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())