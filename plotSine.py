import numpy as np
import matplotlib.pyplot as plot
xAxis = np.arange(0, 10, 0.1)

amplitude   = np.sin(xAxis)
plot.plot(xAxis, amplitude)
plot.grid(True, which='both')
plot.axhline(y=0, color='k')
plot.show()

