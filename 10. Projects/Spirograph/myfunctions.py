import numpy as np
import matplotlib.pylab as plt

def initLine(ax):
  return ax.plot([], [], color = 'white')[0]

def spiroanimation(frame, trace, z):
  trace.set_data(np.real(z)[:frame], np.imag(z)[:frame])
  return trace
def initFigureWindow():
  fig, ax = plt.subplots(figsize=(5,5))
  fig.canvas.manager.window.geometry('+1400+1')
  fig.patch.set_facecolor('k')
  ax.patch.set_facecolor('k')
  return fig, ax