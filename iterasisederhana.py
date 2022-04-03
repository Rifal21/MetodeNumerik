import matplotlib.pyplot as plt
import numpy as np
import math


print('Metode Iterasi Sedehana \n')
def f(x):
  return (2*x**2) - (5*x)
# mecari nilai g(x) dari persamaan 2x^2 - 5x => diturunkan menjadi 4x - 5 = 0, kemudian dipindah ruaskan menjadi 4x = 5, lalu dihasilkan nilai x = 5/4
def g(x):
  return 5/4

epsilon = 0.000001 
nMaks = 30
i = 0
x = 4

print('x','       selisih')
print(x)
while True:
  #x_sebelumnya sama dengan nilai awal yang kemudian nilai x akan disubtitusi dengan nilai g(x) untuk perhitungan selanjutnya
  x_sebelumnya = x
  x = g(x)
  i += 1
  # cetak nilai x yang dibulatkan sebanyak 6 kali serta cetak nilai mutlak x dikurangi nilai x_sebelumnya yang dibulatkan juga sebanyak 6 kali
  print(round(x,6), round(abs(x-x_sebelumnya),6))
  #kemudian cek nilai , jika nilai mutlak x dikuran x-sebelumnya kurang dari nilai epsilon yang ditentukan , atau itersi melebihi batas maksimal iterasi maka program langsung berhenti
  if (abs(x-x_sebelumnya) < epsilon or i > nMaks):
    break
#jika iterasi melebihi nilai iterasi maksimal yang ditentukan maka cetak keterangan divergen
if i > nMaks:
  print('divergen')
#sebaliknya, jika iterasi memenuhi dan mendapatkan hasil nilai sebelum iterasi maksimal , maka cetak hasil akar x dan cetak f(x)
else:
  print('Hasil akar, x = ',x)
  print('f(x) = ',f(x))