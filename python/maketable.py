#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import epics
from pyspec import fit
from pyspec import fitfuncs

def power(x, p, mode = 'eval'):
   """polynomial
   Function:
      :math:`f(x) = p_0 p_1^x`
   """
   if mode == 'eval':
       out = p[0] + (p[1] * x) + (p[2] * x**2) + (p[3] * x**3)
   elif mode == 'params':
       out = ['A', 'B', 'C', 'D']
   elif mode == 'name':
       out = "Power"
   elif mode == 'guess':
       out = [0, 10, 0, 0]
   else:
       out = []

   return out

def fitdata(data):
  data = np.loadtxt(data)

  data[:,0] = data[:,0] * 1000

  plt.figure()
  plt.plot(data[:,1], data[:,0], 'ro')
  f = fit.fitdata([power]) 
  x = np.linspace(100, 3200, 100000)
  y = f.evalfitfunc(x = x)[1]
  plt.plot(x, y, 'b-')
  ny = np.concatenate((np.array([x[0], x[1] - x[0], x.size]), y))
  pv = epics.PV('XF:23ID-ID{EPU:1-FLT}Val:Table1-Wfrm')
  pv.put(ny)
  pv = epics.PV('XF:23ID-ID{EPU:2-FLT}Val:Table1-Wfrm')
  pv.put(ny)
  
  rx = np.linspace(11000, 290000, 100000)
  f = interp1d(y[::100], x[::100], kind = 'cubic')
  print y[::100][-1]
  ry = f(rx)
  plt.figure()
  plt.plot(rx, ry, 'b-')
  plt.plot(data[:,0], data[:,1], 'ro')
  ry = np.concatenate((np.array([rx[0], rx[1] - rx[0], rx.size]), ry))
  pv = epics.PV('XF:23ID-ID{EPU:1-RLT}Val:Table1-Wfrm')
  pv.put(ry)
  pv = epics.PV('XF:23ID-ID{EPU:2-RLT}Val:Table1-Wfrm')
  pv.put(ry)

def main():
  data = np.loadtxt('PhotEnVsPer34x34LH.dat')
  data[:,0] = data[:,0] * 1000

  f = interp1d(data[:,0], data[:,1], kind = 'cubic')
  newx = np.linspace(data[0,0], data[-1,0], 100000)
  fp = f(newx)
  fp = np.concatenate((np.array([newx[0], newx[1] - newx[0], newx.size]), fp))
  print fp
  pv = epics.PV('XF:23ID-ID{EPU:1-RLK}Val:Table-Wfrm')
  pv.put(fp)
  pv = epics.PV('XF:23ID-ID{EPU:2-RLK}Val:Table-Wfrm')
  pv.put(fp)

  f = interp1d(data[:,1], data[:,0], kind = 'cubic')
  newx = np.linspace(data[0,1], data[-1,1], 100000)
  fp = f(newx)
  fp = np.concatenate((np.array([newx[0], newx[1] - newx[0], newx.size]), fp))
  print fp
  pv = epics.PV('XF:23ID-ID{EPU:1-FLK}Val:Table-Wfrm')
  pv.put(fp) 
  pv = epics.PV('XF:23ID-ID{EPU:2-FLK}Val:Table-Wfrm')
  pv.put(fp) 

if __name__ == "__main__":

  #main()
  f = fitdata('PhotEnVsPer34x34LH.dat')
  plt.show()  
