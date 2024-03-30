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

    sentences = [
        "El bosque es un lugar mágico para las hadas",
        "Cuando alguien aprende a programar frecuentemente comete errores fáciles de solucionar",
        "Por favor no me hagan entrar ahí",
        "Trata de no hacer ruido",
    ]

    @pytest.mark.tokenizer
    @pytest.mark.parametrize("sentence", sentences)
    def test_tokenize_sentence_by_words(self, tokenizer_nltk, sentence):
        # Given sentences

        # When
        tokenized_sentence = tokenizer_nltk.tokenize_sentence_by_words(sentence)

        # Then
        assert tokenized_sentence is not None
        assert len(tokenized_sentence) > 0
        assert isinstance(tokenized_sentence, list)
        assert all(isinstance(token, str) for token in tokenized_sentence)
