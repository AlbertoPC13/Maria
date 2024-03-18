import pytest
from dotenv import load_dotenv

from word_suggestion.natural_language_processing_tools.text_processor.word_suggester.WordSuggesterBert import \
    WordSuggesterBert


class TestWordSuggesterBert:
    @pytest.fixture
    def word_suggester_bert(self):
        return WordSuggesterBert()

    @pytest.fixture(autouse=True)
    def load_env_variables(self):
        load_dotenv()

    # TODO: this method returns an error in the response, check why
    # TODO: this suite needs more tests
    def test_get_predictions_from_bert_api(self, word_suggester_bert):
        # Given
        sentence = "El bosque es un lugar mágico para las"
        # When
        predictions = word_suggester_bert.get_predictions_from_bert_api(sentence)
        print(predictions)
        # Then
        assert predictions is not None

    @pytest.mark.word_suggester
    def test_extract_word_scores_from_api_response(self, word_suggester_bert):
        # Given
        response_from_bert = [{'token_str': 'bosque', 'score': '0.44048866629600525'},
                              {'token_str': 'infierno', 'score': '0.09329268336296082'},
                              {'token_str': 'cielo', 'score': '0.07073493301868439'},
                              {'token_str': 'castillo', 'score': '0.03358548879623413'},
                              {'token_str': '.', 'score': '0.019639084115624428'}]
        expected_word_scores = [("bosque", "0.44048866629600525"), ("infierno", "0.09329268336296082"),
                                ("cielo", "0.07073493301868439"), ("castillo", "0.03358548879623413"),
                                (".", "0.019639084115624428")]
        # When
        word_scores = word_suggester_bert.extract_word_scores_from_api_response(response_from_bert)
        # Then
        assert word_scores == expected_word_scores
