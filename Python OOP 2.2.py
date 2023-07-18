from io import StringIO


class StrExtension:
    @staticmethod
    def remove_vowels(string):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
        string1 = ''
        for i in string:
            if i not in vowels:
                string1 += i
            else:
                string1 += ''
        return string1

    @staticmethod
    def leave_alpha(string):
        values = StringIO()
        for value in [char for char in string if char.isalpha()]:
            values.write('' + value)
        return values.getvalue()

    @staticmethod
    def replace_all(string, chars, char):
        for i in chars:
            string = string.replace(i, char)
        return string


print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))

