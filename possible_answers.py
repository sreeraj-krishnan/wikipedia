
from app_config import AppConfig

class PossibleAnswers(object):

    def __init__(self, answers, appconfig):

        self.answers_input = answers
        self.appconfig = appconfig
        self.answers = set()


    def get_answers(self):
        return self.answers

    def parse(self):
        #for answer in self.answers_input.split( self.appconfig.get_value("possible_answer_delimiter")):
        for answer in self.answers_input.split(';'):
            self.answers.add(answer)
