#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')  


from langdetect import detect
from langdetect import detect_langs
import unicodedata as uc
from langdetect import DetectorFactory
import re
from arabish import transliterate

import nltk
from nltk import word_tokenize,sent_tokenize
from nltk.tokenize import sent_tokenize

DetectorFactory.seed = 0

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
# first_name = form.getvalue('first_name')
# last_name  = form.getvalue('last_name')
# tweet  = form.getvalue('tweet')

def detect_language(input_str):
    res = detect_langs(input_str)
    for item in res:
      return item.lang 
         
        



print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<head>'
print '<title>Tweet info</title>'
print '</head>'

input_str =form.getvalue('tweet')
input_str = unicode(input_str, "utf-8")
#input_str = input_str.encode('utf-8')
print "<h3>your tweet is =========================  %s </h3>" % (input_str.encode('utf-8'))
lang = detect_language(input_str)
if lang == "ar":
  print "<h4>language is Arabic </h4>"
elif lang =="en":
  print "<h4>language is English </h4>"
else:
  print "<h4>language is Franco </h4>"
  print transliterate(input_str.encode('utf-8'))

print '</html>'
