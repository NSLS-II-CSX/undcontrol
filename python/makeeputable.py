#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import epics

def main():
  x = np.linspace(100, 1600, 30000)
  y = (-2.0226E-8*(x**3))+(1.945E-5*(x**2)) + (0.018702*x) + 10.785
  y = y * 1000.0
  fp = np.concatenate((np.array([x[0], x[1] - x[0], y.size]), y))
  print fp[:20]
  pv = epics.PV('XF:23ID-ID{EPU:2-FLT}Val:Table1-Wfrm')
  print pv.put(fp)

  x = np.linspace(10, 260, 25000)
  y = (0.13797*(x**3)) + (-8.3582*(x**2)) + (210.06*x) - 1565.3
  x = x * 1000.0
  fp = np.concatenate((np.array([x[0], x[1] - x[0], y.size]), y))
  print fp[:20]
  pv = epics.PV('XF:23ID-ID{EPU:2-RLT}Val:Table1-Wfrm')
  print pv.put(fp)

if __name__ == "__main__":

  main()
   
  
