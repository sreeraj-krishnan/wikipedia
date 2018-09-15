import copy

class QuestionAnswer(object):
        def __init__(self, question):
            self.question = question
            self.answer = None


        def find_answer(self, paragraph, possible_answers):

            possible_lines = set()
            all_possible_lines = set()
            line_count = {}
            for word in self.question.split(' '):
                word = word.lower().strip().replace('?','').replace('\n','').replace('\r','').replace(',','').replace('-','').replace(':','')
                if word in paragraph.skip_words:
                    continue
                if word in paragraph.keywords.keys():
                    all_possible_lines.union(paragraph.keywords[ word ])
                    if  len(paragraph.keywords[ word ]) == 1:
                            possible_lines = paragraph.keywords[ word ]
                            s =  copy.deepcopy(paragraph.keywords[ word ])
                            val = s.pop()
                            line_count[ val ]  = 1
                            break; 
                    else:
                            temp = paragraph.keywords[ word ]
                            temp = temp.intersection( all_possible_lines )
                            if len(temp) > 0:
                                possible_lines = temp
                            else:
                                possible_lines = possible_lines.union( paragraph.keywords[ word ] )
                            for l in possible_lines :
                                if l in line_count:
                                    line_count[ l ] += 1
                                else:
                                    line_count[l] = 1
                            

            if len(possible_lines) > 0 :
                a1_sorted_keys = sorted(line_count, key=line_count.get, reverse=True)
                for answer_line in a1_sorted_keys:
                    if answer_line in possible_lines:
                        for given_answer in possible_answers.get_answers():
                            if paragraph.lines[answer_line].decode('utf-8').lower().find(given_answer.decode('utf-8').strip().lower()) != -1:
                                self.answer = given_answer.strip()
                                possible_answers.answers.remove(given_answer)
                                return True
            
            return False
    
        def set_answer(self, answer):
            self.answer = answer.strip()

        def get_answer(self):
            return self.answer
