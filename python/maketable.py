#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import epics

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

  f = interp1d(data[:,1], data[:,0], kind = 'cubic')
  newx = np.linspace(data[0,1], data[-1,1], 100000)
  fp = f(newx)
  fp = np.concatenate((np.array([newx[0], newx[1] - newx[0], newx.size]), fp))
  print fp
  pv = epics.PV('XF:23ID-ID{EPU:1-FLK}Val:Table-Wfrm')
  pv.put(fp) 

if __name__ == "__main__":

  main()
  #plt.show()  
