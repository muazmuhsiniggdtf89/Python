class StringReverse:
    def __init__(self, text):
        self.__text = text   

    def reverse_words(self):
        words = self.__text.split()
        return " ".join(words[::-1])



s = StringReverse("we live we")
print(s.reverse_words())
