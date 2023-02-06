from src.utils.exceptions import NoTextException


class WordCountCore:
    def __init__(self, payload) -> None:
        self.payload: dict = payload

    def count_words(self) -> int:
        words: list = [
            word for word in self.payload['text'].split(' ') if word != ''
        ]
        
        if word_count := len(words):
            return word_count
        
        else:
            raise NoTextException()


