from .Tokenizer import Tokenizer
from nltk import word_tokenize


class TokenizerNltk(Tokenizer):
    def __init__(self):
        pass

    def tokenize_sentence_by_words(self, sentence: str) -> list:
        tokenized_sentence = word_tokenize(sentence)
        return tokenized_sentence
