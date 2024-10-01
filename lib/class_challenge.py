class GrammarStats:
    def __init__(self):
        self.counter = 0

    def check(self, text):
        if type(text) != str:
            raise Exception("Only strings are allowed!")
        punctuation = '.!?'
        if text[0] == text[0].upper() and text[-1]in punctuation:
            self.counter += 1
            return True
        else:
            return False

    def percentage_good(self):
        return f"{self.counter}%"

