from .NLP import NLP
from transformers import AutoTokenizer, AutoModelForMaskedLM
import torch

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
        tokenizer, model = self.load_bert_model()
        tokens ,input_ids = self.tokenize_sentence_with_bert(tokenizer,normalized_sentence)
        tensor = self.convert_input_ids_to_tensor(input_ids)
        output = self.get_output_from_bert_model(model,tensor)
        mask_index = self.get_mask_index(tokens)
        output_mask = self.get_output_for_mask(output,mask_index)
        probabilities = self.apply_softmax_to_output(output_mask)
        top_probabilities, top_indexes = self.get_top_probabilities_and_indexes(probabilities)
        top_tokens = self.convert_indexes_to_tokens(tokenizer,top_indexes)
        suggested_words= self.get_suggested_words(top_tokens,top_probabilities)
        return suggested_words
    
    def load_bert_model(self):
        tokenizer = AutoTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-cased")
        model = AutoModelForMaskedLM.from_pretrained("dccuchile/bert-base-spanish-wwm-cased")
        return tokenizer, model

    def tokenize_sentence_with_bert(self,tokenizer,normalized_sentence):
        tokens = tokenizer.tokenize(normalized_sentence)
        input_ids = tokenizer.convert_tokens_to_ids(tokens)
        return tokens, input_ids
    
    def convert_input_ids_to_tensor(self,input_ids):
        tensor = torch.tensor([input_ids])
        return tensor
    
    def get_output_from_bert_model(self,model,tensor):
        output = model(tensor)
        return output
    
    def get_mask_index(self,tokens):
        mask_index = tokens.index("[MASK]")
        return mask_index
    
    def get_output_for_mask(self,output,mask_index):
        output_mask = output[0][0][mask_index]
        return output_mask
    
    def apply_softmax_to_output(self,output_mask):
        probabilities = torch.nn.functional.softmax(output_mask, dim=0)
        return probabilities
    
    def get_top_probabilities_and_indexes(self,probabilities):
        top_probabilities, top_indexes = torch.topk(probabilities, 5)
        return top_probabilities, top_indexes
    
    def convert_indexes_to_tokens(self,tokenizer,top_indexes):
        top_tokens = tokenizer.convert_ids_to_tokens(top_indexes)
        return top_tokens
    
    def get_suggested_words(self,top_tokens,top_probabilities):
        suggested_words = []
        for token, prob in zip(top_tokens, top_probabilities):
            if token == "[UNK]":
                continue
            suggested_words.append((str(token),str(prob.item())))
        return suggested_words