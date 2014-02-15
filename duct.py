

from __future__ import division

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider, CheckButtons, Button
import itertools
from copy import deepcopy



c0 = 343  # speed of sound
ro0 = 1.2 # air density


class SineGenerator(object):
    def __init__(self, q, freq):
        self.q = q
        self.freq = freq
        self.amp = abs(q)
        
    def f(self, t):
        return (self.q * np.exp(2j*np.pi*self.freq*t)).real        
    
class PulseGenerator(object):
    def __init__(self, amp, delay=0):
        self.amp = amp
        self.delay = delay
        
    def f(self, t):
        return self.amp if t>self.delay and t<self.delay+0.001 else 0


class MonopoleSource(object):
    def __init__(self, position, generator, name=''):
        self.pos = position
        self.generator = generator
        self.name = name

        self.pAmpl = abs(generator.amp * ro0*c0)
        self.uAmpl = abs(generator.amp)

    def p(self, x, t):
        arg = t-abs(x-self.pos)/c0
        if arg>0:
            return self.generator.f(arg) * ro0*c0
        else:
            return 0
        
    def u(self, x, t):
        sign = 1 if (x>=self.pos) else -1
        arg = t-abs(x-self.pos)/c0
        if arg>0:
            return self.generator.f(arg) * sign
        else:
            return 0

class DipoleSource(object):
    def __init__(self, position, generator, name=''):
        self.pos = position
        self.generator = generator
        self.name = name

        self.pAmpl = abs(generator.amp * ro0*c0)
        self.uAmpl = abs(generator.amp)

    def p(self, x, t):
        arg = t-abs(x-self.pos)/c0
        sign = 1 if (x>=self.pos) else -1
        if arg>0:
            return self.generator.f(arg) * ro0*c0 * sign
        else:
            return 0
        
    def u(self, x, t):
        arg = t-abs(x-self.pos)/c0
        if arg>0:
            return self.generator.f(arg)
        else:
            return 0

       

# range of x coordinate for plots is from 0 to xMax
xMax = 5
nPOINTS = 200  # number of points on x-axis
SPEED = 1/4000 # slow down time


def x2pnt(x):
    "transform x coordinate to points"
    return int(x/xMax * nPOINTS)

def pnt2x(p):
    "transform number of points to x coordinate"
    return p/nPOINTS * xMax



    
