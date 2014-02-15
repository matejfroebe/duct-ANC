
"""
What happens if sound is reflected at x=0?
"""

from __future__ import division
import numpy as np
import duct


duct.xMax = 10

freq = 50
waveLength = duct.c0 / freq
k = 2*np.pi / waveLength


D=1
L=2

# at D=0 and kL=pi/2+n*pi we will have truble - check the amplitude of sec source
#D = 0.01
#L = np.pi/(2*k)

qp = 0.01
primSrc = duct.MonopoleSource(position=D, generator=duct.SineGenerator(qp, freq),
                         name='Primary source')

# equation 5.11.4 for R=1
qs = -qp*(np.exp(1j*k*D) + np.exp(-1j*k*D)) / (np.exp(1j*k*L) + np.exp(-1j*k*L))

secSrc = duct.MonopoleSource(position=L, generator=duct.SineGenerator(qs, freq),
                         name='Secondary source')

duct.animate([primSrc, secSrc], reflect=True)




