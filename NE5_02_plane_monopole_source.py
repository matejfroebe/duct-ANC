"""
Monopole source is a good approximation for speaker mounted on the wall
of the duct if the wavelength of sound wave is much longer than the width
of duct.
"""

from __future__ import division
import numpy as np
import duct


freq = 50

#s = duct.MonopoleSource(position=1, generator=duct.PulseGenerator(amp=1, delay=0))
s = duct.MonopoleSource(position=1, generator=duct.SineGenerator(q=0.001, freq=freq))


duct.animate([s])




