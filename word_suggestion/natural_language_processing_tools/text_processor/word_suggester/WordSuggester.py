from abc import ABCMeta, abstractmethod


class WordSuggester(metaclass=ABCMeta):
    @abstractmethod
    def suggest_next_word(self, normalized_sentence: str) -> list:
        pass
