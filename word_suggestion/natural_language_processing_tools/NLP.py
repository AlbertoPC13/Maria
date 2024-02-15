from abc import ABCMeta, abstractmethod

class NLP(metaclass=ABCMeta):    
    @abstractmethod
    def tokenize_sentence(self,sentence):
        pass

    @abstractmethod
    def normalize_sentence(self,tokenized_sentence):
        pass

    @abstractmethod
    def suggest_next_word(self,normalized_sentence):
        pass