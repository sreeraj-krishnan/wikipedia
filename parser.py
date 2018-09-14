import sys
import os
import re
from paragraph import Paragraph
from question_answer import QuestionAnswer
from possible_answers import PossibleAnswers

class Parser(object):

    lines=[]

    def __init__(self, filename,appconfig):
        self.filename = filename
        self.fullpath = unicode()
        self.appconfig = appconfig

    def readlines(self):
        fileobj = open(self.filename, 'r')
        for line in fileobj.xreadlines():
            yield line

        fileobj.close()

    
    def parse_next_line(self):

        return self.parse_line()

    def parse_line(self):
        line_number = 1
        qline_begin = self.appconfig.get_value('question_lines','start')
        qline_end   = self.appconfig.get_value('question_lines','end')
        possible_answer_line = self.appconfig.get_value('possible_answers_line')

	for line in self.readlines():
            
            if line_number == self.appconfig.get_value('paragraph_line'):
                para = Paragraph(line, self.appconfig)
		para.parse()
                yield ("paragraph", para)

            elif line_number >= qline_begin and line_number <= qline_end:
                line.replace('?','')
                qa = QuestionAnswer(line)
                yield ("question_answer" , qa)

            elif line_number == possible_answer_line:
                pa = PossibleAnswers(line, self.appconfig) 
                pa.parse()
                yield ("possible_answers" , pa)

            else:
                raise ValueError('Invalid input, number of lines exceeded')
            
            line_number += 1


