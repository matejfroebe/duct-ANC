
"""
Again two secondary sources, this time with sine waves.
"""

from __future__ import division
import numpy as np
import duct


duct.xMax = 10

freq = 50
waveLength = duct.c0 / freq

qp = 1
primSrc = duct.MonopoleSource(position=1,
                              generator=duct.SineGenerator(qp, freq),
                              name='Primary source')

d = 0.5
L = waveLength * 3/4
k = 2*np.pi / waveLength

qs2 = -qp * np.exp(-1j*k*L) / (2j*np.sin(k*d))
qs1 = -qs2 * np.exp(-1j*k*d)

secSrc1 = duct.MonopoleSource(position=1+L,
                              generator=duct.SineGenerator(qs1, freq),
                              name='Secondary source 1')
secSrc2 = duct.MonopoleSource(position=1+L+d,
                              generator=duct.SineGenerator(qs2, freq),
                              name='Secondary source 2')
duct.animate([primSrc, secSrc1, secSrc2])

    





