import nltk
from text2text.text_generator import TextGenerator
import wikipedia
import re
from googletrans import Translator
from nltk.tokenize import sent_tokenize


def get_page():
    title = wikipedia.random()
    page = wikipedia.page(title=title)
    return title, page


class QuestionAnswer:
    question = ''
    answer = ''

    def __init__(self):
        self.stops = nltk.download("stopwords")
        self.qg = TextGenerator(output_type="question")
        self.translator = Translator()

    def predict(self):
        en_text = self.make_text()
        question = self.qg.predict([en_text])
        self.question = self.translator.translate(question[0][0], src='en', dest='ru').text
        self.answer = self.translator.translate(question[0][1], src='en', dest='ru').text

    def get_answer(self):
        return self.answer

    def get_question(self):
        answer = ''
        if len(self.question.split()) > 4:
            count = 0
            for i in self.question.split():
                count += 1
                answer += i
                answer += " "
                if count == 4:
                    answer += '\n'

        else:
            answer = self.question

        return answer

    @staticmethod
    def make_text():
        nltk.download('punkt')
        title, page = get_page()
        while 2000 > len(page.content) > 10000:
            title, page = get_page()
        print(title)
        text = page.content
        text = re.sub("\n", "", text)
        text = text.split("== References", 1)[0]
        text = text.split("== Notes", 1)[0]
        text = text.split("== See also", 1)[0]
        text = sent_tokenize(text)
        text = text[:3]
        text = '. '.join(text)
        text += " [SEP] "
        text += title
        print(text)
        return text


