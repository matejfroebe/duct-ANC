
"""
We can get rid of reflected sound, if we use two secondary sources.

Primary source radiates two rectangular pulses with opposite amplitude.
The result is ping pong pictured in figure 5.15 in the book.
"""

from __future__ import division
import numpy as np
import duct


duct.xMax = 10


L = 3
d = 1
amp = 0.01
primSrc_pulse1 = duct.MonopoleSource(position=1,
                                     generator=duct.PulseGenerator(amp),
                                     name='Primary source, 1st pulse')
primSrc_pulse2 = duct.MonopoleSource(position=1,
                                     generator=duct.PulseGenerator(-amp, 2*d/duct.c0),
                                     name='Primary source, 2st pulse')
secSrc1 = duct.MonopoleSource(position=1+L,
                              generator=duct.PulseGenerator(amp, (L+2*d)/duct.c0),
                              name='Secondary source 1')
secSrc2 = duct.MonopoleSource(position=1+L+d,
                              generator=duct.PulseGenerator(-amp, (L+d)/duct.c0),
                              name='Secondary source 2')
duct.animate([primSrc_pulse1, primSrc_pulse2, secSrc1, secSrc2])
    





