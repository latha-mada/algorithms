#!/usr/bin/python

import os

def print_directory_contents(sPath):
   print 'contents in this directory are:'
   for contents in os.listdir(sPath):
       if os.path.isdir(contents):
	  print '----'+contents+':'
          print_directory_contents(os.path.join(sPath,contents))
       else:
          print contents
sPath = '/Users/gummida/latha/python-code'
print_directory_contents(sPath)
