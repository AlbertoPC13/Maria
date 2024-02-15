from flask import Flask
from word_suggestion.word_suggestion_controller import word_suggestion_api

app = Flask(__name__)

# Registrar el blueprint del controlador gramatical_analysis
app.register_blueprint(word_suggestion_api, url_prefix='/word_suggestion')

if __name__ == '__main__':
    app.run(debug=True)