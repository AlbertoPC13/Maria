from abc import ABCMeta, abstractmethod


class Normalizer(metaclass=ABCMeta):
    @abstractmethod
    def normalize_tokens(self, text: str) -> list:
        pass
