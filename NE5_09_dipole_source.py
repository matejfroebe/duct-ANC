
"""
alternative means of generating sound
"""

from __future__ import division
import numpy as np
import duct


duct.xMax = 10

freq = 50

f = 1
s = duct.DipoleSource(position=4, generator=duct.SineGenerator(f/(duct.ro0*duct.c0), freq))
#s = duct.DipoleSource(position=4, generator=duct.PulseGenerator(amp=1/(duct.ro0*duct.c0), delay=0))


duct.animate([s])




