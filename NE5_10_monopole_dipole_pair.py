
from __future__ import division
import numpy as np
import duct


duct.xMax = 10

freq = 50
waveLength = duct.c0 / freq
k = 2*np.pi / waveLength

qp = 0.01
primSrc = duct.MonopoleSource(position=1, generator=duct.SineGenerator(qp, freq),
                              name='Primary source')

L = waveLength * 3/4

f = - duct.ro0 * duct.c0 * qp/2 * np.exp(-1j*k*L)
qs = -qp/2 * np.exp(-1j*k*L)

secMonoSrc = duct.MonopoleSource(position=1+L, generator=duct.SineGenerator(qs, freq),
                                 name='Secondary monopole source')
secDipoleSrc = duct.DipoleSource(position=1+L, generator=duct.SineGenerator(f/(duct.ro0*duct.c0), freq),
                                 name='Secondary dipole source')

duct.animate([primSrc, secMonoSrc, secDipoleSrc])




