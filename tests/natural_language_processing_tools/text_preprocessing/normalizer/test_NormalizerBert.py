import pytest

from word_suggestion.natural_language_processing_tools.text_preprocessing.normalizer.NormalizerBert \
    import (NormalizerBert)


class TestNormalizerBert:
    @pytest.fixture
    def normalizer_bert(self):
        return NormalizerBert()

    tokenized_sentences = [
        ["El", "BOSQUE", "es", "un", "lugar", "mágico", "para", "las", "hadas!!!"],
        ["Cuando", "alguien", "aprende", "a", "PROGRAMAR", "frecuentemente", "comete", "errores", "fáciles", "de",
         "solucionar!!!"],
        ["¡", "Por", "favor", "no", "me", "HAGAN", "entrar", "ahí", "!"],
    ]

    tokens = ["el11", "bosqu3", "es&", "un5", "luga7r", "{mágico}", "par5a", "las", "had55as!!!",]

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
    @pytest.mark.parametrize("sentence", tokenized_sentences)
    def test_normalize_tokens(self, normalizer_bert, sentence):
        # Given sentence
        # When
        normalized_sentence = normalizer_bert.normalize_tokens(sentence)
        # Then
        assert normalized_sentence is not None
        assert isinstance(normalized_sentence, list)
        assert len(normalized_sentence) > 0

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
    @pytest.mark.parametrize("sentence", tokenized_sentences)
    def test_transform_tokens_to_lowercase(self, normalizer_bert, sentence):
        # Given sentence
        # When
        lowercase_tokens = normalizer_bert.transform_tokens_to_lowercase(sentence)
        # Then
        assert lowercase_tokens is not None
        assert isinstance(lowercase_tokens, list)
        assert len(lowercase_tokens) > 0

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
    @pytest.mark.parametrize("sentence", tokenized_sentences)
    def test_normalize_lowercase_tokens(self, normalizer_bert, sentence):
        # Given sentence
        # When
        normalized_tokens = normalizer_bert.normalize_lowercase_tokens(sentence)
        # Then
        assert normalized_tokens is not None
        assert isinstance(normalized_tokens, list)
        assert len(normalized_tokens) > 0

    @pytest.mark.normalizer
    def test_remove_non_alphabet_characters(self, normalizer_bert):
        # Given
        token = "{toke1nvalido}"
        expected_normalized_token = "tokenvalido"
        # When
        normalized_token = normalizer_bert.remove_non_alphabet_characters(token)
        # Then
        assert normalized_token == expected_normalized_token

    @pytest.mark.normalizer
    @pytest.mark.parametrize("token", tokens)
    def test_remove_non_alphabet_characters(self, normalizer_bert, token):
        # Given sentence
        # When
        normalized_sentence = normalizer_bert.remove_non_alphabet_characters(token)
        # Then
        assert normalized_sentence is not None
        assert isinstance(normalized_sentence, str)
        assert [char in normalizer_bert.ALPHABET for char in normalized_sentence]
