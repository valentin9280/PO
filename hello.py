#!/usr/bin/python

"""hello.py:simple hello world"""
import sys

def my_print():       # definition de fct
   if len(sys.argv)>=2:
     name=sys.argv[1]
   else:
     name='world'
   print 'Hello',name

if __name__== '__main__':
   my_print()
