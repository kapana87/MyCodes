from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word):
        self.word = word

    def __str__(self):
        return f"{self.word}".capitalize()

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.word)})"

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented


words = [Word('python'), Word('bee'), Word('geek')]

print(sorted(words))
print(min(words))
print(max(words))

print()

words = [Word('miss'), Word('notice'), Word('forget'), Word('six'), Word('son'), Word('every'), Word('response'),
         Word('success'), Word('million'), Word('game'), Word('most'), Word('economic'), Word('guy'), Word('worry'),
         Word('professional'), Word('sea'), Word('role'), Word('determine'), Word('drive'), Word('value'), Word('tend'),
         Word('forget'), Word('policy'), Word('bit'), Word('property'), Word('officer'), Word('truth'), Word('reduce'),
         Word('suggest'), Word('rest'), Word('seat'), Word('candidate'), Word('according'), Word('he'), Word('reach'),
         Word('five'), Word('food'), Word('purpose'), Word('center'), Word('last'), Word('power'), Word('goal'),
         Word('happy'), Word('pattern'), Word('pretty'), Word('control'), Word('share'), Word('better'), Word('this'),
         Word('give'), Word('and'), Word('clear'), Word('argue'), Word('into'), Word('alone'), Word('sea'),
         Word('hour'), Word('response'), Word('occur'), Word('consumer'), Word('bring'), Word('expect'), Word('until'),
         Word('race'), Word('fall'), Word('charge'), Word('meet'), Word('still'), Word('single'), Word('consider'),
         Word('less'), Word('special'), Word('building'), Word('body'), Word('often'), Word('window'), Word('dinner'),
         Word('small'), Word('stop'), Word('above'), Word('lead'), Word('huge'), Word('despite'), Word('direction'),
         Word('city'), Word('couple'), Word('conference'), Word('purpose'), Word('oil'), Word('chance'), Word('home'),
         Word('practice'), Word('perhaps'), Word('coach'), Word('gas'), Word('may'), Word('quickly'), Word('officer'),
         Word('free'), Word('let')]

print(sorted(words))
print(min(words))
print(max(words))