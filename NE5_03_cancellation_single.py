
"""
Primary source represents unwanted noise and we use secondary sound source
to cancel it. The problem is that the sound from primary source is reflected
from sec. source.

If we would try to measure sound from primary source with microphone,
it would also pick the reflected sound and we couldn't calculate the right
signal for secondary source.
"""

from __future__ import division
import numpy as np
import duct

duct.xMax = 10


# sine waves
if 0:
    freq = 50
    waveLength = duct.c0 / freq
    k = 2*np.pi / waveLength

    q1 = 1
    #L = waveLength/2 # cancelation in both directions
    L = waveLength * 5/8
    #L = waveLength * 3/4
    #L = waveLength

    q2 = -q1 * np.exp(-1j*k*L) # necessary for calculation
    primSrc = duct.MonopoleSource(position=1, generator=duct.SineGenerator(q1, freq))
    secSrc = duct.MonopoleSource(position=1+L, generator=duct.SineGenerator(q2, freq))


# pulse
else:
    primSrc = duct.MonopoleSource(position=3, generator=duct.PulseGenerator(amp=1, delay=0))
    L = 2
    delay = L/duct.c0
    secSrc = duct.MonopoleSource(position=3+L, generator=duct.PulseGenerator(amp=-1, delay=delay))

    
duct.animate([primSrc, secSrc])




