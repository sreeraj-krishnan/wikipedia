import sys
import json
import os
import codecs
from pprint import pprint
#from utils import validate_file

class JSONReader(object):
	
	def __init__(self, filename):
		self.filename = filename
	
	
	def get_json(self):
	    self.fullpath = self.filename
            if not os.path.isfile( self.filename):
                cwd = os.getcwd()
                self.fullpath = os.path.join(cwd , self.filename)
                if not os.path.isfile(fullpath):
                    print "File ", self.filename  ," does not exist "
                    return '{}'
            else:
                self.fullpath = self.filename
			
            with codecs.open(self.fullpath,encoding='utf-8') as data_file: 
		data = json.load(data_file)
		
            return data

'''
if __name__ == '__main__':
    pass
    #print str(j.get_json()['symbols'][0]['next_allowed_for_subtraction'][0])
'''
