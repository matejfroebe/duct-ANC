"""
Similar to example in chapter 5.15

The duct is closed only on the left side at x=0. Primary source is on the right
and secondary on the left at x=0.
"""

from __future__ import division
import numpy as np
import duct


duct.xMax = 5

freq = 50
waveLength = duct.c0 / freq
k = 2*np.pi / waveLength



L = 2

ampPrim = 0.01
sp = duct.MonopoleSource(position=L, generator=duct.PulseGenerator(ampPrim, 0),
                         name='Primary source')

# Amplitude and delay to ensure no reflected sound.
# Compared to equation 5.15.4 in Nelson&Elliott we added factor 1/2,
# because in our case the duct is opened on primary source side.
ampSec = -ampPrim/2
delay = L/duct.c0
ss = duct.MonopoleSource(position=0, generator=duct.PulseGenerator(ampSec, delay),
                         name='Secondary source')

duct.animate([sp, ss], reflect=True)