def animate(sources, reflect=False):
    fig = plt.figure()

    # create reflection images of sources
    if reflect:
        reflectedSources = []
        for src in sources:
            reflSrc = deepcopy(src)
            reflSrc.pos = -src.pos
            reflectedSources.append(reflSrc)

            
    # subplot for every source
    lines = []
    for i, src in enumerate(sources):
        # pressure on left y axis
        ax1 = fig.add_subplot(len(sources)+1, 1, i+1)
        ax1.set_xlim([0, xMax])
        yLim = src.pAmpl * 1.3 * (1+reflect)
        ax1.set_ylim([-yLim, yLim])
        ax1.set_ylabel('p')
        line_pSrc, = plt.plot([], [], 'r--', lw=1)
        line_pRefl, = plt.plot([], [], 'r:', lw=1)
        line_p, = plt.plot([], [], 'r', lw=1, label='p')
        ax1.legend(loc='upper left')
                
        # velocity on right y axis
        ax2 = ax1.twinx()
        ax2.set_xlim([0, xMax])
        yLim = src.uAmpl * 2  * (1+reflect)
        ax2.set_ylim([-yLim, yLim])
        ax2.set_ylabel('u')
        line_uSrc, = plt.plot([], [], 'b--', lw=1)
        line_uRefl, = plt.plot([], [], 'b:', lw=1)
        line_u, = plt.plot([], [], 'b', lw=1, label='u')
        ax2.legend(loc='upper right')

        ax1.set_title(src.name)
        lines.append([line_pSrc, line_uSrc, line_pRefl, line_uRefl, line_p, line_u])

    # subplot for total pressure and velocity
    # pressure on left y axis
    ax1 = fig.add_subplot(len(sources)+1, 1, len(sources)+1)
    ax1.set_xlim([0, xMax])
    yLim = sum([src.pAmpl for src in sources]) * 1.3 * (1+reflect)
    ax1.set_ylim([-yLim, yLim])
    ax1.set_ylabel('p')
    line_p, = plt.plot([], [], 'r', lw=1, label='p')
    ax1.legend(loc='upper left')

    # velocity on right y axis
    ax2 = ax1.twinx()
    ax2.set_xlim([0, xMax])
    yLim = sum([src.uAmpl for src in sources]) * 2 * (1+reflect)
    ax2.set_ylim([-yLim, yLim])
    ax2.set_ylabel('u')
    line_u, = plt.plot([], [], 'b', lw=1, label='u')
    ax2.legend(loc='upper right')

    ax1.set_title('Sum of all sources')
    lineSum = [line_p, line_u]

    
    # interactive plots :)
    plt.subplots_adjust(left=0.15, top=0.9)
    showVelocity = [not reflect]  # value in list - a hack to use nonlocal in Python 2
    showPressure = [True]
    checkAx = plt.axes([0.05, 0.6, 0.05, 0.15])
    checkButtons = CheckButtons(checkAx, ('p', 'v'), (True, showVelocity[0]))
    def toggleLines(label):
        if label == 'p': 
            showPressure[0] = not showPressure[0]
        elif label == 'v':
            showVelocity[0] = not showVelocity[0]
    checkButtons.on_clicked(toggleLines)

    resetAnimation = [False]
    buttonAx = plt.axes([0.05, 0.85, 0.05, 0.04])
    button = Button(buttonAx, 'Reset', hovercolor='0.975')
    def reset(event):
        resetAnimation[0] = True
    button.on_clicked(reset)
    

    

    def drawBackground():
        for iSrc, src in enumerate(sources):
            lines[iSrc][0].set_data([src.pos, src.pos],
                                    [-src.pAmpl * 3, src.pAmpl * 3])
            for line in lines[iSrc][1:]:
                line.set_data([], [])
        
        lineSum[0].set_data([], [])
        lineSum[1].set_data([], [])
        
        return tuple(itertools.chain(*lines)) + tuple(lineSum)
        
    def drawFrame(i):
        t = i * SPEED
        x = np.linspace(0, xMax, nPOINTS)
        pSum = np.zeros(nPOINTS)
        uSum = np.zeros(nPOINTS)
        for iSrc, src in enumerate(sources):
            pDirect = np.zeros(nPOINTS)
            uDirect = np.zeros(nPOINTS)
            pRefl = np.zeros(nPOINTS)
            uRefl = np.zeros(nPOINTS)
            p = np.zeros(nPOINTS)
            u = np.zeros(nPOINTS)
            for i in xrange(0, nPOINTS):
                pDirect[i] = src.p(pnt2x(i), t)
                uDirect[i] = src.u(pnt2x(i), t)
                if reflect:
                    pRefl[i] = reflectedSources[iSrc].p(pnt2x(i), t)
                    uRefl[i] = reflectedSources[iSrc].u(pnt2x(i), t)
                pSum[i] += (pDirect[i] + pRefl[i])
                uSum[i] += (uDirect[i] + uRefl[i])

            p = pDirect + pRefl
            u = uDirect + uRefl

            if showPressure[0]:
                lines[iSrc][0].set_data(x, pDirect)
                lines[iSrc][2].set_data(x, pRefl)
                lines[iSrc][4].set_data(x, p)
            else:
                lines[iSrc][0].set_data([], [])
                lines[iSrc][2].set_data([], [])
                lines[iSrc][4].set_data([], [])
            if showVelocity[0]:
                lines[iSrc][1].set_data(x, uDirect)
                lines[iSrc][3].set_data(x, uRefl)
                lines[iSrc][5].set_data(x, u)
            else:
                lines[iSrc][1].set_data([], [])
                lines[iSrc][3].set_data([], [])
                lines[iSrc][5].set_data([], [])

        if showPressure[0]:
            lineSum[0].set_data(x, pSum)
        else:
            lineSum[0].set_data([], [])
        if showVelocity[0]:
            lineSum[1].set_data(x, uSum)
        else:
            lineSum[1].set_data([], [])

        return tuple(itertools.chain(*lines)) + tuple(lineSum)

    def cnt():
        i = 0
        while True:
            yield i
            if resetAnimation[0]:
                i = 0
                resetAnimation[0] = False
            else:
                i += 1
        
    anim = animation.FuncAnimation(fig, drawFrame, init_func=drawBackground,
                                   frames=cnt, interval=40, blit=True, repeat=False)
    plt.show()


    


