from flask import Blueprint, jsonify, Response

from .natural_language_processing_tools.text_preprocessing.normalizer.NormalizerBert import NormalizerBert
from .natural_language_processing_tools.text_preprocessing.tokenizer.TokenizerNltk import TokenizerNltk
from .natural_language_processing_tools.text_processor.word_suggester.WordSuggesterBert import WordSuggesterBert
from .word_suggestion_service import WordSuggestionService
from http import HTTPStatus

word_suggestion_api = Blueprint('word_suggestion_api', __name__)

tokenizer = TokenizerNltk()
normalizer = NormalizerBert()
word_suggester = WordSuggesterBert()


@word_suggestion_api.route('/<sentence>', methods=['GET'])
def suggest_word(sentence: str) -> tuple[Response, int]:
    service = WordSuggestionService(tokenizer, normalizer, word_suggester)
    result = service.suggest_next_word(sentence)
    return jsonify(result), HTTPStatus.OK
