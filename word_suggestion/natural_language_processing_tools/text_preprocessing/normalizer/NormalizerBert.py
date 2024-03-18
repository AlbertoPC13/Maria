from .Normalizer import Normalizer


class NormalizerBert(Normalizer):
    def __init__(self):
        self.ALPHABET = {
            "a", "b", "c", "d", "e", "f", "g", "h", "i",
            "j", "k", "l", "m", "n", "ñ", "o", "p", "q",
            "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "á", "é", "í", "ó", "ú", " ", "\n", "ü", ".", "[", "]"
        }

    def normalize_tokens(self, tokenized_sentence: list) -> list:
        lowercase_tokens = self.transform_tokens_to_lowercase(tokenized_sentence)
        normalized_tokens = self.normalize_lowercase_tokens(lowercase_tokens)
        return normalized_tokens

    @staticmethod
    def transform_tokens_to_lowercase(tokenized_sentence: list) -> list:
        lowercase_tokens = [token.lower() for token in tokenized_sentence]
        return lowercase_tokens

    def normalize_lowercase_tokens(self, lowercase_tokens: list) -> list:
        normalized_tokens = []

        for token in lowercase_tokens:
            normalized_token = self.remove_non_alphabet_characters(token)
            if len(normalized_token) > 0:
                normalized_tokens.append(normalized_token)

        return normalized_tokens

    def remove_non_alphabet_characters(self, token: str) -> str:
        normalized_token = ''.join(
            char for char in token
            if char in self.ALPHABET
        )

        return normalized_token
