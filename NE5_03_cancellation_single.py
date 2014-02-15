

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
    s1 = duct.MonopoleSource(position=1, generator=duct.SineGenerator(q1, freq))
    s2 = duct.MonopoleSource(position=1+L, generator=duct.SineGenerator(q2, freq))


# pulse
else:
    s1 = duct.MonopoleSource(position=3, generator=duct.PulseGenerator(amp=1, delay=0))
    L = 2
    delay = L/duct.c0
    s2 = duct.MonopoleSource(position=3+L, generator=duct.PulseGenerator(amp=-1, delay=delay))

    
duct.animate([s1, s2])




