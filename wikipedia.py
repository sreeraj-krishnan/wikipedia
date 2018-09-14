from app_config import AppConfig
from parser import Parser
from possible_answers import PossibleAnswers
class Wikipedia(object):

    def __init__(self, input_file, appconfig_file):

        self.input_filename = input_file
        self.appconfig = AppConfig(appconfig_file)

        self.parser = Parser(self.input_filename, self.appconfig)
        
        self.question_answer = []
        self.paragraph = None
        self.possible_answers = None


    def parse_input(self):

        for token in self.parser.parse_next_line():
            Type = token[0]
            Object = token[1]
            if Type == "paragraph":
                self.paragraph = Object

            elif Type == "question_answer":
                self.question_answer.append( Object )

            elif Type == "possible_answers":
                self.possible_answers = Object
            
            else:
                raise ValueError('Invalid input, parsing failed') 


    def calculate_and_print_answers(self):
        for question in self.question_answer:
            #print question.get_question()
            if question.find_answer(self.paragraph , self.possible_answers):
                print question.get_answer()
            else:
                print 'Could not find the answer'

