import re
from app_config import AppConfig as config
import copy

class Paragraph(object):
        def __init__(self, paragraph, appconfig):
            self.paragraph = paragraph
            self.lines = []

            # keywords to line
            self.keywords = {}
            self.skip_words=[]
            temp = appconfig.get_value('skip_words')
            for word in temp:
                 self.skip_words.append(word)


        def get_line(self):

            for line in self.paragraph.split('.'):
                yield line
        

        def debug_file(self):
            out = open('debug', 'w+')
            i = 0
            for line in self.lines:
                msg =  str(i) + ' ' + line + '\n'
                out.write(msg)
                i += 1

            out.close()


        def parse(self):
            line_number = 0
            for line in self.get_line():
                self.lines.append(line)
                tokens = line.split()

                for token in tokens:
                    #token = re.sub(r'\W+','',token)
                    token = token.strip().lower().replace(',','').replace('.','').replace('(','').replace(')','').replace('[','').replace(']','')
                    
                    if unicode(token,encoding='utf-8') not in self.skip_words:
                        if token in self.keywords:
                            self.keywords[ token ].add(line_number)
                        else:
                            self.keywords[ token ] = set()
                            self.keywords[ token ].add(line_number)


                line_number += 1

            
            self.debug_file()
            
            #for key in self.keywords:
            #    print self.keywords[ key ]
