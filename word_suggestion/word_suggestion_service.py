from word_suggestion.natural_language_processing_tools.text_preprocessing.normalizer.NormalizerBert import \
    NormalizerBert
from word_suggestion.natural_language_processing_tools.text_preprocessing.tokenizer.TokenizerNltk import TokenizerNltk
from word_suggestion.natural_language_processing_tools.text_processor.word_suggester.WordSuggesterBert import \
    WordSuggesterBert


class WordSuggestionService:
    def __init__(self):
        self.tokenizer = TokenizerNltk()
        self.normalizer = NormalizerBert()
        self.word_suggester = WordSuggesterBert()

    def suggest_next_word(self, sentence: str) -> list:
        normalized_sentence = self.prepare_sentence(sentence)
        suggested_words = self.word_suggester.suggest_next_word(normalized_sentence)
        return suggested_words

    def prepare_sentence(self, sentence: str) -> str:
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
