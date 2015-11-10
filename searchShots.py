#!/usr/bin/env python

import numpy
import sys

def process_file(file):
   data = numpy.loadtxt(fname=file, delimiter=',')
   if data[2,0] < 2:
      print( file,data[2,0])


input_len=len(sys.argv)
if input_len !=2:
   print('incorrect number of inputs')
   sys.exit(1)

file = sys.argv[1]

process_file(file)

