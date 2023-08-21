import itertools as it


class DevelopmentTeam:
    def __init__(self):
        self.junior = []
        self.senior = []

    def add_junior(self, *args):
        self.junior.extend((name, 'junior') for name in args)

    def add_senior(self, *args):
        self.senior.extend((name, 'senior') for name in args)

    def __iter__(self):
        yield from it.chain(self.junior, self.senior)

    def __next__(self):
        yield from it.chain(self.junior, self.senior)


beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
beegeek.add_senior('Gvido')
print(*beegeek, sep='\n')

print()

beegeek = DevelopmentTeam()

print(len(list(beegeek)))

print()

beegeek = DevelopmentTeam()

beegeek.add_junior('Timur')
beegeek.add_junior('Arthur', 'Valery')
print(*beegeek, sep='\n')

print()

pied_piper = DevelopmentTeam()

pied_piper.add_senior('Richard', 'Gilfoyle', 'Dinesh', 'Erlich')
pied_piper.add_junior('Jared', 'Big Head')

print(*pied_piper, sep='\n')
print(len(list(pied_piper)))

print()

smart_monkey = DevelopmentTeam()

smart_monkey.add_senior('Gvido', 'Alan')
smart_monkey.add_junior('Denis')

print(list(smart_monkey))