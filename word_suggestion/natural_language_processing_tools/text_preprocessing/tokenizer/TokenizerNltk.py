from .Tokenizer import Tokenizer
from nltk import word_tokenize
import nltk


class TokenizerNltk(Tokenizer):
    def __init__(self):
        nltk.download('punkt')

    def tokenize_sentence_by_words(self, sentence: str) -> list:
        tokenized_sentence = word_tokenize(sentence)
        return tokenized_sentence
