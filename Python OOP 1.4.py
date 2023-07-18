from copy import deepcopy


class Wordplay:
    def __init__(self, words=[]):
        self.words = deepcopy(words)

    def add_word(self, string):
        if string not in self.words:
            self.words.append(string)

    def words_with_length(self, number):
        return [word for word in self.words if len(word) == number]

    def only(self, *args):
        return [word for word in self.words if set(word).issubset(args)]

    def avoid(self, *args):
        return [word for word in self.words if set(word).isdisjoint(set(args))]


wordplay = Wordplay(['o', 'to', 'otto', 'top', 't'])

print(wordplay.only('o', 't'))