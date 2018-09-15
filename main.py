#!/usr/bin/python

import sys
import os
import traceback
from wikipedia import Wikipedia


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage : python main.py <input-file-name>"
        sys.exit(1)

    input_filename = sys.argv[1]
    cwd = os.getcwd()
    configuration_file = os.path.join(cwd,"config", "app_config.json")
    if not os.path.isfile(configuration_file):
        print "cannot access file ", configuration_file
        sys.exit(1)

    try:
        wiki = Wikipedia(input_filename, configuration_file)        
        wiki.parse_input()
        wiki.calculate_and_print_answers()
    except Exception as e:
         print e
         #traceback.print_exc(file=sys.stdout)

