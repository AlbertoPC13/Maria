from word_suggestion.natural_language_processing_tools.NLP_bert import NLP_bert

class WordSuggestionService:
    def __init__(self):
        print("WordSuggestionService has been created")

    def suggest_next_word(self,sentence):
        nlp = NLP_bert()
        sentence = sentence + " [MASK]"
        tokenized_sentence = nlp.tokenize_sentence(sentence)
        normalized_sentence = nlp.normalize_sentence(tokenized_sentence)
        suggested_words = nlp.suggest_next_word(normalized_sentence)
        print(suggested_words)
        return suggested_words