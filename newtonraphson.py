import matplotlib.pyplot as plt
import numpy as np
import math

print('Metode Newton Raphson \n')
def f(x):
  return (2*x**2) - (5*x)

def f_aksen(x):
  return (4*x) - 5

e1 = 0.000001
e2 = 0.000000001
nMaks = 30
x = 1
i = 0
berhenti = False 
print('x','       selisih')
print(x)
while True:
  if (abs(f_aksen(x))< e2):
    berhenti = True
  else:
    x_sebelumnya = x
    x = x - (f(x)/f_aksen(x))
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