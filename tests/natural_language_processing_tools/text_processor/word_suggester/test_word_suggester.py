import time

import pytest
import pytest_mock
from dotenv import load_dotenv

from word_suggestion.natural_language_processing_tools.text_processor.word_suggester.WordSuggesterBert import \
    WordSuggesterBert


class TestWordSuggesterBert:
    @pytest.fixture
    def word_suggester_bert(self):
        word_suggester = WordSuggesterBert()
        time.sleep(1)
        return word_suggester

    @pytest.fixture(autouse=True)
    def load_env_variables(self):
        load_dotenv()

    # TODO: this suite needs more tests
    sentences = [
        "El bosque es un lugar mágico para las [MASK]",
        "Cuando alguien aprende a programar frecuentemente comete [MASK] fáciles de solucionar",
        "Por favor no me hagan entrar [MASK]",
        "Trata de no hacer [MASK]"
    ]

    @pytest.mark.word_suggester
    def test_suggest_next_word(self, word_suggester_bert, mocker):
        # Given
        sentence = "El bosque es un lugar mágico para las [MASK]"
        mocked_predictions = [{'token_str': 'bosque', 'score': '0.44048866629600525'},
                              {'token_str': 'infierno', 'score': '0.09329268336296082'},
                              {'token_str': 'cielo', 'score': '0.07073493301868439'},
                              {'token_str': 'castillo', 'score': '0.03358548879623413'},
                              {'token_str': '.', 'score': '0.019639084115624428'}]

        mock_get_predictions_from_bert_api = mocker.patch.object(
            WordSuggesterBert,
            "get_predictions_from_bert_api",
            return_value=mocked_predictions
        )

        scores_expected = [("bosque", "0.44048866629600525"), ("infierno", "0.09329268336296082"),
                           ("cielo", "0.07073493301868439"), ("castillo", "0.03358548879623413"),
                           (".", "0.019639084115624428")]

        # When
        suggested_words_with_scores = word_suggester_bert.suggest_next_word(sentence)

        # Then
        mock_get_predictions_from_bert_api.assert_called_once_with(sentence)
        assert suggested_words_with_scores == scores_expected

    @pytest.mark.parametrize("sentences", sentences)
    @pytest.mark.word_suggester
    def test_get_predictions_from_bert_api(self, word_suggester_bert, sentences):
        # Given sentences
        # When
        predictions = word_suggester_bert.get_predictions_from_bert_api(sentences)
        # Then
        assert predictions is not None
        assert len(predictions) > 0
        assert isinstance(predictions, list)

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
