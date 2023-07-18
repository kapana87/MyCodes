class Todo:
    def __init__(self):
        self.things = []

    def add(self, case_title, number):
        self.things.append((case_title, number))

    def get_by_priority(self, n):
        return [case[0] for case in self.things if n in case]

    def get_low_priority(self):
        min_case = min(self.things, key=lambda x: x[1], default=0)
        return [case[0] for case in self.things if case[1] in min_case]

    def get_high_priority(self):
        max_case = max(self.things, key=lambda x: x[1], default=0)
        return [case[0] for case in self.things if case[1] in max_case]