#coding: UTF-8

import math
import cmath
import random

import scipy.linalg as slinalg
import numpy.linalg as linalg
import numpy as np

import solver

#------------------------------------
# function definition
#------------------------------------
def generate_a(size):
  r = np.zeros((size,size), dtype=np.double)
  for i in range(0,size):
    for j in range(0,size):
      r[i,j] = random.uniform(-1,1)
  return r

def generate_x(size):
  r = np.zeros(size, dtype=np.double)
  for i in range(0,size):
    r[i] = random.uniform(-1,1)
  return r

def test(size):
  a = generate_a(size)
  x = generate_x(size)
  b = a.dot(x)
  xx = solver.solver(a,b)
  print(x)
  print("result:",xx)
  print(linalg.norm(x-xx))

test(128)
