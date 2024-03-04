from .WordSuggester import WordSuggester
import os
import requests


class WordSuggesterBert(WordSuggester):
    def __init__(self):
        self.API_URL = os.environ.get('API_URL')
        API_TOKEN = os.environ.get('API_TOKEN')
        self.headers = {"Authorization": f"Bearer {API_TOKEN}"}

    def suggest_next_word(self, normalized_sentence: str) -> list:
        suggested_words = self.predict_next_word_with_bert(normalized_sentence)
        return suggested_words

    def predict_next_word_with_bert(self, sentence: str) -> list:
        response_from_bert = self.get_predictions_from_bert_api(sentence)
        suggested_words = [(item['token_str'], item['score']) for item in response_from_bert]
        return suggested_words

    def get_predictions_from_bert_api(self, sentence: str) -> list:
        input_data = {"inputs": sentence}
        response = requests.post(self.API_URL, headers=self.headers, json=input_data)
        return response.json()
