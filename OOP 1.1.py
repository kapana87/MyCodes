class TextHandler:
    def __init__(self):
        self.lst = []

    def add_words(self, string):
        for word in string.split():
            self.lst.append(word)

    def get_shortest_words(self):
        return [word for word in self.lst if len(word) == len(min(self.lst, key=len))]

    def get_longest_words(self):
        return [word for word in self.lst if len(word) == len(max(self.lst, key=len))]


texthandler = TextHandler()

texthandler.add_words('The world will hold my trial for your sins')
texthandler.add_words('Never meant to see the sky, never meant to live')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())