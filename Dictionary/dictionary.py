class Dictionary:
    def __init__(self):
        self.words = {}
    
    def add_word(self, word, definition):
            self.words[word] = [definition]      
    
    def get_definitions(self, word):
        if word in self.words:
            return self.words[word]
        return f"The word '{word}' does not exist."
    
    def list_words(self):
        return list(self.words.keys())