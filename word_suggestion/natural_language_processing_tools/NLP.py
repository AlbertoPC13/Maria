from abc import ABCMeta, abstractmethod


class NLP(metaclass=ABCMeta):
    @abstractmethod
    def tokenize_sentence(self, sentence: str) -> list:
        pass

    @abstractmethod
    def normalize_tokens(self, tokenized_sentence: list) -> list:
        pass

    @abstractmethod
    def suggest_next_word(self, normalized_tokens: list) -> list:
        pass
