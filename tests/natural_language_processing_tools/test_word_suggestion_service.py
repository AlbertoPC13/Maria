import pytest

from word_suggestion.natural_language_processing_tools.text_preprocessing.normalizer.NormalizerBert import \
    NormalizerBert
from word_suggestion.natural_language_processing_tools.text_preprocessing.tokenizer.TokenizerNltk import TokenizerNltk
from word_suggestion.natural_language_processing_tools.text_processor.word_suggester.WordSuggesterBert import \
    WordSuggesterBert
from word_suggestion.word_suggestion_service import WordSuggestionService


class TestWordSuggestionService:

    @pytest.fixture
    def word_suggestion_service(self):
        tokenizer = TokenizerNltk()
        normalizer = NormalizerBert()
        word_suggester = WordSuggesterBert()
        return WordSuggestionService(tokenizer, normalizer, word_suggester)

    @pytest.mark.word_suggestion_service
    def test_prepare_sentence(self, word_suggestion_service):
        # Given
        sentence = "Vivieron felices para234#@  "
        expected_prepared_sentence = "vivieron felices para [MASK]"
        # When
        prepared_sentence = word_suggestion_service.prepare_sentence(sentence)
        # Then
        assert prepared_sentence == expected_prepared_sentence

    @pytest.mark.word_suggestion_service
    def test_recover_sentence_from_tokens(self, word_suggestion_service):
        # Given
        tokens = ["Vivieron", "felices", "para"]
        expected_sentence = "Vivieron felices para"
        # When
        sentence = word_suggestion_service.recover_sentence_from_tokens(tokens)
        # Then
        assert sentence == expected_sentence

    @pytest.mark.word_suggestion_service
    def test_add_mask_to_sentence(self, word_suggestion_service):
        # Given
        sentence = "Vivieron felices para"
        expected_sentence_with_mask = "Vivieron felices para [MASK]"
        # When
        sentence_with_mask = word_suggestion_service.add_mask_to_sentence(sentence)
        # Then
        assert sentence_with_mask == expected_sentence_with_mask
