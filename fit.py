# -*- coding: utf-8 -*-
"""fit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AcS0KMEsUdHeoPoZrFC6JTWsNgOqRahJ
"""

import astropy

from matplotlib.colors import LogNorm

# Commented out IPython magic to ensure Python compatibility.
import numpy as np

# Set up matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline

from astropy.io import fits

hdu_list = astropy.io.fits.open('re.fits')

hdu_list.info()

im = hdu_list[6].data # for detector 6
plt.imshow(im, norm=LogNorm())
plt.colorbar()
plt.title("Observed Star Field")
plt.xlabel("X Pixels")
plt.ylabel("Y Pixels")
plt.grid()
plt.show()

im = hdu_list[1].data
plt.imshow(im, cmap='gray')
plt.colorbar()

