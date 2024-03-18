import pytest

from word_suggestion.natural_language_processing_tools.text_preprocessing.normalizer.NormalizerBert \
    import (NormalizerBert)


class TestNormalizerBert:
    @pytest.fixture
    def normalizer_bert(self):
        return NormalizerBert()

    @pytest.mark.normalizer
    def test_normalize_tokens(self, normalizer_bert):
        # Given
        tokenized_sentence = ["Esta", "es", "una", "oración", "de", "PRUEBA", ".", "&/"]
        expected_normalized_tokens = ["esta", "es", "una", "oración", "de", "prueba", "."]
        # When
        normalized_tokens = normalizer_bert.normalize_tokens(tokenized_sentence)
        # Then
        assert normalized_tokens == expected_normalized_tokens

    @pytest.mark.normalizer
    def test_transform_tokens_to_lowercase(self, normalizer_bert):
        # Given
        tokenized_sentence = ["Esta", "es", "UNA", "oracióN", "De", "PRUEBA", ".", "["]
        expected_lowercase_tokens = ["esta", "es", "una", "oración", "de", "prueba", ".", "["]
        # When
        lowercase_tokens = normalizer_bert.transform_tokens_to_lowercase(tokenized_sentence)
        # Then
        assert lowercase_tokens == expected_lowercase_tokens

    @pytest.mark.normalizer
    def test_normalize_lowercase_tokens(self, normalizer_bert):
        # Given
        lowercase_tokens = ["esta", "es", "una", "oración", "de", "prueba", ".", "1%", "#$"]
        expected_normalized_tokens = ["esta", "es", "una", "oración", "de", "prueba", "."]
        # When
        normalized_tokens = normalizer_bert.normalize_lowercase_tokens(lowercase_tokens)
        # Then
        assert normalized_tokens == expected_normalized_tokens

    @pytest.mark.normalizer
    def test_remove_non_alphabet_characters(self, normalizer_bert):
        # Given
        token = "{toke1nvalido}"
        expected_normalized_token = "tokenvalido"
        # When
        normalized_token = normalizer_bert.remove_non_alphabet_characters(token)
        # Then
        assert normalized_token == expected_normalized_token
