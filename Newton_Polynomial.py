"""
NEWTON INTERPOLATING POLYNOMIALS 
University of Alberta
https://engcourses-uofa.ca/books/numericalanalysis/polynomial-interpolation/newton-interpolating-polynomials/
"""
 
import numpy as np
import sympy as sp
sp.init_printing(use_latex=True)

Data = [(1, 3), (4, 5), (5, 6), (6, 8), (7, 8)]
x = sp.symbols('x')
def f(anydata):
  if len(anydata) == 1:
    return anydata[0][1]
  elif len(anydata) == 2:
    return (anydata[1][1] - anydata[0][1])/(anydata[1][0] -anydata[0][0])
  else:
    return (f(anydata[1:]) - f(anydata[:-1]))/(anydata[len(anydata)-1][0] - anydata[0][0])
def NP(anydata):
  return sum([f(anydata[0:i+1])*np.prod([(x - anydata[j][0]) for j in range(i)]) for i in range(len(anydata))])
# Using the Newton polynomial function
display("y: ",sp.expand(NP(Data)))
# Using the interpolating polynomial built-in function
display("y2: ",sp.interpolate(Data, x))