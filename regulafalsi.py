import matplotlib.pyplot as plt
import numpy as np
import math

print('Metode Reguola-falsi \n')

# deklarasi fungsi f(x)
def f(x):
  return (2*x**2) - (5*x)

# variabel yang sudah diketahui
a = -1 
b = 2
# n = 10
# taksiran nilai presisi 
prs1 = 0.000001
prs2 = 0.00000001
i = 0

while True:
  print('Iterasi ke-',(i+1))
  # rumus regula falsi
  c = b - (f(b)*(b-a)/(f(b) - f(a)))
  # jika nilai mutlak f(c) kurang dari nilai presisi2 maka a = c dan b = c lalu hentikan
  if (abs(f(c)) < prs2):
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
  # jika nilai mutlak a - b kurang dari presisi satu maka berhenti dan ambil nilai c terakhir sebagai nilai akar 
  if(abs(a-b) < prs1):
    break

print('Nilai Akar = ', c)