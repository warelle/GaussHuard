#coding: UTF-8

import math
import cmath
import random

import scipy.linalg as slinalg
import numpy.linalg as linalg
import numpy as np


#------------------------------------
# function definition
#------------------------------------

def expand(a,b):
  (size,_) = a.shape
  r = np.zeros((size,size+1), dtype=np.double)
  for i in range(0,size):
    r[i,size] = b[i]
    for j in range(0,size):
      r[i,j] = a[i,j]
  return r,size

def solver(a, b):
  r,n = expand(a,b)
  for k in range(0,n):
    for j in range(k,n+1):
      for l in range(0,k):
        r[k,j] -= r[k,l]*r[l,j]
    for i in range(k+1, n+1):
      r[k,i] = r[k,i]/r[k,k]
    r[k,k] = 1.0
    for i in range(0,k):
      for j in range(k+1, n+1):
        r[i,j] -= r[i,k]*r[k,j]

  return r[0:n,n]


