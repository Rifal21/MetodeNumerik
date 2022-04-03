import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
  return (2*x**2) - (5*x)

  
print('metode regula-falsi')
print('\n')

e1 = 0.000001
e2 = 0.00000001
a = -1
b = 2
i = 0

while True:
  print('iterasi ke-',(i+1))
  c = b - (f(b)*(b-a)/(f(b)-f(a)))
  if (abs(f(c)) < e2):
    a = c
    b = c
    break
  else:
    if (f(a)*f(c) < 0):
      print('a = ',a)
      print('b = ',b)
      print('c = ',c)
      print('f(a) = ',f(a))
      print('f(b) = ',f(b))
      print('f(c) = ',f(c))
      b = c 
    else:
      print('a = ',a)
      print('b = ',b)
      print('c = ',c)
      print('f(a) = ',f(a))
      print('f(b) = ',f(b))
      print('f(c) = ',f(c))
      a = c
  i += 1
  print()
  if (abs(a-b) < e1):
    break
  
  
print('hasil akar = ',c)