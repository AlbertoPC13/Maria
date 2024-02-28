from word_suggestion.natural_language_processing_tools.NLPBert import NLPBert


class WordSuggestionService:
    def __init__(self):
        self.nlp = NLPBert()

    def suggest_next_word(self, sentence: str) -> list:
        tokenized_sentence = self.nlp.tokenize_sentence(sentence)
        normalized_sentence = self.nlp.normalize_tokens(tokenized_sentence)
        suggested_words = self.nlp.suggest_next_word(normalized_sentence)
        return suggested_words
