#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import epics


def main():
  x = np.linspace(0, 900, 1800)
  #x = x - (610-530) 
  y = (-3.1729E-7*(x**3))+(6.4899E-4*(x**2)) + (-0.51501*x) + 210.82
  fp = np.concatenate((np.array([x[0], x[1] - x[0], y.size]), y))
  print fp[900]
  pv = epics.PV('XF:23ID1-OP{Mono-Corr}Val:Table1-Wfrm')
  pv.put(fp)

if __name__ == "__main__":

  main()
   
  
