from .NLP import NLP
import urllib.request
import json
import os
import ssl

class NLP_bert(NLP):
    def __init__(self):
        print("Se ha creado una instancia de NLP_bert")

    def tokenize_sentence(self,sentence):
        tokenized_sentence = sentence.split()
        return tokenized_sentence
    
    def normalize_sentence(self,tokenized_sentence):
        alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","á","é","í","ó","ú"," ","\n","ü",".","[","]"}

        normalized_sentence = []    
        
        for word in tokenized_sentence:
            if word == "[MASK]":
                normalized_sentence.append(word)
                continue
            
            normalized_word = ""
            
            for char in word:
                if char in alphabet:
                    normalized_word += char
            
            normalized_sentence.append(normalized_word)
        
        normalized_sentence = " ".join(normalized_sentence)
        return normalized_sentence

    def suggest_next_word(self,normalized_sentence):
        suggested_words = self.predict_with_bert(normalized_sentence)
        return suggested_words

    def allowSelfSignedHttps(self,allowed):
        # bypass the server certificate verification on client side
        if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
            ssl._create_default_https_context = ssl._create_unverified_context

    def predict_with_bert(self,normalized_sentence):
        self.allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

        url = os.environ.get('BERT_ENDPOINT')
        api_key = os.environ.get('BERT_API_KEY')

        data = { "inputs": normalized_sentence }       
        body = str.encode(json.dumps(data))

        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key), 'azureml-model-deployment': 'dccuchile-bert-base-spanish--12' }

        request = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(request)

            result = response.read()
            decoded_result = json.loads(result)
            suggested_words = [(item['token_str'],item['score']) for item in decoded_result]
            
            return suggested_words
        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))

            # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
            print(error.info())
            print(error.read().decode("utf8", 'ignore'))
