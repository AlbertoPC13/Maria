from abc import ABCMeta, abstractmethod


class Normalizer(metaclass=ABCMeta):
    @abstractmethod
    def normalize_tokens(self, tokenized_sentence: str) -> list:
        pass
