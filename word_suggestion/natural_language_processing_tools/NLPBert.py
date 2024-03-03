from .NLP import NLP
from .text_preprocessing.normalizer.NormalizerBert import NormalizerBert
from .text_preprocessing.tokenizer.TokenizerNltk import TokenizerNltk
from .text_processor.WordSuggesterBert import WordSuggesterBert


class NLPBert(NLP):
    def __init__(self):
        self.tokenizer = TokenizerNltk()
        self.normalizer = NormalizerBert()
        self.word_suggester = WordSuggesterBert()

    def suggest_next_word(self, normalized_tokens: list) -> list:
        normalized_sentence = self.recover_sentence_from_tokens(normalized_tokens)
        masked_sentence = self.add_mask_to_sentence(normalized_sentence)
        print(masked_sentence)
        suggested_words = self.word_suggester.suggest_next_word(masked_sentence)
        return suggested_words

    @staticmethod
    def recover_sentence_from_tokens(tokens: list) -> str:
        sentence = " ".join(tokens)
        return sentence

    @staticmethod
    def add_mask_to_sentence(sentence: str) -> str:
        sentence_with_mask = sentence + " [MASK]"
        return sentence_with_mask

    def tokenize_sentence(self, sentence: str) -> list:
        tokenized_sentence = self.tokenizer.tokenize_sentence_by_words(sentence)
        return tokenized_sentence

    def normalize_tokens(self, tokenized_sentence: list) -> list:
        normalized_tokens = self.normalizer.normalize_tokens(tokenized_sentence)
        return normalized_tokens
