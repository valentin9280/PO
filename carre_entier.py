#!/usr/bin/python

import sys
import math


print("\t\t\t Les carres des 10 premiers entiers\n\n")

def power(x):
  return x*x

L=range(10)

print (map(power,L))

