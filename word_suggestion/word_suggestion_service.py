from word_suggestion.natural_language_processing_tools.text_preprocessing.normalizer import Normalizer
from word_suggestion.natural_language_processing_tools.text_preprocessing.tokenizer import Tokenizer
from word_suggestion.natural_language_processing_tools.text_processor.word_suggester import WordSuggester
import logging

class WordSuggestionService:
    def __init__(self, tokenizer: Tokenizer, normalizer: Normalizer, word_suggester: WordSuggester):
        self.tokenizer = tokenizer
        self.normalizer = normalizer
        self.word_suggester = word_suggester

    def suggest_next_word(self, sentence: str) -> list:
        normalized_sentence = self.prepare_sentence(sentence)
        suggested_words = self.word_suggester.suggest_next_word(normalized_sentence)
        return suggested_words

    def prepare_sentence(self, sentence: str) -> str:
        logging.warning(f"Received request for sentence: {sentence}")
        tokenized_sentence = self.tokenizer.tokenize_sentence_by_words(sentence)
        normalized_sentence_tokens = self.normalizer.normalize_tokens(tokenized_sentence)
        normalized_sentence_string = self.recover_sentence_from_tokens(normalized_sentence_tokens)
        masked_sentence = self.add_mask_to_sentence(normalized_sentence_string)
        return masked_sentence

    @staticmethod
    def recover_sentence_from_tokens(tokens: list) -> str:
        sentence = " ".join(tokens)
        return sentence

    @staticmethod
    def add_mask_to_sentence(sentence: str) -> str:
        sentence_with_mask = sentence + " [MASK]"
        return sentence_with_mask