import matplotlib.pyplot as plt
import numpy as np
import math

print('Metode secant \n')
def f(x):
  return (2*x**2) - (5*x)

e1 = 0.000001
e2 = 0.000000001
nMaks = 30
x = 1
i = 0
x0 = 0.5
x1 = 1
berhenti = False 
print('x','       selisih')
print(x)
while True:
  if (abs(f(x1) - f(x0))< e2):
    berhenti = True
  else:
    x_sebelumnya = x1
    x = x - ((f(x1)*(x1-x0))/(f(x1)-f(x0)))
    x0 = x1
    x1 = x 
    i = i+1
    print(round(x,6), round(abs(x-x_sebelumnya),6))
  if (abs(x-x_sebelumnya) < e1 or berhenti or i > nMaks):
    break

if(berhenti):
  print('pembagian dengan 0')
else:
  if (i > nMaks):
    print('divergen')
  else:
    print('hasil akar = ',x)