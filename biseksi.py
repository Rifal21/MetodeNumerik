from pickle import TRUE
import matplotlib.pyplot as plt
import numpy as np
import math

print('Metode Biseksi \n')

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

# looping untuk mencari hasil akar 
while True:               
  print('iterasi ke-',(i+1))
  # cari nilai c sebagai nilai tengah
  c = (a+b)/2
  # jika fungsi batas atas kali fungsi batas bawah bernilai kurang dari 0 maka lakukan perulangan dengan nilai batas bawah = nilai c 
  if (f(a)*f(c) < 0):
    print('nilai a = ', a)
    print('nilai b = ', b)
    print('nilai c = ', c)
    print('nilai f(a) = ', f(a))
    print('nilai f(b) = ', f(b))
    print('nilai f(c) = ', f(c))
    b = c
    # jika fungsi batas atas kali fungsi batas bawah lebih besar dari 0 maka nilai batas atas diambil dari nilai c dari iterasi sebelumnya
  else:
    print('nilai a = ', a)
    print('nilai b = ', b)
    print('nilai c = ', c)
    print('nilai f(a) = ', f(a))
    print('nilai f(b) = ', f(b))
    print('nilai f(c) = ', f(c))
    a = c

  i += 1
  print()
  if(abs(a-b) < prs1 or abs(f(c)) < prs2):
    break

print('hasil akar = ',c) 
  
