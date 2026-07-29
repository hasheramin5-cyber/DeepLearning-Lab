import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as anim
from myfunctions import *

r1 = 4
r2 = 4
r3 = 1.3

w1 = 44
w2 = -17
w3  = -54

p1 = 0
p2 = 0
p3 = 0

fig, ax = initFigureWindow()
trace = initLine(ax)
theta = np.linspace(0, 2 * np.pi, 1000)

z = (r1 * np.exp((theta * w1 + p1) * 1j)+
     r2 * np.exp((theta * w2 + p2) * 1j)+
     r3 * np.exp((theta * w3 + p3) * 1j))

ax.axis([-10, 10, -10, 10])

myanimation = anim.FuncAnimation(fig,
                                 lambda frame: spiroanimation(frame, trace, z),
                                 frames=1000,
                                 interval = 10)
                            
plt.show()