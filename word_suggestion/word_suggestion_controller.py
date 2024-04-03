from flask import Blueprint, jsonify, Response, request

from http import HTTPStatus

from word_suggestion.natural_language_processing_tools.text_preprocessing.normalizer.NormalizerBert import NormalizerBert
from word_suggestion.natural_language_processing_tools.text_preprocessing.tokenizer.TokenizerNltk import TokenizerNltk
from word_suggestion.natural_language_processing_tools.text_processor.word_suggester.WordSuggesterBert import WordSuggesterBert
from word_suggestion.word_suggestion_service import WordSuggestionService

word_suggestion_api = Blueprint('word_suggestion_api', __name__)

tokenizer = TokenizerNltk()
normalizer = NormalizerBert()
word_suggester = WordSuggesterBert()


@word_suggestion_api.route('', methods=['POST'])
def suggest_word() -> tuple[Response, int]:
    if request.is_json:
        data = request.get_json()
        text = data.get('text')
        if text:
            service = WordSuggestionService(tokenizer, normalizer, word_suggester)
            result = service.suggest_next_word(text)
            return jsonify(result), HTTPStatus.OK
        else:
            return jsonify(
                {'error': 'The "text" field is required on the body of the request'}), HTTPStatus.BAD_REQUEST
    else:
        return jsonify({'error': 'The request must be on JSON format'}), HTTPStatus.BAD_REQUEST

