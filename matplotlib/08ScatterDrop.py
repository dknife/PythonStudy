# -----------------------------------------------------------------------------
# 2017, Young-Min Kang. All Rights Reserved.
# Harmonic Oscillator
# -----------------------------------------------------------------------------

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

matplotlib.rcParams['toolbar'] = 'None'

fig = plt.figure(figsize=(6, 6), facecolor='white')

N = 500
P = np.ones((N,2))
P[:,0] = np.linspace(-10,10,N)
P[:,1] = 3*np.cos(P[:,0]) + 10
V = np.random.uniform(0,0, (N,2))
k = 10.0
d = 0.1
g = np.array([0,-9.8])
scat = plt.scatter(P[:, 0], P[:, 1], s=1.5, c='red')
plt.xlim(-10,10)
plt.ylim(0,20)

startFlag = True

def start(event) :
    global startFlag
    startFlag = True

def reset(event) :
    global P, V, startFlag, N
    P = np.ones((N, 2))
    P[:, 0] = np.linspace(-10, 10, N)
    P[:, 1] = 3 * np.cos(P[:, 0]) + 10
    V = np.random.uniform(0, 0, (N, 2))
    startFlag = False

def update(frame) :
    global P, S, k, d, startFlag, N
    if startFlag is False:
        scat.set_offsets(P)
        return scat,
    h = 0.001
    for i in range(N):
        V[i] += g*h
    for i in range(N):
        P[i] += V[i]

    # collision
    e = np.random.uniform(0.9, 0.9, 1); #0.5;
    for i in range(N):
        if P[i][1] < 0:
            e = 0.5 + np.abs(P[i][0]/20.0)
            P[i][1] -= (1.0+e)*P[i][1]
            if V[i][1] < 0:
                V[i][1] -= (1.0 + e) * V[i][1]

    scat.set_offsets(P)
    return scat,

plt.grid(True)

startBox = plt.axes([0.1, 0.9, 0.1, 0.05])
bStart = Button(startBox, 'Drop')
bStart.on_clicked(start)

resetBox = plt.axes([0.2, 0.9, 0.1, 0.05])
bReset = Button(resetBox, 'Reset')
bReset.on_clicked(reset)

animation = FuncAnimation(fig, update, interval = 10, frames=500, blit=True )
#animation.save('curveDrop.mp4', writer="ffmpeg")
plt.show()