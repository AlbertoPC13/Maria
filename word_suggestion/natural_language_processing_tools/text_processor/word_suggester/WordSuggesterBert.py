from .WordSuggester import WordSuggester
import os
import requests


class WordSuggesterBert(WordSuggester):
    def __init__(self):
        self.API_URL = os.environ.get('API_URL')
        API_TOKEN = os.environ.get('API_TOKEN')
        self.headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def suggest_next_word(self, normalized_sentence: str) -> list:
        response_from_bert = self.get_predictions_from_bert_api(normalized_sentence)
        suggested_words_with_scores = self.extract_word_scores_from_api_response(response_from_bert)
        return suggested_words_with_scores

    def get_predictions_from_bert_api(self, sentence: str) -> list:
        input_data = {"inputs": sentence}
        response = requests.post(self.API_URL, headers=self.headers, json=input_data)
        return response.json()

    @staticmethod
    def extract_word_scores_from_api_response(response_from_bert):
        return [(item['token_str'], item['score']) for item in response_from_bert]
