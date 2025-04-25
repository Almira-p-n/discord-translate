from translate import Translator
import requests
from collections import defaultdict

# Tugas #5
questions = {'siapa namamu' : "Aku adalah bot yang super keren dan diciptakan untuk membantumu!",
             "berapa usiamu" : "Itu adalah pertanyaan yang sangat filosofis..."}

class TextAnalysis():   
    
    memory = defaultdict(list)

    def __init__(self, text, owner):

        TextAnalysis.memory[owner].append(self)

        self.text = text
        self.translation = self.__translate(self.text, "id", "en")

        # Tugas #6
        if self.text.lower() in questions.keys():
            self.response = questions[self.text.lower()]
        else:
            self.response = self.get_answer()

    
    def get_answer(self):
        res = self.__translate("No sé cómo ayudar", "es", "en")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator = Translator(from_lang= from_lang, to_lang= to_lang)
            translation = translator.translate(text)
            return translation
        except:
            return "Gagal menerjemahkan"