import re
from app_config import AppConfig as config
import copy

class Paragraph(object):
        def __init__(self, paragraph, appconfig):
            self.paragraph = paragraph
            self.lines = []
            self.appconfig = appconfig

            # keywords to line
            self.keywords = {}
            self.skip_words=[]
            temp = appconfig.get_value('skip_words')
            for word in temp:
                 self.skip_words.append(word)


        def get_line(self):
            total_len = 0

            for line in self.paragraph.split('.'):
                total_len += len(line)
                if total_len > self.appconfig.get_value('paragraph_length'):
                    raise ValueError('input exceeds ' + str(self.appconfig.get_value('paragraph_length')) + ' characters')
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
                    token = token.strip().lower().replace(',','').replace('.','').replace('(','').replace(')','').replace('[','').replace(']','').replace('-','').replace(':','')
                    
                    if unicode(token,encoding='utf-8') not in self.skip_words:
                        if token in self.keywords:
                            self.keywords[ token ].add(line_number)
                        else:
                            self.keywords[ token ] = set()
                            self.keywords[ token ].add(line_number)


                line_number += 1

            
            #self.debug_file()
