import re


class CaseHelper:
    @staticmethod
    def is_snake(string):
        regex = re.fullmatch(r'[a-z]+_?[a-z]*', string)
        return bool(regex)

    @staticmethod
    def is_upper_camel(string):
        regex = re.fullmatch(r'[A-Z][a-z]+[A-Z]?[a-z]+', string)
        return bool(regex)

    @staticmethod
    def to_snake(text):
        return re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text).lower()

    @staticmethod
    def to_upper_camel(text):
        return ''.join(word.capitalize() for word in text.split('_'))


