class HangmanWord:
    def __init__(self, word):
        self.word = word.lower()
        self.reveal_set = set()

    def __str__(self):
        return_str = " ".join(
            [char if char in self.reveal_set else "_" for char in self.word]
        )
        return return_str

    def _validate_character(self, char):
        if len(char) != 1 or not char.isalpha():
            return False
        if not self.char_in_word(char):
            return False
        return True

    def char_in_word(self, char):
        return char.lower() in self.word

    def reveal_letter(self, char):
        if self._validate_character(char):
            self.reveal_set.add(char.lower())
