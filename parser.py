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
        self.fullpath=self.filename
        cwd = os.getcwd()
        if not os.path.isfile(self.filename):
            self.fullpath = os.path.join(cwd , self.filename)
            if not os.path.isfile(self.fullpath):
                print "File ", self.filename  ," does not exist "
                sys.exit(0)
        else:
            self.fullpath = self.filename

        try:
            fileobj = open(self.fullpath, 'r')
            for line in fileobj.xreadlines():
                yield line

            fileobj.close()

        except Exception as e:
            print e , 'readlines'

    """ 
    """

    def parse_next_line(self):

        try:
            return self.parse_line()
        except Exception as e:
            print e, 'parse_next_line'

    def parse_line(self):
        line_number = 1
        qline_begin = self.appconfig.get_value('question_lines','start')
        qline_end   = self.appconfig.get_value('question_lines','end')
        possible_answer_line = self.appconfig.get_value('possible_answers_line')

	for line in self.readlines():
            
            #line = re.sub(r'\W+','',line)
            #print line
            if line_number == self.appconfig.get_value('paragraph_line'):
                para = Paragraph(line, self.appconfig)
		para.parse()
                yield ("paragraph", para)

            elif line_number >= qline_begin and line_number <= qline_end:
                line.replace('?','')
                qa = QuestionAnswer(line)
                yield ("question_answer" , qa)

            elif line_number == possible_answer_line:
                #print line
                pa = PossibleAnswers(line, self.appconfig) 
                pa.parse()
                yield ("possible_answers" , pa)

            else:
                raise ValueError('Invalid input, number of lines exceeded')
            
            line_number += 1
            #print line_number


