#!/usr/bin/python

import os
import sys
import collections
import unittest
import traceback

from app_config import AppConfig
from parser import Parser
from possible_answers import PossibleAnswers
from paragraph import Paragraph
from question_answer import QuestionAnswer
from wikipedia import Wikipedia
from json_parser import JSONReader


class TestAll(unittest.TestCase):

    def no_answer_question(self):
        try:
            cwd = os.getcwd()
            configuration_file = os.path.join(cwd,"config", "app_config.json")
            wiki = Wikipedia('tests/err', configuration_file)
            wiki.parse_input()
            wiki.calculate_and_print_answers()
            self.assertEqual(False,"test faile")
        except Exception as e:
            print e
            self.assertEqual(True,True)

        try:
            wiki = Wikipedia('tests/test.input8', configuration_file)
            q = QuestionAnswer('why is the earth flat?')
            self.assertEqual( False, q.find_answer(wiki.paragraph, wiki.appconfig) )
        except Exception as e:
            self.assertEqual(False,"test faile")
            
    
    def input_error(self):
        cwd = os.getcwd()
        configuration_file = os.path.join(cwd,"config", "app_config.json")
        try:
            wiki = Wikipedia('tests/test.input8', configuration_file)
            wiki.parse_input()
            self.assertEqual(False,"test faile")
        except Exception as e:
            print e
            self.assertEqual(True,True)

    def test_app_config_exception(self):
        try:
            app = AppConfig('tests/1app_config.json')
            self.assertEqual(False,'Invalid file passed')
        except Exception as e:
            self.assertEqual(True,True)
    


    def test_json_parser(self):
        try:
            j = JSONReader('wetempfile')
            j.get_json()['re']
            self.assertEqual(False,'Shoud fail')
        except:
            self.assertEqual(True,True)
        

    def testAll(self):
        try:
            cwd = os.getcwd()
            configuration_file = os.path.join(cwd,"config", "app_config.json")
            wiki = Wikipedia('test.input', configuration_file)
            wiki.parse_input()
            wiki.calculate_and_print_answers()
            self.assertEqual(True,True)

        except Exception as e:
         print e
         traceback.print_exc(file=sys.stdout)
         self.assertEqual(True,False)
    
    def test_app_config(self):
        try:
            app = AppConfig('tests/app_config.json')
            self.assertEqual( app.get_value('question_lines','start') , 2 )
            self.assertEqual( app.get_value('question_lines','end') , 6 )
            self.assertEqual( app.get_value('paragraph_length'),5000)
            self.assertEqual(True,True)
        except Exception as e:
            print e
            traceback.print_exc(file=sys.stdout)
            self.assertEqual(False,'Shoutd not fail')

        try:
            self.assertEqual( app.get_value('paragraph_length',2323),5000)
            self.assertEqual(False,'Shoud fail')
        except:
            self.assertEqual(True,True)



if __name__ == '__main__':
    unittest.main()
