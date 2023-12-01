import spacy
import requests
from collections import defaultdict
from datetime import datetime
from data_processing import preprocess_input, extract_entities

class ChatbotModel:
    def __init__(self):
        self.nlp = spacy.load("fr_core_news_sm")
        self.conversations = defaultdict(list)

    def train(self, user_input, model_response):
        self.conversations[user_input].append(model_response)

    def get_current_datetime(self):
        return datetime.now().strftime("Aujourd'hui nous sommes le %Y-%m-%d et il est actuellement %H:%M:%S.")



    def generate_response(self, input_text):
        processed_input = preprocess_input(input_text, self.nlp)
        entities = extract_entities(processed_input)

        generated_response = "Je ne comprends pas la question."

        if "heure" in entities and "est" in entities:
            generated_response = self.get_current_datetime()

        elif input_text in self.conversations:
            generated_response = " ".join(self.conversations[input_text])

        return generated_response
