# -*- coding: utf-8 -*-
"""GCD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NI9e4VcXzx-32XATa51d5Vt0nkzcRwRx
"""

def Dcf(m,n):
  
  for i in range (1,min(m,n)+1):
    if(m%i==0 and n%i==0):
     mrcf=i
  return (mrcf)

print(Dcf(49,70))