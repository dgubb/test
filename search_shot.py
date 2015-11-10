#!/usr/bin/env python

import numpy
import sys

def process_file(file):
   data = numpy.loadtxt(fname=file, delimiter=',')
   if data[2,0] < 2:
      print( file,data[2,0])

if __name__ == "__main__":
   for file in sys.argv[1]:
      try:
         process_file(file)
      except:
         print("bad input file")
