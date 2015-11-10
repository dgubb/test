#!/usr/bin/env python

import numpy
import sys

def process_file(file):
   data = numpy.loadtxt(fname=file, delimiter=',')
   if data[2,0] < 2:
      return file,data[2,0]
   else:
      return file, None

if __name__ == "__main__":
   for file in sys.argv[1:]:
      try:
         print( process_file(file))
      except:
         print("bad input file")
