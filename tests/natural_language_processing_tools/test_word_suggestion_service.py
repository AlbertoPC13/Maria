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
    def test_suggest_next_word(self, word_suggestion_service, mocker):
        # Given
        sentence = "El bosque es un lugar mágico para las"
        prepared_sentence = "El bosque es un lugar mágico para las [MASK]"
        expected_suggested_words = [("bosque", "0.44048866629600525"), ("infierno", "0.09329268336296082"),
                                    ("cielo", "0.07073493301868439"), ("castillo", "0.03358548879623413"),
                                    (".", "0.019639084115624428")]

        # Mock the prepare_sentence method
        mock_prepare_sentence = mocker.patch.object(
            WordSuggestionService,
            "prepare_sentence",
            return_value=prepared_sentence
        )

        # Mock the suggest_next_word method of word_suggester
        mock_suggest_next_word = mocker.patch.object(
            WordSuggesterBert,
            "suggest_next_word",
            return_value=expected_suggested_words
        )

        # When
        suggested_words = word_suggestion_service.suggest_next_word(sentence)

        # Then
        mock_prepare_sentence.assert_called_once_with(sentence)
        mock_suggest_next_word.assert_called_once_with(prepared_sentence)
        assert suggested_words == expected_suggested_words

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
