from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

from word_suggestion.word_suggestion_controller import word_suggestion_api
import os

app = Flask(__name__)

CORS(app, resources={r"/word_suggestion/*": {"origins": "*"}})

if os.path.exists('.env'):
     load_dotenv()

app.register_blueprint(word_suggestion_api, url_prefix='/word_suggestion')

if __name__ == '__main__':
    app.run(debug=True)
