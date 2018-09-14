

class QuestionAnswer(object):
        def __init__(self, question):
            self.question = question
            self.answer = None


        def find_answer(self, paragraph, possible_answers):

            possible_lines = set()
            for word in self.question.split(' '):
                word = word.lower().strip().replace('?','').replace('\n','').replace('\r','').replace(',','')
                if word in paragraph.skip_words:
                    continue
                #print 'question word' , word
                if word in paragraph.keywords.keys():
                    #print word , ' -> ' , paragraph.keywords[ word ]
                    if len(possible_lines) == 0:
                        possible_lines = paragraph.keywords[ word ]
                    else:
                        if  len(paragraph.keywords[ word ]) == 1:
                            possible_lines = paragraph.keywords[ word ]
                            break; 
                        else:
                            temp = possible_lines.intersection( paragraph.keywords[ word ] )
                            if len(temp) > 0:
                                possible_lines = temp
                            else:
                                possible_lines = possible_lines.union( paragraph.keywords[ word ] )
                            

                    #possible_lines = self.update_possible_lines( possible_lines, paragraph, word )
                    #print possible_lines
                else:
                    pass
                    #print 'not present ' , word , ' in paragraph.keywords'

            if len(possible_lines) > 0 :
                for answer_line in possible_lines:
                    #print answer_line
                    for given_answer in possible_answers.get_answers():
                        #print paragraph.lines[answer_line].decode('utf-8') , ' -> ' , given_answer.decode('utf-8')
                        if paragraph.lines[answer_line].decode('utf-8').lower().find(given_answer.decode('utf-8').strip().lower()) != -1:
                            self.answer = given_answer.strip()
                            possible_answers.answers.remove(given_answer)
                            #print ' length now -> ' , len(possible_answers.answers)
                            return True
            
            return False
    
        def set_answer(self, answer):
            self.answer = answer.strip()

        def get_answer(self):
            return self.answer
