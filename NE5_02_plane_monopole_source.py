

from __future__ import division
import numpy as np
import duct


freq = 50

#s = duct.MonopoleSource(position=1, generator=duct.PulseGenerator(amp=1, delay=0))
s = duct.MonopoleSource(position=1, generator=duct.SineGenerator(q=0.001, freq=freq))


duct.animate([s])




