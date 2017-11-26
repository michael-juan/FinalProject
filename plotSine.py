import numpy as np
import matplotlib.pyplot as mpl
xAxis = np.arange(0, 10, 0.1)

amplitude   = np.sin(xAxis)
mpl.plot(xAxis, amplitude)
mpl.grid(True, which='both')
mpl.axhline(y=0, color='k')
mpl.show()

