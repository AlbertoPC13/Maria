import pytest

from word_suggestion.natural_language_processing_tools.text_preprocessing.tokenizer.TokenizerNltk import TokenizerNltk


class TestTokenizerNltk:
    @pytest.fixture
    def tokenizer_nltk(self):
        return TokenizerNltk()

    @pytest.mark.tokenizer
    def test_tokenize_sentence_by_words(self, tokenizer_nltk):
        # Given
        sentence = "Esta es una oración de prueba. 12345, #$%"
        expected_tokenized_sentence = ["Esta", "es", "una", "oración", "de", "prueba", ".", "12345", ",", "#", "$", "%"]
        # When
        tokenized_sentence = tokenizer_nltk.tokenize_sentence_by_words(sentence)
        # Then
        assert tokenized_sentence == expected_tokenized_sentence
