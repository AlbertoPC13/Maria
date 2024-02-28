from abc import ABCMeta, abstractmethod


class Tokenizer(metaclass=ABCMeta):
    @abstractmethod
    def tokenize_sentence_by_words(self, text: str) -> list:
        pass
