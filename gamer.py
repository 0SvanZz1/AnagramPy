class Gamer():
    def __init__(self):
        self.chances = 5
        self.discovered_words = []

    def decrease_chances(self):
        self.chances-=1

    def discover_word(self, word):
        self.discovered_words.append(word)