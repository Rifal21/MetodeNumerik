import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
  return (2*x**2) - (5*x)
a= -1
b = 2
h = 0.3

x = a
print('Metode table \n NIM : 2003010025')
while(x <= b):
  print(round(x,2) , round(f(x),5))
  x += h



