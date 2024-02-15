from flask import Blueprint, jsonify
from .word_suggestion_service import WordSuggestionService

word_suggestion_api = Blueprint('word_suggestion_api', __name__)

@word_suggestion_api.route('/<sentence>', methods=['GET'])
def suggest_word(sentence):
    service = WordSuggestionService()
    result = service.suggest_next_word(sentence)
    return jsonify(result), 200